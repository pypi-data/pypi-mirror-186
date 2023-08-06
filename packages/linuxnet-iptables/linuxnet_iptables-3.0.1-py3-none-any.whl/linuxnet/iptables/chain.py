# Copyright (c) 2021, 2022, Panagiotis Tsirigotis

# This file is part of linuxnet-iptables.
#
# linuxnet-iptables is free software: you can redistribute it and/or
# modify it under the terms of version 3 of the GNU Affero General Public
# License as published by the Free Software Foundation.
#
# linuxnet-iptables is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General
# Public License along with linuxnet-iptables. If not, see
# <https://www.gnu.org/licenses/>.

"""This module provides the Chain class
"""

import traceback

from typing import Callable, List, Optional

from .exceptions import (
        IptablesError, IptablesParsingError, IptablesExecutionError)
from .rule import ChainRule
from .target import ChainTarget
from .deps import get_logger

_logger = get_logger('linuxnet.iptables.chain')

# pylint: disable=too-many-instance-attributes,too-many-public-methods

class Chain:
    """This class is used to represent an iptables chain.
    A chain contains a list of rules which can be referenced by
    number (rule numbers start with 1).
    """

    def __init__(self,          # pylint: disable=too-many-arguments
                        chain_name: str,
                        policy: Optional[str] =None,
                        reference_count=0,
                        packet_count=0, byte_count=0):
        """
        :param chain_name: real chain name
        :param policy: the chain policy if this is a builtin chain, ``None``
            otherwise
        :param reference_count: number of rules referencing this chain
        :param packet_count: number of packets that flowed through this chain
        :param byte_count: number of bytes that flowed through this chain
        """
        self.__real_chain_name = chain_name
        self.__policy = policy
        # The policy packet/byte count are the stats associated with
        # the chain policy (applicable only for builtin chains)
        self.__policy_packet_count = packet_count
        self.__policy_byte_count = byte_count
        self.__reference_count = reference_count
        self.__packet_count = 0
        self.__byte_count = 0
        self.__rule_list = []
        self.__pft = None

    def __str__(self):
        return f'Chain({self.__real_chain_name})'

    def is_builtin(self) -> bool:
        """Returns ``True`` if this is a built-in chain (e.g. ``INPUT``)
        """
        return self.__policy is not None

    def get_reference_count(self) -> int:
        """Returns the reference count of a (non-builtin) chain; returns 0
        for builtin chains
        """
        return self.__reference_count

    def get_policy_packet_count(self) -> int:
        """Returns the number of packets that were handled as per
        the chain policy; returns 0 for non-builtin chains
        """
        return self.__policy_packet_count

    def get_policy_byte_count(self) -> int:
        """Returns the number of bytes that were handled as per
        the chain policy; returns 0 for non-builtin chains
        """
        return self.__policy_byte_count

    def get_packet_count(self) -> int:
        """Returns the packet count of the chain
        """
        return self.__packet_count

    def get_byte_count(self) -> int:
        """Returns the byte count of the chain
        """
        return self.__byte_count

    def get_real_name(self) -> str:
        """Returns the real chain name
        """
        return self.__real_chain_name

    def get_logical_name(self) -> str:
        """Returns the logical chain name
        """
        if self.__pft is None:
            return self.__real_chain_name
        return self.__pft.rcn2lcn(self.__real_chain_name)

    def get_policy(self) -> Optional[str]:
        """Returns the policy of the (builtin) chain, or ``None`` if
        this is not a builtin chain.
        """
        return self.__policy

    def has_unparsed_rules(self) -> bool:
        """Returns ``True`` if the chain contains unparsed rules
        """
        for rule in self.__rule_list:
            if rule.parsing_failed():
                return True
        return False

    def get_unparsed_rule_count(self) -> int:
        """Returns the number of unparsed rules
        """
        count = 0
        for rule in self.__rule_list:
            if rule.parsing_failed():
                count += 1
        return count

    def get_rules(self) -> List[ChainRule]:
        """Returns the chain rules.

        The return value is a copy to avoid inadvertent modifications of
        the internal rule list (since the internal rule list should reflect
        the system's state).
        """
        return self.__rule_list[:]

    def _set_rule_list(self, rule_list: List[ChainRule]) -> None:
        """Set the rule list.
        This method is only used by the parsing code, so it does not
        update any chain reference counts.
        """
        for rulenum, rule in enumerate(rule_list, 1):
            rule._set_chain(self, rulenum)   # pylint: disable=protected-access
        self.__rule_list = rule_list

    def _propagate_rule_stats(self, log_stat_failures: bool) -> None:
        """Propagate the packet/byte counts of each rule to
        the rule's target.
        This method is only used by the parsing code.
        """
        for rule in self.__rule_list:
            target = rule.get_target()
            if not isinstance(target, ChainTarget):
                continue
            target_chain = target.get_chain()
            if target_chain is None:
                if log_stat_failures:
                    _logger.warning("%s: unknown chain: %s",
                        self._propagate_rule_stats.__qualname__,
                        self.get_real_name())
                    _logger.warning("Call stack:\n%s",
                        ''.join(traceback.extract_stack().format()[:-1]))
                continue
            target_chain._update_stats(   # pylint: disable=protected-access
                                packet_count=rule.get_packet_count(),
                                byte_count=rule.get_byte_count())

    def _set_stats(self, packet_count: int, byte_count: int) -> None:
        """Set the packet/byte counts of this chain
        """
        self.__packet_count = packet_count
        self.__byte_count = byte_count

    def _update_stats(self, packet_count: int, byte_count: int) -> None:
        """Update the packet/byte counts of this chain
        """
        self.__packet_count += packet_count
        self.__byte_count += byte_count

    def find_rule_by_target_lcn(self,
                        logical_chain_name: str) -> List[ChainRule]:
        """Return a list of rules with the specified target

        :param logical_chain_name: identifies the chain targetted by the rule
        """
        rule_list = []
        for rule in self.__rule_list:
            target_chain = rule.get_target_chain()
            if target_chain is None:
                continue
            # A builtin chain may reference multiple peers, each with a
            # different prefix. We need to ignore ones not handled by our pft.
            if (self.is_builtin() and
                    not self.__pft.is_handler_of(target_chain.get_real_name())):
                continue
            if target_chain.get_logical_name() == logical_chain_name:
                rule_list.append(rule)
        return rule_list

    def find_rule_by(self, *, match=None, target=None) -> List[ChainRule]:
        """Return a list of :class:`ChainRule` objects where the rule
        contains the specified ``match`` object or has the specified ``target``
        (target comparison is by name), or both. If no ``match`` or ``target``
        is present, an empty list is returned.

        :param match: optional :class:`Match` object; use a :class:`MatchNone`
            object to find a rule that has no matches
        :param target: optional :class:`Target` object; use a :class:`TargetNone`
            object to find a rule that has no target
        """
        if match is None and target is None:
            return []
        return [rule for rule in self.__rule_list
                    if (match is None or rule.has_match(match)) and
                        (target is None or rule.has_target(target))]

    def get_pft(self):
        """Returns the :class:`IptablesPacketFilterTable` where this
        chain belongs
        """
        return self.__pft

    def set_pft(self, pft) -> None:
        """Set the :class:`IptablesPacketFilterTable` where this
        :class:`Chain` belongs.

        :param pft: an :class:`IptablesPacketFilterTable` object
        """
        self.__pft = pft

    def clear_pft(self) -> None:
        """Reset the :class:`IptablesPacketFilterTable` where this
        :class:`Chain` belongs.
        """
        self.__pft = None

    def flush(self) -> None:
        """Delete all rules from this chain
        """
        _ = self.__pft.iptables_run(['-F', self.__real_chain_name], check=True)
        for rule in self.__rule_list:
            try:
                self.__dec_target_refcount(rule.get_target())
                rule._deleted()             # pylint: disable=protected-access
            except Exception:           # pylint: disable=broad-except
                _logger.exception("%s: unexpected exception",
                                        self.flush.__qualname__)
        self.__rule_list.clear()

    def _incref(self) -> None:
        """Increase the chain reference count
        """
        self.__reference_count += 1

    def _decref(self) -> None:
        """Decrease the chain reference count
        """
        self.__reference_count -= 1
        if self.__reference_count < 0:
            # This shouldn't happen
            _logger.warning("Negative refcount for chain %s",
                                self.__real_chain_name)

    def __inc_target_refcount(self, target) -> None:
        """If target is a :class:`ChainTarget`, increase the refcount of the
        corresponding chain.
        """
        if not isinstance(target, ChainTarget):
            return
        chain = target.resolve_chain(self.__pft)
        if chain is not None:
            chain._incref()     # pylint: disable=protected-access
        else:
            _logger.warning("Missed refcount increase for chain %s",
                                target.get_target_name())

    def __dec_target_refcount(self, target) -> None:
        """If target is a :class:`ChainTarget`, decrease the refcount of the
        corresponding chain.

        :param target: a :class:`Target` object
        """
        if not isinstance(target, ChainTarget):
            return
        chain = target.resolve_chain(self.__pft)
        if chain is not None:
            chain._decref()     # pylint: disable=protected-access
        else:
            _logger.warning("Missed refcount decrease for chain %s",
                                target.get_target_name())

    def __added_rule(self, rule: ChainRule, rulenum: int):
        """Added the specified rule.
        """
        # pylint: disable=protected-access
        rule._set_chain(self, rulenum)
        self.__inc_target_refcount(rule.get_target())
        # pylint: enable=protected-access
        for i in range(rulenum, len(self.__rule_list)):
            rule = self.__rule_list[i]
            rule._inc_rulenum()  # pylint: disable=protected-access

    def append_rule(self, rule: ChainRule) -> None:
        """Append the new rule at the end of the chain
        """
        if rule.get_chain() is not None:
            raise IptablesError('rule belongs to another chain')
        rule_args = rule.to_iptables_args()
        if not rule_args:
            _logger.warning("%s: rule has no args: %s",
                self.append_rule.__qualname__, rule)
            return
        args = ['-A', self.__real_chain_name] + rule_args
        _ = self.__pft.iptables_run(args, check=True)
        self.__rule_list.append(rule)
        self.__added_rule(rule, rulenum=len(self.__rule_list))

    def insert_rule(self, rule: ChainRule, rulenum=0) -> None:
        """Insert the new rule at the beginning of the chain (by
        default) or as rule number ``rulenum``.

        :param rulenum: rule number (starting with 1)
        """
        if rule.get_chain() is not None:
            raise IptablesError('rule belongs to another chain')
        rule_args = rule.to_iptables_args()
        if not rule_args:
            _logger.warning("%s: rule has no args: %s",
                self.insert_rule.__qualname__, rule)
            return
        if rulenum < 0:
            raise IptablesError(f'invalid rule number: {rulenum}')
        rule_index = rulenum-1 if rulenum > 0 else 0
        try:
            self.__rule_list.insert(rule_index, rule)
        except IndexError as idxerr:
            raise IptablesError(
                    f'rule number out-of-range: {rulenum}') from idxerr
        args = ['-I', self.__real_chain_name, str(rule_index+1)] + rule_args
        try:
            _ = self.__pft.iptables_run(args, check=True)
        except Exception:
            self.__rule_list.pop(rule_index)
            raise
        self.__added_rule(rule, rulenum=rule_index+1)

    def delete_rule(self, rule: ChainRule) -> None:
        """Delete the specified ``rule``: the rule must belong to this chain.
        """
        if rule.get_chain() is not self:
            raise IptablesError('attempt to delete rule from wrong chain')
        rule_index = rule.get_rulenum() - 1
        if self.__rule_list[rule_index] is not rule:
            _logger.error("%s: wrong rule index '%d'; ChainRule: %s",
                self.delete_rule.__qualname__, rule_index, rule)
            raise IptablesError('internal rule list error')
        self.__delete_rule_at(rule_index)

    def delete_rulenum(self, rulenum: int) -> None:
        """Delete the rule with the specified rule number

        Raises an :class:`IptablesError` if the number is invalid

        :param rulenum: rule number (numbering starts from 1)
        """
        rule_index = rulenum - 1
        if 0 <= rule_index < len(self.__rule_list):
            self.__delete_rule_at(rule_index)
        else:
            raise IptablesError(f'bad rule number: {rulenum}')

    def __delete_rule_at(self, rule_index: int) -> None:
        """Delete the rule at index ``rule_index`` in the rule_list.
        This is the method that actually performs the deletion.
        """
        rule = self.__rule_list.pop(rule_index)
        # iptables enumerates rules starting from 1
        rulenum = rule_index + 1
        cmd = ['-D', self.__real_chain_name, f'{rulenum}']
        try:
            _ = self.__pft.iptables_run(cmd, check=True)
        except Exception as ex:
            self.__rule_list.insert(rule_index, rule)
            _logger.exception("Rule deletion failed")
            raise IptablesExecutionError(
                    f'unable to delete rule {rulenum} '
                    f'from chain {self.get_real_name()}') from ex
        rule._deleted()         # pylint: disable=protected-access
        self.__dec_target_refcount(rule.get_target())
        #
        # Renumber rules after the deleted rule
        #
        for index in range(rule_index, len(self.__rule_list)):
            rule = self.__rule_list[index]
            rule._dec_rulenum()         # pylint: disable=protected-access

    def __delete_rules(self, rule_list: List[ChainRule]) -> int:
        """Delete a number of rules
        """
        if not rule_list:
            return 0
        # We can delete rules in any order.
        # The reason for sorting in reverse rule number order is that it
        # makes debugging easier # as the rule numbers of the rules being
        # deleted do not change.
        rule_list.sort(key=lambda r: r.get_rulenum(), reverse=True)
        for rule in rule_list:
            self.__delete_rule_at(rule.get_rulenum()-1)
        return len(rule_list)

    def delete_rule_by_pred(self, pred: Callable[[ChainRule], bool]) -> int:
        """Delete all rules for which ``pred`` returns ``True``.

        Returns the number of deleted rules

        :param pred: a ``Callable`` object
        """
        deletion_list = [rule for rule in self.__rule_list if pred(rule)]
        return self.__delete_rules(deletion_list)

    def delete_rule_if(self, *, match=None, target=None) -> int:
        """Delete all rules with the specified ``match`` and/or ``target``.
        If no ``match`` or ``target`` is present, this is a no-op.

        Returns the number of deleted rules.

        :param match: optional :class:`Match` object; use a :class:`MatchNone`
            object to delete a rule that has no matches
        :param target: optional :class:`Target` object; use a :class:`TargetNone`
            object to delete a rule that has no target
        """
        if match is None and target is None:
            return 0
        deletion_list = self.find_rule_by(match=match, target=target)
        return self.__delete_rules(deletion_list)

    def delete_rule_by_target_chain(self, chain: 'Chain') -> int:
        """Delete all rules that jump/goto the specified chain.

        Returns the number of deleted rules

        :param chain: a :class:`Chain` object
        """
        return self.delete_rule_by_pred(pred=lambda r: r.targets_chain(chain))

    @classmethod
    def __parse_chain_line(cls, line) -> 'Chain':
        """Parse a line which has one of the following 2 forms:
            Chain INPUT (policy ACCEPT 9108340 packets, 10054611039 bytes)
            Chain host_origin (1 references)

        Returns a Chain object.

        It raises an IptablesParsingError in case of a parsing error.
        """
        fields = line.split(' ', 2)
        n_fields = len(fields)
        if n_fields != 3:
            raise IptablesParsingError(
                f'line has {n_fields} field(s) instead of 3', line=line)
        if fields[0] != 'Chain':
            raise IptablesParsingError("line does not start with 'Chain'",
                                line=line)
        real_chain_name = fields[1]
        packet_count = 0
        byte_count = 0
        policy = None
        reference_count = 0
        try:
            param_fields = fields[2][1:-1].split()
            if param_fields[0] == 'policy':
                policy = param_fields[1]
                if param_fields[3].startswith('packets'):
                    packet_count = int(param_fields[2])
                if param_fields[5].startswith('bytes'):
                    byte_count = int(param_fields[4])
            elif param_fields[1] == 'references':
                reference_count = int(param_fields[0])
            else:
                _logger.warning("unable to parse line: %s", line)
                return None
            return Chain(real_chain_name, policy, reference_count,
                                        packet_count, byte_count)
        except IndexError as idxerr:
            raise IptablesParsingError(
                        'insufficient number of fields', line=line) from idxerr
        except ValueError as valerr:
            raise IptablesParsingError(
                        'bad field value', line=line) from valerr

    @classmethod
    def create_from_existing(cls, line_list: List[str],
                pft: 'IptablesPacketFilterTable',
                log_parsing_failures=True) -> 'Chain':
        """Parse a set of lines from the output of ``iptables -xnv``
        into a :class:`Chain` object.

        It returns a :class:`Chain` object.

        It raises an :exc:`IptablesParsingError` if there is a parsing error.

        :param line_list: list of **iptables(8)** output lines
        :param pft: an :class:`IptablesPacketFilterTable` object
        :param log_parsing_failures: if ``True``, log any parsing failures
        """
        line_iter = iter(line_list)
        chain = cls.__parse_chain_line(next(line_iter).rstrip())
        # The next line contains the headers - skip it
        try:
            _ = next(line_iter)
        except StopIteration as stopit:
            raise IptablesParsingError(
                        'chain output lines missing headers') from stopit
        rule_list = []
        for line in line_iter:
            line = line.rstrip()
            if not line:
                continue
            try:
                rule = ChainRule.create_from_existing(line, pft)
            except IptablesParsingError:
                if log_parsing_failures:
                    _logger.exception(
                        "%s: chain=%s: error parsing rules; "
                        "will create unparsed rule",
                            cls.create_from_existing.__qualname__,
                            chain.get_real_name())
                rule = ChainRule._create_unparsed_rule(line) # pylint: disable=protected-access
            rule_list.append(rule)
        chain._set_rule_list(rule_list) # pylint: disable=protected-access
        return chain

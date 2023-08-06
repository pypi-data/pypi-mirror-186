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

"""This module defines classes corresponding to iptables(8) targets
"""

import traceback

from ipaddress import IPv4Address
from typing import List, Optional

from .deps import get_logger
from .exceptions import IptablesParsingError, IptablesError

_logger = get_logger("linuxnet.iptables.target")

class Target:
    """Parent class for all targets.
    """
    def __init__(self, target_name: str, terminates: bool):
        """
        :param target_name: the name of the target
        :param terminates: if ``True``, this target terminates processing
        """
        self.__target_name = target_name
        self.__terminates = terminates

    def __str__(self):
        return f'Target({self.__target_name})'

    def is_terminating(self) -> bool:
        """Returns ``True`` if this is a terminating target
        """
        return self.__terminates

    def get_target_name(self) -> str:
        """Returns the target name
        """
        return self.__target_name

    def __eq__(self, other):
        """Target comparison is only by name.
        This implies that we do not distinguish between targets
        with the same name but different options.
        """
        return (isinstance(other, Target) and
                self.__target_name == other.get_target_name())

    def __ne__(self, other):
        return not self.__eq__(other)

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        if not self.__target_name:
            return []
        return [self.__target_name]


class TargetNone(Target):       # pylint: disable=too-few-public-methods
    """A target that is not there.
    This class is intended to be used for comparison purposes.
    """
    def __init__(self):
        super().__init__("", terminates=False)

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        return []


class UnparsedTarget(Target):   # pylint: disable=too-few-public-methods
    """We use this class for targets we cannot parse.
    This allows us to process **iptables(8)** output without triggering
    parsing errors. An error will be triggered lazily if/when an
    object of this class is used to generate an **iptables(8)** command
    line.
    """
    def __init__(self, target_name: str, field_iter):
        """
        :param target_name: the target name
        :param field_iter: iterator returning fields of a line
        """
        super().__init__(target_name, terminates=False)
        self.__options = []
        for field in field_iter:
            if field == target_name:
                self.__options = list(field_iter)
                break
            field_iter.store_field(field)

    def get_target_options(self) -> List[str]:
        """Returns target options
        """
        return self.__options

    def is_terminating(self) -> bool:
        """Raises an :exc:`IptablesError` since we don't know if this
        target is terminating or not.
        """
        raise IptablesError(
                f"unknown if unparsed target {self.get_target_name()} "
                "is terminating or not")

    def to_iptables_args(self) -> List[str]:
        """Since this is an unparsed target, it cannot be expressed
        in **iptables(8)** arguments.
        """
        raise IptablesError(f'unable to parse options of {self}')


class LogTarget(Target):
    """This class provides access to the ``LOG`` target
    """

    __OPT_MAP = {
                   1 : '--log-tcp-sequence',
                   2 : '--log-tcp-options',
                   4 : '--log-ip-options',
                   8 : '--log-uid'
                }

    def __init__(self,          # pylint: disable=too-many-arguments
                        log_prefix: Optional[str] =None,
                        log_level: Optional[str] =None,
                        log_tcp_sequence=False,
                        log_tcp_options=False,
                        log_ip_options=False,
                        log_uid=False):
        """
        :param log_prefix: prefix to include in every log message
        :param log_level: log level; see **syslog(3)** for possible
            values, e.g. ``info`` (note that the **LOG_** prefix is
            stripped); numbers in string form (e.g. "5") are also accepted
        :param log_tcp_sequence: optional boolean (see **iptables(8)** **LOG**
           target)
        :param log_tcp_options: optional boolean (see **iptables(8)** **LOG**
           target)
        :param log_ip_options: optional boolean (see **iptables(8)** **LOG**
           target)
        :param log_uid: optional boolean (see **iptables(8)** **LOG** target)
        """
        super().__init__('LOG', terminates=False)
        self.__log_prefix = log_prefix
        self.__log_level = log_level
        self.__log_options = []
        if log_tcp_sequence:
            self.__log_options.append('--log-tcp-sequence')
        if log_tcp_options:
            self.__log_options.append('--log-tcp-options')
        if log_ip_options:
            self.__log_options.append('--log-ip-options')
        if log_uid:
            self.__log_options.append('--log-uid')

    def get_log_prefix(self) -> Optional[str]:
        """Returns the log prefix
        """
        return self.__log_prefix

    def get_log_level(self) -> Optional[str]:
        """Returns the log level
        """
        return self.__log_level

    def get_log_options(self) -> List[str]:
        """Returns the log options
        """
        return self.__log_options

    def set_log_options(self, log_options: List[str]) -> None:
        """Sets the log options
        """
        self.__log_options = log_options

    @classmethod
    def __parse_log_target_flags(cls, numstr) -> List[str]:
        """Parse a decimal value numstr into a list of arguments
        for the iptables LOG target
        """
        opt_map = cls.__OPT_MAP
        try:
            flag_mask = int(numstr)
            opts = [opt_name for opt_bit, opt_name in opt_map.items()
                                        if flag_mask & opt_bit]
            return opts
        except ValueError as valerr:
            raise IptablesParsingError(
                        "Bad TCP flag mask: " + numstr) from valerr

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        retval = super().to_iptables_args()
        if self.__log_prefix:
            retval += ['--log-prefix', self.__log_prefix]
        if self.__log_level:
            retval += ['--log-level', self.__log_level]
        retval += self.__log_options
        return retval

    @classmethod
    def _parse(cls, field_iter) -> Target:
        """Parse the LOG target options
        """
        field_iter.forward_past('LOG')
        log_level = None
        log_prefix = None
        log_options = None
        for val in field_iter:
            if val == 'flags':
                val = field_iter.next_value(val)
                log_options = cls.__parse_log_target_flags(val)
            elif val == 'level':
                log_level = field_iter.next_value(val)
            elif val == 'prefix':
                # Consume the rest of the fields
                val = ' '.join(field_iter)
                # Backquote used by iptables 1.4.7, double quote used
                # by iptables 1.8.4
                if val[0] in ("`", '"'):
                    val = val[1:-1]
                log_prefix = val
            else:
                raise IptablesParsingError(f'unknown target option: {val}')
        target = LogTarget(log_prefix, log_level)
        target.set_log_options(log_options)
        return target


class RejectTarget(Target):
    """This class provides access to the ``REJECT`` target
    """
    def __init__(self, reject_with: Optional[str] =None):
        """
        :param reject_with: optional ``ICMP`` message type
            (see **iptables(8)** **REJECT** target)
        """
        super().__init__('REJECT', terminates=True)
        self.__reject_with = reject_with

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        retval = super().to_iptables_args()
        if self.__reject_with is not None:
            retval += ['--reject-with', self.__reject_with]
        return retval

    def get_rejection_message(self) -> Optional[str]:
        """Returns the ICMP rejection message.
        """
        return self.__reject_with

    @classmethod
    def _parse(cls, field_iter) -> Target:
        """Parse the MARK target options
        """
        reject_with = 'reject-with'
        field_iter.forward_past(reject_with)
        icmp_message = field_iter.next_value(reject_with)
        return RejectTarget(reject_with=icmp_message)


class MarkTarget(Target):
    """This class provides access to the ``MARK`` target
    """
    def __init__(self, mark: Optional[int] =None, xmark: Optional[int] =None):
        """
        :param mark: value used to set the mark value in the packet
        :param xark: see **iptables(8)** **MARK** target
        """
        super().__init__('MARK', terminates=False)
        self.__mark = mark
        self.__xmark = xmark

    def get_mark(self) -> Optional[int]:
        """Returns the mark value set by this target
        """
        return self.__mark

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        retval = super().to_iptables_args()
        if self.__mark is not None:
            retval += ['--set-mark', f'0x{self.__mark:x}']
        if self.__xmark is not None:
            retval += ['--set-xmark', f'0x{self.__xmark}']
        return retval

    @classmethod
    def _parse(cls, field_iter) -> Target:
        """Parse the MARK target options
        """
        field_iter.forward_past('MARK')
        mark = None
        xmark = None
        for val in field_iter:
            if val == 'set':
                mark = int(field_iter.next_value(val), 16)
            elif val == 'xset':
                xmark = int(field_iter.next_value(val), 16)
            else:
                raise IptablesParsingError(f'unknown MARK argument: {val}')
        return MarkTarget(mark=mark, xmark=xmark)


class ConnmarkTarget(Target):
    """This class provides access to the ``CONNMARK`` target
    """
    def __init__(self, *, mark: Optional[int] =None,
                        xmark: Optional[int] =None, restore_mark=False):
        """
        :param mark: value used to set the ctmark value (associated with
            a connection)
        :param xark: see **iptables(8)** **CONNMARK** target
        :param restore_mark: if ``True``, copy the connection mark to the
            packet mark
        """
        super().__init__('CONNMARK', terminates=False)
        self.__mark = mark
        self.__xmark = xmark
        self.__restore_mark = restore_mark

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        retval = super().to_iptables_args()
        if self.__restore_mark:
            retval += ['--restore-mark']
        if self.__mark is not None:
            retval += ['--set-mark', str(self.__mark)]
        if self.__xmark is not None:
            retval += ['--set-xmark', str(self.__xmark)]
        return retval

    def get_mark(self) -> Optional[int]:
        """Returns the mark to set
        """
        return self.__mark

    def get_xmark(self) -> Optional[int]:
        """Returns the xmark to set
        """
        return self.__xmark

    def is_restoring_mark(self) -> bool:
        """Returns True if we are restoring the mark
        """
        return self.__restore_mark

    def restore_mark(self) -> None:
        """Sets the restore mark flag
        """
        self.__restore_mark = True

    @classmethod
    def _parse(cls, field_iter) -> Target:
        """Parse the CONNMARK target options
        """
        field_iter.forward_past('CONNMARK')
        mark = None
        xmark = None
        restore_mark = False
        for val in field_iter:
            if val == 'set':
                mark = int(field_iter.next_value(val), 16)
            elif val == 'xset':
                xmark = int(field_iter.next_value(val), 16)
            elif val == 'restore':
                restore_mark = True
            else:
                raise IptablesParsingError(
                            f'unknown CONNMARK argument: {val}')
        return ConnmarkTarget(mark=mark, xmark=xmark,
                                        restore_mark=restore_mark)


class _NatTarget(Target):
    """This class provides access to the SNAT/DNAT targets.
    """
    def __init__(self, *, nat_target: str, nat_option: str,
                        addr: Optional[IPv4Address],
                        port: Optional[int], last_port: Optional[int],
                        is_random: bool, is_persistent: bool):
        super().__init__(nat_target, terminates=True)
        self.__nat_option = nat_option
        self.__addr = addr
        self.__port = port
        self.__last_port = last_port
        self.__is_random = is_random
        self.__is_persistent = is_persistent

    def get_address(self) -> Optional[IPv4Address]:
        """Returns the address used for [SD]NAT
        """
        return self.__addr

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        retval = super().to_iptables_args()
        dest_spec = ''
        if self.__addr is not None:
            dest_spec += str(self.__addr)
        if self.__port is not None:
            dest_spec += f':{self.__port:d}'
            if self.__last_port is not None:
                dest_spec += f'-{self.__last_port:d}'
        retval += [self.__nat_option, dest_spec]
        if self.__is_random:
            retval.append('--random')
        if self.__is_persistent:
            retval.append('--persistent')
        return retval

    @staticmethod
    def _parse_nat(target_name, field_iter):
        """Parse the [SD]NAT target options
        Returns a kwargs dictionary
        """
        # pylint: disable=undefined-loop-variable, too-many-branches
        # Fast-forward until we find a field starting with 'to:'
        for val in field_iter:
            if val.startswith('to:'):
                break
            field_iter.store_field(val)
        else:
            return None
        kwargs = {}
        try:
            values = val.split(':')
            if len(values) == 2:
                addr_spec = values[1]
                port_spec = None
            elif len(values) == 3:
                addr_spec = values[1]
                port_spec = values[2]
            else:
                raise IptablesParsingError(f'bad DNAT dest spec: {val}')
            if '-' in addr_spec:
                raise IptablesParsingError("IP address range not supported")
            if addr_spec:
                kwargs['addr'] = IPv4Address(addr_spec)
            if port_spec is not None:
                if '-' in port_spec:
                    port_str, last_port_str = port_spec.split('-', 1)
                    kwargs['port'] = int(port_str)
                    kwargs['last_port'] = int(last_port_str)
                elif port_spec:
                    kwargs['port'] = int(port_spec)
        except Exception as ex:
            raise IptablesParsingError(
                        f'bad {target_name} dest spec: {val}') from ex
        for val in field_iter:
            if val == 'random':
                kwargs['is_random'] = True
            elif val == 'persistent':
                kwargs['is_persistent'] = True
            else:
                raise IptablesParsingError(
                        f'unknown {target_name} argument: {val}')
        return kwargs
        # pylint: enable=undefined-loop-variable, too-many-branches


class SnatTarget(_NatTarget):
    """This class provides access to the ``SNAT`` target
    """
    def __init__(self, *, addr: Optional[IPv4Address] =None,
                    port: Optional[int] =None, last_port: Optional[int] =None,
                    is_random=False, is_persistent=False):
        """
        :param addr: an :class:`IPv4Address` object
        :param port: port number (integer)
        :param last_port: port number (integer) used when defining
            a port range
        :param is_random: if ``True``, use the **iptables(8)**
            ``--random`` option
        :param is_persistent: if ``True``, use the **iptables(8)**
            ``--persistent`` option
        """
        if addr is None and port is None:
            raise ValueError('addr/port both None')
        super().__init__(nat_target='SNAT', nat_option='--to-source',
                        addr=addr, port=port, last_port=last_port,
                        is_random=is_random, is_persistent=is_persistent)

    @classmethod
    def _parse(cls, field_iter) -> Target:
        """Parse the SNAT target options
        """
        kwargs = cls._parse_nat('SNAT', field_iter)
        if kwargs is None:
            return None
        return SnatTarget(**kwargs)


class DnatTarget(_NatTarget):
    """This class provides access to the ``DNAT`` target
    """
    def __init__(self, *, addr=None, port=None, last_port=None,
                        is_random=False, is_persistent=False):
        """
        :param addr: an :class:`IPv4Address` object
        :param port: port number (integer)
        :param last_port: port number (integer) used when defining
            a port range
        :param is_random: if ``True``, use the **iptables(8)**
            ``--random`` option
        :param is_persistent: if ``True``, use the **iptables(8)**
            ``--persistent`` option
        """
        if addr is None and port is None:
            raise ValueError('addr/port both None')
        super().__init__(nat_target='DNAT', nat_option='--to-destination',
                        addr=addr, port=port, last_port=last_port,
                        is_random=is_random, is_persistent=is_persistent)

    @classmethod
    def _parse(cls, field_iter) -> Target:
        """Parse the DNAT target options
        """
        kwargs = cls._parse_nat('DNAT', field_iter)
        if kwargs is None:
            return None
        return DnatTarget(**kwargs)


class MasqueradeTarget(Target):
    """This class provides access to the ``MASQUERADE`` target
    """
    def __init__(self, *,
                port: Optional[int] =None, last_port: Optional[int] =None,
                is_random=False):
        """
        :param port: port number (integer)
        :param last_port: port number (integer) used when defining
            a port range
        :param is_random: if ``True``, use the **iptables(8)**
            ``--random`` option
        """
        super().__init__('MASQUERADE', terminates=True)
        self.__port = port
        self.__last_port = last_port
        self.__is_random = is_random

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        retval = super().to_iptables_args()
        if self.__port is not None:
            dest_spec = f':{self.__port:d}'
            if self.__last_port is not None:
                dest_spec += f'-{self.__last_port:d}'
            retval += ['--to-ports', dest_spec]
        if self.__is_random:
            retval.append('--random')
        return retval

    @classmethod
    def _parse(cls, field_iter) -> Target:
        """Parse the MASQUERADE target options
        """
        # If there are arguments to the target, they are after the field 'masq'
        for val in field_iter:
            if val == 'masq':
                break
            field_iter.store_field(val)
        else:
            return MasqueradeTarget()
        port = None
        last_port = None
        is_random = False
        for val in field_iter:
            try:
                if val == 'ports:':
                    port_spec = next(field_iter)
                    if '-' in port_spec:
                        port_str, last_port_str = port_spec.split('-', 1)
                        port = int(port_str)
                        last_port = int(last_port_str)
                    else:
                        port = int(port_spec)
                elif val == 'random':
                    is_random = True
                else:
                    raise IptablesParsingError(
                        f'unknown MASQUERADE argument: {val}')
            except Exception as ex:
                raise IptablesParsingError(f'bad value for {val}') from ex
        return MasqueradeTarget(port=port, last_port=last_port,
                                        is_random=is_random)


class ChainTarget(Target):
    """This class handles a target that is a chain
    """
    def __init__(self, *, chain=None,
                        real_chain_name: Optional[str] =None):
        """
        At least one of ``chain``, ``real_chain_name`` must be present.
        If both are present, the chain's real name must be equal to
        ``real_chain_name``.

        The target name is set to the real chain name.

        :param chain: a :class:`Chain` object
        :param real_chain_name: a string
        """
        if real_chain_name is not None:
            if chain is not None and chain.get_real_name() != real_chain_name:
                raise IptablesError(
                        f"chain name '{chain.get_real_name()}' does not match "
                        f"provided name '{real_chain_name}'")
            target_name = real_chain_name
        else:
            if chain is None:
                raise IptablesError(
                    'attempt to create ChainTarget without providing '
                    'chain object or chain name')
            target_name = chain.get_real_name()
        super().__init__(target_name, terminates=False)
        self.__chain = chain

    def get_chain(self) -> Optional['Chain']:
        """Returns the :class:`Chain` object
        """
        return self.__chain

    def resolve_chain(self, pft, log_failure=True) -> 'Chain':
        """Resolve the target name to the :class:`Chain` object, and return
        that object

        :param pft: the :class:`IptablesPacketFilterTable` object that is
            expected to contain the chain
        :param log_failure: if ``True`` and resolution fails, log a warning
        :rtype: a :class:`Chain` object or ``None``
        """
        if self.__chain is None:
            real_chain_name = self.get_target_name()
            self.__chain = pft.get_chain_by_rcn(real_chain_name)
            if self.__chain is None and log_failure:
                _logger.warning("%s: unable to resolve chain name %s",
                    self.resolve_chain.__qualname__, real_chain_name)
                _logger.warning("Call stack:\n%s",
                        ''.join(traceback.extract_stack().format()[:-1]))
        return self.__chain


class Targets:
    """This class provides a namespace for all target classes
    """

    #: Special ``ACCEPT`` target
    ACCEPT = Target('ACCEPT', terminates=True)

    #: Special ``DROP`` target
    DROP = Target('DROP', terminates=True)

    #: Special ``QUEUE`` target
    QUEUE = Target('QUEUE', terminates=True)

    #: Special ``RETURN`` target
    RETURN = Target('RETURN', terminates=True)

    LOG = LogTarget()
    CONNMARK = ConnmarkTarget()
    MARK = MarkTarget()
    REJECT = RejectTarget()

    __SPECIAL_TARGET_MAP = {
                        'ACCEPT' : ACCEPT,
                        'DROP' : DROP,
                        'QUEUE' : QUEUE,
                        'RETURN' : RETURN,
                    }

    @classmethod
    def get_special(cls, target_name: str) -> Optional[Target]:
        """Returns the :class:`Target` object for the special target
        identified by ``target_name``.

        The special targets are:

            - ``ACCEPT``
            - ``DROP``
            - ``RETURN``
            - ``QUEUE``
        """
        return cls.__SPECIAL_TARGET_MAP.get(target_name)

    @classmethod
    def from_policy(cls, policy: str) -> Target:
        """Return the :class:`Target` object for one the special targets
        that can be used as a policy target. These include:

            - ``ACCEPT``
            - ``DROP``
            - ``QUEUE``

        """
        if policy == 'ACCEPT':
            return cls.ACCEPT
        if policy == 'DROP':
            return cls.DROP
        if policy == 'QUEUE':
            return cls.QUEUE
        raise IptablesError(f"No target for policy '{policy}'")


# pylint: disable=protected-access
def parse_target(               # pylint: disable=too-many-return-statements
                target_name: Optional[str],
                field_iter, is_goto: bool) -> Optional[Target]:
    """Parses the specified target name and options.
    Returns a (subclass of) :class:`Target` or ``None`` if ``target_name``
    is not one of the built-in targets.
    """
    if target_name is None:
        field_iter.store_rest()
        return None
    if is_goto:
        field_iter.store_rest()
        return ChainTarget(real_chain_name=target_name)
    # As a heuristic, assume that if target_name is not all upper-case,
    # then it is a chain.
    if not target_name.isupper():
        field_iter.store_rest()
        return ChainTarget(real_chain_name=target_name)
    target = Targets.get_special(target_name)
    if target is not None:
        field_iter.store_rest()
        return target
    if target_name == 'LOG':
        return LogTarget._parse(field_iter)
    if target_name == 'CONNMARK':
        return ConnmarkTarget._parse(field_iter)
    if target_name == 'MARK':
        return MarkTarget._parse(field_iter)
    if target_name == 'REJECT':
        return RejectTarget._parse(field_iter)
    if target_name == 'SNAT':
        return SnatTarget._parse(field_iter)
    if target_name == 'DNAT':
        return DnatTarget._parse(field_iter)
    if target_name == 'MASQUERADE':
        return MasqueradeTarget._parse(field_iter)
    return UnparsedTarget(target_name, field_iter)
# pylint: enable=protected-access

# Copyright (c) 2021, Panagiotis Tsirigotis

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

"""This module offers two types of classes:
        - xxxCriterion
        - xxxMatch
An xxxMatch class allows packet matching using one or more match-specific
criteria. An xxxMatch class corresponds to an iptables(8) extension match
module (except for PacketMatch), with the options of that module mapping
to xxxCriterion classes, while the PacketMatch class offers matching
against the common criteria (source/dest address etc.)
"""

# pylint: disable=too-many-lines

from enum import IntFlag
from ipaddress import IPv4Network
from typing import Any, List, Optional, Set, Tuple

from .exceptions import IptablesError, IptablesParsingError
from .deps import get_logger

_logger = get_logger('linuxnet.iptables.match')

class Criterion:
    """
    This class is used to *express* an **iptables(8)** match criterion;
    it does not perform any comparisons.

    :class:`Criterion` is a superclass that serves the following purposes:
        1) it provides an :meth:`equals` method and a :meth:`not_equals`
           method to express comparison against a value
        2) it keeps track of whether the criterion has been set;
           a criterion is set when either the :meth:`equals` or
           :meth:`not_equals` method is invoked; **a criterion may only**
           **be set once**
        3) it keeps track of whether a criterion is negated or not
        4) its :meth:`iptables_to_args` method generates the '!'
           **iptables(8)** argument, and also checks if the criterion was set

    The :meth:`equals`/:meth:`not_equals` methods of :class:`Criterion`
    subclasses **must invoke** the :meth:`_set_polarity` method of
    :class:`Criterion` to indicate the polarity of the test.
    These methods are also responsible for saving the comparison value
    in the subclass object.

    A :class:`Criterion` has an owner which is an object of a subclass
    of :class:`Match`. The :meth:`equals`/:meth:`not_equals` methods return
    this object to facilitate building a criteria list:

    ::

        match.crit1().equals('foo').crit2().not_equals('bar')

    """
    def __init__(self, match: 'Match'):
        """
        :param match: the :class:`Match` object that owns this ``Criterion``
        """
        self.__match: 'Match' = match
        self.__positive = None

    def __eq__(self, other: 'Criterion'):
        """Compare this :class:`Criterion` with ``other``
        """
        if not self._may_be_equal(other):
            return False
        if not self.is_set():
            return True
        return self.get_value() == other.get_value()

    def __ne__(self, other: 'Criterion'):
        return not self.__eq__(other)

    def is_set(self) -> bool:
        """Returns ``True`` if the criterion has been set
        """
        return self.__positive is not None

    def is_positive(self) -> bool:
        """Returns the 'polarity' of the criterion; ``True`` for
        :meth:`equals` or ``False`` for :meth:`not_equals`

        Raises :class:`IptablesError` if the criterion is not set
        """
        if not self.is_set():
            raise IptablesError('criterion not set')
        return self.__positive

    def _may_be_equal(self, other: 'Criterion') -> bool:
        """Returns ``True`` iff:

             *  both criteria are set or both criteria are not set
             *  if both criteria are set, they have the same polarity
        """
        if self.is_set() ^ other.is_set():
            return False
        if self.is_set():
            # Both set, so compare boolean values
            return self.is_positive() == other.is_positive()
        # None set, so equal
        return True

    def get_value(self) -> Any:
        """Returns the value that this criterion is comparing against
        """
        raise NotImplementedError

    def _set_polarity(self, polarity: bool) -> 'Match':
        """Set the comparison polarity:

            - ``True`` : equality test
            - ``False`` : inequality test

        Raises an :class:`IptablesError` if the polarity is already set.

        Returns this object.
        """
        if self.__positive is not None:
            raise IptablesError(f"attempt to modify {self.__class__.__name__}")
        self.__positive = polarity
        return self.__match

    def equals(self, *args, **kwargs) -> 'Match':
        """Express equality comparison against the argument values.

        The method implementation in this class expects no arguments and
        expresses a bool comparison.

        Subclasses will implement this method to express comparisons
        against a specific value (or values). These values will be the
        arguments of the subclass method and will be stored in the
        subclass object.

        Subclasses overriding this method should invoke the
        :meth:`_set_polarity` method of this class to set the polarity
        to ``True``.

        Returns this object.
        """
        _ = (args, kwargs)
        return self._set_polarity(True)

    def not_equals(self, *args, **kwargs) -> 'Match':
        """Express inequality comparison against the argument values.

        The method implementation in this class invokes the :meth:`equals`
        method and then reverses the polarity; subclasses should not need
        to override it.

        Subclasses overriding this method should invoke the
        :meth:`_set_polarity` method of this class to set the polarity
        to ``False``.

        Returns this object.
        """
        _ = self.equals(*args, **kwargs)
        self.__positive = False
        return self.__match

    def compare(self, is_equal: bool, *args, **kwargs) -> 'Match':
        """Alternative method used for comparisons. It invokes
        :meth:`equals` (or :meth:`not_equals`) with ``args`` and ``kwargs``
        if ``is_equal`` is ``True`` (or ``False``).
        """
        if is_equal:            # pylint: disable=no-else-return
            return self.equals(*args, **kwargs)
        else:
            return self.not_equals(*args, **kwargs)

    def _crit_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments for the criterion,
        except for polarity
        """
        raise NotImplementedError

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        retval = [] if self.is_positive() else ['!']
        retval += self._crit_iptables_args()
        return retval


class Match:
    """Parent class for all match-specific subclasses.
    """

    @staticmethod
    def build_iptables_args(match_name: Optional[str],
                                crit_iterable) -> List[str]:
        """Helper method to build an **iptables(8)** argument list from
        a match name and a list of :class:`Criterion` objects.
        **iptables(8)** arguments will be extracted from each
        criterion that is set.

        :param match_name: optional match name that will result
            in adding '-m' ``match_name`` at the beginning of
            the argument list; there must be at least one set
            criterion for the match name to be included in the
            return value
        :param crit_iterable: a :class:`Criterion` iterator
        """
        args = []
        for crit in crit_iterable:
            if crit is not None and crit.is_set():
                args += crit.to_iptables_args()
        if not args:
            return args
        if not match_name:
            return args
        return ['-m', match_name] + args

    def has_criteria(self) -> bool:
        """Returns ``True`` if the match has any criteria set
        """
        return bool(self.to_iptables_args())

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments

        This method must be implemented by subclasses.
        """
        raise NotImplementedError

    def __eq__(self, other: 'Match'):
        """We rely on subclasses to define equality by value
        """
        return self is other

    def __ne__(self, other: 'Match'):
        return not self.__eq__(other)


class MatchNone(Match):
    """This is a special class to indicate the absence of any
    :class:`Match` objects.
    """

    def to_iptables_args(self) -> List[str]:
        """Returns a list of **iptables(8)** arguments
        """
        return []


class _GenericCriterion(Criterion):
    """A generic criterion that can be used by all criteria that
    correspond to **iptables(8)** options of the form "[!] option value",
    for example, "[!] -p tcp"
    """

    def __init__(self, match: Match, iptables_option: str):
        super().__init__(match)
        self.__value = None
        self.__option = iptables_option

    def get_value(self) -> Any:
        """Returns the criterion value
        """
        return self.__value

    def equals(self, value) -> Match:    # pylint: disable=arguments-differ
        """Compare with the specified value
        """
        self.__value = value
        return self._set_polarity(True)

    def _crit_iptables_args(self) -> List[str]:
        """Convert to **iptables(8)** arguments
        """
        return [self.__option, str(self.__value)]


#
#######################################################################
#
# Matching against standard packet attributes
#

class InputInterfaceCriterion(_GenericCriterion):
    """Compare with the input interface; used by :class:`PacketMatch`.

    The comparison value is a string.
    """
    def __init__(self, match: Match):
        super().__init__(match, '-i')

    def __eq__(self, other):
        return (isinstance(other, InputInterfaceCriterion) and
                                super().__eq__(other))


class OutputInterfaceCriterion(_GenericCriterion):
    """Compare with the output interface; used by :class:`PacketMatch`.

    The comparison value is a string.
    """
    def __init__(self, match: Match):
        super().__init__(match, '-o')

    def __eq__(self, other):
        return (isinstance(other, OutputInterfaceCriterion) and
                                                super().__eq__(other))


class SourceAddressCriterion(_GenericCriterion):
    """Compare with the source address; used by :class:`PacketMatch`.

    The comparison value is an :class:`IPv4Network`.
    """
    def __init__(self, match: Match):
        super().__init__(match, '-s')

    def __eq__(self, other):
        return (isinstance(other, SourceAddressCriterion)
                                                and super().__eq__(other))


class DestAddressCriterion(_GenericCriterion):
    """Compare with the destination address; used by :class:`PacketMatch`.

    The comparison value is an :class:`IPv4Network`.
    """
    def __init__(self, match: Match):
        super().__init__(match, '-d')

    def __eq__(self, other):
        return (isinstance(other, DestAddressCriterion) and
                                                super().__eq__(other))


class ProtocolCriterion(_GenericCriterion):
    """Compare with the protocol; used by :class:`PacketMatch`.

    The comparison value is a string.
    """
    def __init__(self, match: Match):
        super().__init__(match, '-p')

    def __eq__(self, other):
        return isinstance(other, ProtocolCriterion) and super().__eq__(other)


class FragmentCriterion(Criterion):
    """Check if a packet is a fragment. The parent :class:`Criterion`
    methods :meth:`equals`, :meth:`not_equals` can be used with no
    arguments to indicate matching when the fragment bit is set or is not set.
    This criterion is used by :class:`PacketMatch`.
    """

    def get_value(self) -> bool:
        """Returns the 'polarity' of the criterion
        """
        return self.is_positive()

    def __eq__(self, other):
        return (isinstance(other, FragmentCriterion) and
                                        self._may_be_equal(other))

    def _crit_iptables_args(self) -> List[str]:
        """Convert to **iptables(8)** arguments
        """
        return ['-f']


class PacketMatch(Match):
    """This class provides matching against the following attributes of
    a packet:

    * input interface
    * output interface
    * source address
    * destination address
    * fragment bit

    """

    def __init__(self):
        self.__iif_crit = None
        self.__oif_crit = None
        self.__proto_crit = None
        self.__frag_crit = None
        self.__source_crit = None
        self.__dest_crit = None

    def __eq__(self, other):
        return (
                isinstance(other, PacketMatch) and
                self.input_interface() == other.input_interface() and
                self.output_interface() == other.output_interface() and
                self.protocol() == other.protocol() and
                self.fragment() == other.fragment() and
                self.source_address() == other.source_address() and
                self.dest_address() == other.dest_address()
                )

    def protocol(self) -> ProtocolCriterion:
        """Match against the protocol
        """
        if self.__proto_crit is None:
            self.__proto_crit = ProtocolCriterion(self)
        return self.__proto_crit

    def input_interface(self) -> InputInterfaceCriterion:
        """Match against the input interface
        """
        if self.__iif_crit is None:
            self.__iif_crit = InputInterfaceCriterion(self)
        return self.__iif_crit

    def output_interface(self) -> OutputInterfaceCriterion:
        """Match against the output interface
        """
        if self.__oif_crit is None:
            self.__oif_crit = OutputInterfaceCriterion(self)
        return self.__oif_crit

    def source_address(self) -> SourceAddressCriterion:
        """Match against the source address
        """
        if self.__source_crit is None:
            self.__source_crit = SourceAddressCriterion(self)
        return self.__source_crit

    def dest_address(self) -> DestAddressCriterion:
        """Match against the destination address
        """
        if self.__dest_crit is None:
            self.__dest_crit = DestAddressCriterion(self)
        return self.__dest_crit

    def fragment(self) -> FragmentCriterion:
        """Match if packet has (or has not) the fragment bit set
        """
        if self.__frag_crit is None:
            self.__frag_crit = FragmentCriterion(self)
        return self.__frag_crit

    def to_iptables_args(self) -> List[str]:
        """Generate an **iptables(8)** arguments list for the set criteria
        """
        criteria = (
                            self.__iif_crit,
                            self.__oif_crit,
                            self.__proto_crit,
                            self.__frag_crit,
                            self.__source_crit,
                            self.__dest_crit,
                        )
        return self.build_iptables_args(None, criteria)

    @classmethod
    def _parse(cls, field_iter) -> Optional['PacketMatch']:
        """Parse the following fields, which will be returned in-order
        from field_iter:
            protocol, options, input-interface, output-interface,
            source, destination
        Returns a PacketMatch object if any criteria for the above
        fields are defined, otherwise None.

        :param field_iter: an iterator that returns the fields of an
            **iptables(8)** output line starting with the protocol field
        """
        packet_match = PacketMatch()
        proto = next(field_iter)
        if proto != 'all':
            is_equal, proto = _parse_value(proto)
            packet_match.protocol().compare(is_equal, proto)
        opt = next(field_iter)
        if opt == '--':
            pass
        elif opt == '-f':
            packet_match.fragment().equals()
        elif opt == '!f':
            packet_match.fragment().not_equals()
        else:
            raise IptablesParsingError(f'cannot parse option: {opt}')
        iif = next(field_iter)
        if iif != '*':
            is_equal, interface_name = _parse_value(iif)
            packet_match.input_interface().compare(is_equal, interface_name)
        oif = next(field_iter)
        if oif != '*':
            is_equal, interface_name = _parse_value(oif)
            packet_match.output_interface().compare(is_equal, interface_name)
        source = next(field_iter)
        if source != '0.0.0.0/0':
            is_equal, srcaddr = _parse_value(source, IPv4Network)
            packet_match.source_address().compare(is_equal, srcaddr)
        dest = next(field_iter)
        if dest != '0.0.0.0/0':
            is_equal, destaddr = _parse_value(dest, IPv4Network)
            packet_match.dest_address().compare(is_equal, destaddr)
        return packet_match if packet_match.has_criteria() else None


#
#######################################################################
#
# Matching against packet marks (either fwmark or ctmark)
#

class MarkCriterion(Criterion):
    """A criterion for a mark, used by :class:`MarkMatch` and
    :class:`ConnmarkMatch`
    since the **iptables(8)** option used by the mark/connmark modules is
    the same.

    The comparison value is a tuple consisting of an (integer) mark value
    and an integer mask value (``None`` in case of no mask).
    """
    def __init__(self, match: Match):
        super().__init__(match)
        self.__mark = None
        self.__mask = None

    def __eq__(self, other):
        return isinstance(other, MarkCriterion) and super().__eq__(other)

    def get_value(self):
        """Returns the value that the criterion is comparing against.

        :rtype: tuple of (int, int|None)
        """
        return (self.__mark, self.__mask)

    def equals(self,            # pylint: disable=arguments-differ
                    mark: int, mask: Optional[int] =None) -> Match:
        """Check for equality against ``mark`` and optionally ``mask``

        :param mark: the mark value
        :param mask: the mask value
        """
        self.__mark = mark
        self.__mask = mask
        return self._set_polarity(True)

    def __mark2str(self):
        """Convert the mark/mask to a string
        """
        markstr = f'{self.__mark:#x}'
        if self.__mask is not None:
            markstr += f'/{self.__mask:#x}'
        return markstr

    def _crit_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for the specified mark
        """
        return ['--mark', self.__mark2str()]


class MarkMatch(Match):
    """Match against the fwmark
    """
    def __init__(self):
        self.__mark_crit = None

    def __eq__(self, other):
        return isinstance(other, MarkMatch) and self.mark() == other.mark()

    def mark(self) -> MarkCriterion:
        """Match against the packet's fwmark.
        """
        if self.__mark_crit is None:
            self.__mark_crit = MarkCriterion(self)
        return self.__mark_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        return self.build_iptables_args('mark', [self.__mark_crit])

    @classmethod
    def _parse(                          # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Parse the mark criteria
        """
        val = next(criteria_iter)
        if val != 'match':
            raise IptablesParsingError("missing 'match' keyword")
        is_equal, val = _parse_next_value(criteria_iter,
                                        xform=lambda x: int(x, 16))
        return MarkMatch().mark().compare(is_equal, val)


class ConnmarkMatch(Match):
    """Match against the ctmark
    """
    def __init__(self):
        self.__mark_crit = None

    def __eq__(self, other):
        return isinstance(other, ConnmarkMatch) and self.mark() == other.mark()

    def mark(self) -> MarkCriterion:
        """Match against the packet's ctmark
        """
        if self.__mark_crit is None:
            self.__mark_crit = MarkCriterion(self)
        return self.__mark_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        return self.build_iptables_args('connmark', [self.__mark_crit])

    @classmethod
    def _parse(                          # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Parse the mark criteria
        """
        val = next(criteria_iter)
        if val != 'match':
            raise IptablesParsingError("missing 'match' keyword")
        is_equal, val = _parse_next_value(criteria_iter,
                                        xform=lambda x: int(x, 16))
        return ConnmarkMatch().mark().compare(is_equal, val)


#
#######################################################################
#
# Matching against connection tracking attributes
#

class CtStateCriterion(_GenericCriterion):
    """Compare against the connection tracking state

    The comparison value is a string.
    """
    def __init__(self, match):
        super().__init__(match, '--ctstate')

    def __eq__(self, other):
        return isinstance(other, CtStateCriterion) and super().__eq__(other)


class CtStatusCriterion(_GenericCriterion):
    """Compare against the connection tracking status

    The comparison value is a string.
    """
    def __init__(self, match):
        super().__init__(match, '--ctstatus')

    def __eq__(self, other):
        return isinstance(other, CtStatusCriterion) and super().__eq__(other)


class ConntrackMatch(Match):
    """Match against the connection tracking attributes.
    """
    def __init__(self):
        self.__ctstate_crit = None
        self.__ctstatus_crit = None

    def __eq__(self, other):
        return (isinstance(other, ConntrackMatch) and
                    self.ctstate() == other.ctstate() and
                    self.ctstatus() == other.ctstatus()
                    )

    def ctstate(self) -> CtStateCriterion:
        """Match against the connection tracking state
        """
        if self.__ctstate_crit is None:
            self.__ctstate_crit = CtStateCriterion(self)
        return self.__ctstate_crit

    def ctstatus(self) -> CtStatusCriterion:
        """Matching against the connection tracking status
        """
        if self.__ctstatus_crit is None:
            self.__ctstatus_crit = CtStatusCriterion(self)
        return self.__ctstatus_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        return self.build_iptables_args('conntrack',
                        [self.__ctstate_crit, self.__ctstatus_crit])

    @classmethod
    def _parse(cls, criteria_iter, match_name: str,
                        negation: Optional[str]) -> Match:
        """Match against ctstate, ctstatus
        """
        # Return the match_name and (optionally) negation to the iterator
        # so that we can process them as part of the for-loop below.
        # The for-loop is designed to handle all conntrack-related criteria
        # (which we expect to appear consecutively).
        criteria_iter.put_back(match_name)
        if negation is not None:
            criteria_iter.put_back(negation)
        match = ConntrackMatch()
        for criterion in criteria_iter:
            negation = None
            if criterion == '!':
                negation = match_name
                criterion = next(criteria_iter)
            if criterion == 'ctstate':
                is_equal, val = _parse_value(next(criteria_iter))
                if negation is not None:
                    is_equal = False
                match.ctstate().compare(is_equal, val)
            elif criterion == 'ctstatus':
                is_equal, val = _parse_value(next(criteria_iter))
                if negation is not None:
                    is_equal = False
                match.ctstatus().compare(is_equal, val)
            else:
                criteria_iter.put_back(criterion)
                if negation is not None:
                    criteria_iter.put_back(negation)
                break
        return match


#
#######################################################################
#
# Matching against connection tracking state
#

class StateCriterion(_GenericCriterion):
    """Compare with the connection tracking state

    The comparison value is a string.
    """
    def __init__(self, match):
        super().__init__(match, '--state')

    def __eq__(self, other):
        return isinstance(other, StateCriterion) and super().__eq__(other)


class StateMatch(Match):
    """Match against the connection tracking state
    This match is accessed via the state module, but it is not clear
    how its functionality is different from the conntrack module's
    --ctstate option.
    """
    def __init__(self):
        self.__state_crit = None

    def __eq__(self, other):
        return isinstance(other, StateMatch) and self.state() == other.state()

    def state(self) -> StateCriterion:
        """Match against the connection tracking state
        """
        if self.__state_crit is None:
            self.__state_crit = StateCriterion(self)
        return self.__state_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        return self.build_iptables_args('state', [self.__state_crit])

    @classmethod
    def _parse(                          # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Match against state
        """
        is_equal, val = _parse_value(next(criteria_iter))
        if negation is not None:
            is_equal = False
        return StateMatch().state().compare(is_equal, val)


#
#######################################################################
#
# Matching against protocol-related attributes, where protocol
# is TCP, UDP, ICMP
#

class MssCriterion(_GenericCriterion):
    """Compare with MSS field of the TCP header.

    The comparison value is a string in the form ``value``[:``value``]
    """
    def __init__(self, match):
        super().__init__(match, '--mss')

    def __eq__(self, other):
        return isinstance(other, MssCriterion) and super().__eq__(other)


class TcpmssMatch(Match):
    """Match against the MSS field of the TCP header
    """
    def __init__(self):
        self.__mss_crit = None

    def __eq__(self, other):
        return isinstance(other, TcpmssMatch) and self.mss() == other.mss()

    def mss(self) -> MssCriterion:
        """Match against the MSS field of the TCP header
        """
        if self.__mss_crit is None:
            self.__mss_crit = MssCriterion(self)
        return self.__mss_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        return self.build_iptables_args('tcpmss', [self.__mss_crit])

    @classmethod
    def _parse(                          # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Parse tcpmss.
        """
        # NB: although the expected value has the syntax <num>[:num>]
        #     we currently treat it as a string
        val = next(criteria_iter)
        if val != 'match':
            raise IptablesParsingError("missing 'match' keyword")
        is_equal, val = _parse_value(next(criteria_iter))
        return TcpmssMatch().mss().compare(is_equal, val)


class TcpFlag(IntFlag):
    """Names and values for the TCP flags.
    """
    FIN = 0x1
    SYN = 0x2
    RST = 0x4
    PSH = 0x8
    ACK = 0x10
    URG = 0x20


class TcpFlagsCriterion(Criterion):
    """A criterion for comparing against packets with an arbitrary set of
    TCP flags set.
    As a special case, it also serves for comparing against SYN packets.

    The value is the tuple (flags-checked, flags-set); both flags-checked
    and flags-set are comma-separated lists of TCP flag names.
    """
    def __init__(self, match: Match, syn_only=False):
        """
        :param match: the :class:`Match` object that owns this object
        :param syn_only: optional boolean value indicating a check only
            against the **SYN** flag
        """
        super().__init__(match)
        # If syn_only is True, then flags_checked/flags_set will be None
        self.__syn_only = syn_only
        self.__flags_checked = None
        self.__flags_set = None

    def __eq__(self, other):
        if not isinstance(other, TcpFlagsCriterion):
            return False
        if self.is_syn_only():
            return other.is_syn_only()
        if other.is_syn_only():
            return False
        return self.get_value() == other.get_value()

    def get_value(self) -> Any:
        """Returns the value that the criterion is comparing against
        """
        return (self.__flags_checked, self.__flags_set)

    def is_syn_only(self):
        """Returns ``True`` if the criterion is only meant to check
        for the SYN flag (but note that it may not be set yet)
        """
        return self.__syn_only

    def equals(self,            # pylint: disable=arguments-differ
                flags_checked: Optional[Set[TcpFlag]] =None,
                flags_set: Optional[List[TcpFlag]] =None) -> Match:
        """Perform flags comparison
        """
        if self.__syn_only:
            if not (flags_checked is None and flags_set is None):
                raise IptablesError("cannot set flags in SYN criterion")
            return self._set_polarity(True)
        if flags_checked is None:
            raise IptablesError("need to specify flags to check")
        if flags_set is None:
            raise IptablesError("need to specify flags that are set")
        self.__flags_checked = flags_checked
        self.__flags_set = flags_set
        return self._set_polarity(True)

    def _crit_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for the specified TCP flags
        """
        if self.__syn_only:
            return ['--syn']
        return ['--tcp-flags',
                ','.join([f.name for f in self.__flags_checked]),
                ','.join([f.name for f in self.__flags_set])]


class _PortCriterion(Criterion):
    """Compare against a source/destination port or port-range
    """
    def __init__(self, match: Match, iptables_option: str):
        super().__init__(match)
        self.__option = iptables_option
        self.__port = None
        self.__last_port = None

    def get_value(self) -> Any:
        """Returns the value that the criterion is comparing against
        """
        return (self.__port, self.__last_port)

    def equals(self,                    # pylint: disable=arguments-differ
                port: int, last_port: Optional[int] =None) -> Match:
        """Compare with a port (or inclusion in port-range if ``last_post``
        is present)
        """
        self.__port = port
        self.__last_port = last_port
        return self._set_polarity(True)

    def _crit_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for the specified port(s)
        """
        port_spec = str(self.__port)
        if self.__last_port is not None:
            port_spec += f':{self.__last_port}'
        return [self.__option, port_spec]


class SourcePortCriterion(_PortCriterion):
    """Compare with a source port or check for inclusion in port-range
    """
    def __init__(self, match: Match):
        super().__init__(match, '--sport')

    def __eq__(self, other):
        return isinstance(other, SourcePortCriterion) and super().__eq__(other)


class DestPortCriterion(_PortCriterion):
    """Compare against a destination port or check for inclusion in port-range
    """
    def __init__(self, match: Match):
        super().__init__(match, '--dport')

    def __eq__(self, other):
        return isinstance(other, DestPortCriterion) and super().__eq__(other)


class _PortParser:      # pylint: disable=too-few-public-methods
    """Helper class used to parse TCP/UDP port criteria
    """

    SOURCE_PORT_PREFIX = ('spt:', 'spts:')
    DEST_PORT_PREFIX = ('dpt:', 'dpts:')
    PORT_PREFIX = SOURCE_PORT_PREFIX + DEST_PORT_PREFIX

    @classmethod
    def parse(cls, port_match_str: str, match: Match):
        """Add the proper criterion to 'match'
        """
        if port_match_str.startswith(cls.SOURCE_PORT_PREFIX):
            port_crit = match.source_port()
        else:
            port_crit = match.dest_port()
        port_spec = port_match_str.split(':', 1)[1]
        is_equal, port_spec = _parse_value(port_spec)
        if ':' not in port_spec:
            port_crit.compare(is_equal, int(port_spec))
            return
        ports = port_spec.split(':', 1)
        port_crit.compare(is_equal, int(ports[0]), int(ports[1]))


class TcpMatch(Match):
    """Match against the fields of the TCP header
    """

    def __init__(self):
        self.__flags_crit = None
        self.__src_port_crit = None
        self.__dest_port_crit = None

    def __eq__(self, other):
        return (
                isinstance(other, TcpMatch) and
                self.tcp_flags() == other.tcp_flags() and
                self.source_port() == other.source_port() and
                self.dest_port() == other.dest_port()
                )

    def syn(self) -> TcpFlagsCriterion:
        """Criterion for matching against a SYN packet
        """
        if self.__flags_crit is None:
            self.__flags_crit = TcpFlagsCriterion(self, syn_only=True)
        return self.__flags_crit

    def tcp_flags(self) -> TcpFlagsCriterion:
        """Compare with TCP flags
        """
        if self.__flags_crit is None:
            self.__flags_crit = TcpFlagsCriterion(self)
        return self.__flags_crit

    def source_port(self) -> SourcePortCriterion:
        """Matching against the source port
        """
        if self.__src_port_crit is None:
            self.__src_port_crit = SourcePortCriterion(self)
        return self.__src_port_crit

    def dest_port(self) -> DestPortCriterion:
        """Match against the destination port
        """
        if self.__dest_port_crit is None:
            self.__dest_port_crit = DestPortCriterion(self)
        return self.__dest_port_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        criteria = (self.__flags_crit, self.__src_port_crit,
                                                self.__dest_port_crit)
        return self.build_iptables_args('tcp', criteria)

    @classmethod
    def __parse_tcp_flags_num(cls, numstr: int) -> Set[TcpFlag]:
        """Parse a hex-value numstr (e.g. 0x11) into a set of TCP flags.
        """
        try:
            flag_mask = int(numstr, 16)
            flags = {flag for flag in TcpFlag if flag_mask & flag}
            return flags
        except ValueError as valerr:
            raise IptablesParsingError(
                        "Bad TCP flag mask: " + numstr) from valerr

    @classmethod
    def _parse(                          # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Parse the TCP criteria
        """
        match = TcpMatch()
        for val in criteria_iter:
            if val.startswith('flags:'):
                flag_spec = val.split(':', 1)[1]
                is_equal, flag_spec = _parse_value(flag_spec)
                if '/' not in flag_spec:
                    raise IptablesParsingError(
                                f"no '/' in TCP flags: {flag_spec}")
                mask, comp = flag_spec.split('/', 1)
                flags_checked = cls.__parse_tcp_flags_num(mask)
                flags_set = cls.__parse_tcp_flags_num(comp)
                if (flags_set == {TcpFlag.SYN} and
                        flags_checked == {TcpFlag.FIN, TcpFlag.SYN,
                                                TcpFlag.RST, TcpFlag.ACK}):
                    match.syn().compare(is_equal)
                else:
                    match.tcp_flags().compare(is_equal,
                                                flags_checked, flags_set)
            elif val.startswith(_PortParser.PORT_PREFIX):
                _PortParser.parse(val, match)
            else:
                criteria_iter.put_back(val)
                break
        return match


class UdpMatch(Match):
    """Match against the fields of the UDP header
    """
    def __init__(self):
        self.__src_port_crit = None
        self.__dest_port_crit = None

    def __eq__(self, other):
        return (
                isinstance(other, UdpMatch) and
                self.source_port() == other.source_port() and
                self.dest_port() == other.dest_port()
                )

    def source_port(self) -> SourcePortCriterion:
        """Match against the source port
        """
        if self.__src_port_crit is None:
            self.__src_port_crit = SourcePortCriterion(self)
        return self.__src_port_crit

    def dest_port(self) -> DestPortCriterion:
        """Match against the destination port
        """
        if self.__dest_port_crit is None:
            self.__dest_port_crit = DestPortCriterion(self)
        return self.__dest_port_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        criteria = (self.__src_port_crit, self.__dest_port_crit)
        return self.build_iptables_args('udp', criteria)

    @classmethod
    def _parse(                          # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Parse the UDP criteria
        """
        match = UdpMatch()
        for val in criteria_iter:
            if val.startswith(_PortParser.PORT_PREFIX):
                _PortParser.parse(val, match)
            else:
                criteria_iter.put_back(val)
                break
        return match


class IcmpTypeCriterion(Criterion):
    """Compare with the ICMP type.

    The comparison value is the tuple
    (icmp-type-name, icmp-type-value, icmp-code); icmp-type-name
    is a string, icmp-type-value is an integer, and icmp-code is a string.
    """

    # Mapping of ICMP codes to iptables(8) --icmp-type parameter values
    __VAL2NAME_MAP = {
                    0 : 'echo-reply',
                    3 : 'destination-unreachable',
                    4 : 'source-quench',
                    5 : 'redirect',
                    8 : 'echo-request',
                    9 : 'router-advertisement',
                    10 : 'router-solicitation',
                    11 : 'time-exceeded',
                    12 : 'parameter-problem',
                    13 : 'timestamp-request',
                    14 : 'timestamp-reply',
                    17 : 'address-mask-request',
                    18 : 'address-mask-reply',
                }
    __NAME2VAL_MAP = {v : k for k, v in __VAL2NAME_MAP.items()}

    def __init__(self, match: Match):
        super().__init__(match)
        # If __icmp_type_name is not None, __icmp_type_value and __icmp_code
        # must be None.
        # If icmp_type_value is not None, __icmp_code may or may not be None
        self.__icmp_type_name = None
        self.__icmp_type_value = None
        self.__icmp_code = None

    def __eq__(self, other):
        return isinstance(other, IcmpTypeCriterion) and super().__eq__(other)

    def get_value(self) -> Any:
        """Returns the value that the criterion is comparing against
        """
        return (self.__icmp_type_name, self.__icmp_type_value, self.__icmp_code)

    def equals(self,                    # pylint: disable=arguments-differ)
                        icmp_type_name: Optional[str] =None,
                        icmp_type_value: Optional[int] =None,
                        icmp_code: Optional[str] =None) -> Match:
        """Check for equality against icmp_type_name, or
        icmp_type_value and icmp_code.
        Exactly one of icmp_type_name/icmp_type_value must be present;
        icmp_code is optional.
        """
        if icmp_type_name is not None:
            if icmp_type_value is not None:
                raise IptablesError(
                        'cannot specify both ICMP type name and value')
            if icmp_type_name not in self.__NAME2VAL_MAP:
                raise IptablesError(f'unknown ICMP type name: {icmp_type_name}')
            # If an icmp_code was specified, replace icmp_type_name with
            # icmp_type_value so that it can be expressed in --icmp-type syntax
            if icmp_code is not None:
                icmp_type_value = self.__NAME2VAL_MAP[icmp_type_name]
                icmp_type_name = None
        else:
            if icmp_type_value is None:
                raise IptablesError(
                        'must specify either ICMP type name or value')
            if icmp_code is None:
                icmp_type_name = self.__VAL2NAME_MAP.get(icmp_type_value)
                if icmp_type_name is not None:
                    icmp_type_value = None
        self.__icmp_type_name = icmp_type_name
        self.__icmp_type_value = icmp_type_value
        self.__icmp_code = icmp_code
        return self._set_polarity(True)

    def _crit_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for the specified mark
        """
        retval = ['--icmp-type']
        if self.__icmp_type_name is not None:
            retval.append(self.__icmp_type_name)
        elif self.__icmp_type_value is not None:
            val = f'{self.__icmp_type_value}'
            if self.__icmp_code is not None:
                val += f'/{self.__icmp_code}'
            retval.append(val)
        else:
            raise IptablesError('no ICMP type present')
        return retval


class IcmpMatch(Match):
    """Match against the fields of the ICMP header
    """
    def __init__(self):
        self.__icmp_type_crit = None

    def __eq__(self, other):
        return (isinstance(other, IcmpMatch) and
                        self.icmp_type() == other.icmp_type())

    def icmp_type(self) -> IcmpTypeCriterion:
        """Criterion for matching against the ICMP type
        """
        if self.__icmp_type_crit is None:
            self.__icmp_type_crit = IcmpTypeCriterion(self)
        return self.__icmp_type_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        return self.build_iptables_args('icmp', [self.__icmp_type_crit])

    @classmethod
    def _parse(                          # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Parse the ICMP criteria
        """
        # iptables 1.4.7 output:
        #       icmp type 3
        #       icmp !type 3
        # iptables 1.8.4 output:
        #       icmptype 3
        #       icmp !type 3
        if match_name == 'icmp':
            is_equal, val = _parse_value(next(criteria_iter))
            if val != 'type':
                raise IptablesParsingError(f"expecting 'type' instead of {val}")
        elif match_name == 'icmptype':
            is_equal = True
        else:
            raise IptablesParsingError(f"ICMP unable to parse '{match_name}'")
        match = IcmpMatch()
        val = int(next(criteria_iter))
        return match.icmp_type().compare(is_equal, icmp_type_value=val)

#
#######################################################################
#
# Rate limit
#

class RateLimitCriterion(Criterion):
    """Compare with a rate limit

    The comparison value is an integer
    """

    __INTERVAL_LIST = [
                        (86400, 'sec'),
                        (1440, 'min'),
                        (24, 'hour'),
                        (1, 'day'),
                    ]

    @classmethod
    def spec2rate(cls, spec: str) -> int:
        """Convert a rate spec which has the form <num>/<interval> into
        a rate number which is per-day
        """
        fields = spec.split('/')
        if len(fields) != 2:
            raise ValueError(f"bad rate spec '{spec}'")
        rate = int(fields[0])
        spec_interval = fields[1]
        for numsec, interval in cls.__INTERVAL_LIST:
            if spec_interval == interval:
                return rate * numsec
        raise ValueError(f"unknown interval '{spec_interval}'")

    @classmethod
    def rate2spec(cls, rate: int) -> str:
        """Convert a rate number which is per-second to the form
        <num>/<interval>
        """
        for numsec, interval in cls.__INTERVAL_LIST:
            if (rate % numsec) == 0:
                spec_rate = rate // numsec
                return f'{spec_rate:d}/{interval}'
        raise ValueError(f"bad rate value: {rate}")

    def __init__(self, match: Match):
        super().__init__(match)
        # The rate, when present, is always in events/day
        self.__rate = None

    def __eq__(self, other):
        return isinstance(other, RateLimitCriterion) and super().__eq__(other)

    def get_value(self) -> int:
        """Returns the value that the criterion is comparing against
        """
        return self.__rate

    def equals(self, rate: int) -> Match:    # pylint: disable=arguments-differ
        """Compare with the specified rate
        """
        if rate <= 0:
            raise IptablesError(f'invalid rate: {rate}')
        self.__rate = rate
        return self._set_polarity(True)

    def _crit_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for the specified rate
        """
        if not self.is_set():
            raise IptablesError('limit not set')
        return ['--limit', self.rate2spec(self.__rate)]


class BurstCriterion(_GenericCriterion):
    """Compare with the burst limit

    The comparison value is an integer
    """
    def __init__(self, match: Match):
        super().__init__(match, '--limit-burst')

    def __eq__(self, other):
        return isinstance(other, BurstCriterion) and super().__eq__(other)


class LimitMatch(Match):
    """Match against a rate limit with a maximum burst
    """
    def __init__(self):
        self.__rate_limit_crit = None
        self.__limit_burst_crit = None

    def __eq__(self, other):
        return (
                isinstance(other, LimitMatch) and
                self.limit() == other.limit() and
                self.burst() == other.burst()
                )

    def limit(self) -> RateLimitCriterion:
        """Compare with the rate limit
        """
        if self.__rate_limit_crit is None:
            self.__rate_limit_crit = RateLimitCriterion(self)
        return self.__rate_limit_crit

    def burst(self) -> BurstCriterion:
        """Compare with the burst limit
        """
        if self.__limit_burst_crit is None:
            self.__limit_burst_crit = BurstCriterion(self)
        return self.__limit_burst_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        criteria = (self.__rate_limit_crit, self.__limit_burst_crit)
        return self.build_iptables_args('limit', criteria)

    @classmethod
    def _parse(                  # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Parse limit
        """
        val = next(criteria_iter)
        if val != 'avg':
            _logger.error(
                "%s: parsing limit: expected 'avg'; found '%s'",
                    cls._parse.__qualname__, val)
            raise IptablesParsingError("missing 'avg' field")
        match = LimitMatch()
        val = next(criteria_iter)
        rate = RateLimitCriterion.spec2rate(val)
        # limit does not support '!'
        match.limit().equals(rate)
        val = next(criteria_iter)
        if val != 'burst':
            _logger.error(
                "%s: parsing limit: expected 'burst'; found '%s'",
                    cls._parse.__qualname__, val)
            raise IptablesParsingError("missing 'burst' field")
        burst = int(next(criteria_iter))
        return match.burst().equals(burst)

#
#######################################################################
#
# Packet type
#

class PacketTypeCriterion(_GenericCriterion):
    """Compare with the packet type

    The comparison value is a string.
    """
    def __init__(self, match: Match):
        super().__init__(match, '--pkt-type')

    def __eq__(self, other):
        return isinstance(other, PacketTypeCriterion) and super().__eq__(other)


class PacketTypeMatch(Match):
    """Match against the packet type
    """
    def __init__(self):
        self.__packet_type_crit = None

    def __eq__(self, other):
        return (isinstance(other, PacketTypeMatch) and
                self.packet_type() == other.packet_type())

    def packet_type(self) -> PacketTypeCriterion:
        """Compare with the packet type
        """
        if self.__packet_type_crit is None:
            self.__packet_type_crit = PacketTypeCriterion(self)
        return self.__packet_type_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        return self.build_iptables_args('pkttype', [self.__packet_type_crit])

    @classmethod
    def _parse(                  # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Parse PKTTYPE
        """
        val = next(criteria_iter)
        if val == '=':
            is_equal = True
        elif val == '!=':
            is_equal = False
        else:
            _logger.error(
                "%s: parsing PKTTYPE: expected comparator; found '%s'",
                    cls._parse.__qualname__, val)
            raise IptablesParsingError("missing comparator field")
        return PacketTypeMatch().packet_type().compare(is_equal,
                                                        next(criteria_iter))


#
#######################################################################
#
# Comment
#

class CommentCriterion(_GenericCriterion):
    """Not really a criterion.

    The comparison value is a string.
    """
    def __init__(self, match: Match):
        super().__init__(match, '--comment')

    def __eq__(self, other):
        return isinstance(other, CommentCriterion) and super().__eq__(other)


class CommentMatch(Match):
    """Provide a way to add a comment to a rule
    """
    def __init__(self):
        self.__comment_crit = None

    def __eq__(self, other):
        return (isinstance(other, CommentMatch) and
                self.comment() == other.comment())

    def comment(self) -> CommentCriterion:
        """The rule comment
        """
        if self.__comment_crit is None:
            self.__comment_crit = CommentCriterion(self)
        return self.__comment_crit

    def to_iptables_args(self) -> List[str]:
        """Returns **iptables(8)** arguments for this match
        """
        return self.build_iptables_args('comment', [self.__comment_crit])

    @classmethod
    def _parse(                  # pylint: disable=unused-argument
                cls, criteria_iter, match_name: str,
                negation: Optional[str]) -> Match:
        """Parse a comment
        """
        words = []
        for val in criteria_iter:
            if val == '*/':
                break
            words.append(val)
        return CommentMatch().comment().equals(' '.join(words))

#
#######################################################################
#
# Criteria parsing
#

# pylint: disable=protected-access
_parser_map = {
                'connmark'      : ConnmarkMatch._parse,
                'ctstate'       : ConntrackMatch._parse,
                'ctstatus'      : ConntrackMatch._parse,
                'icmp'          : IcmpMatch._parse,
                'icmptype'      : IcmpMatch._parse,
                'limit:'        : LimitMatch._parse,
                'PKTTYPE'       : PacketTypeMatch._parse,
                'mark'          : MarkMatch._parse,
                'state'         : StateMatch._parse,
                'tcp'           : TcpMatch._parse,
                'tcpmss'        : TcpmssMatch._parse,
                'udp'           : UdpMatch._parse,
                '/*'            : CommentMatch._parse
                }
# pylint: enable=protected-access


def _parse_value(value: str, xform=None) -> Tuple[bool, Any]:
    """Check if the specified value starts with '!' indicating negation.
    Returns the tuple (is_negative, value) where the optional '!'
    has been stripped from the argument 'value'; the 'value'
    may also be transformed by the xform callable; this allows
    returning a value of an arbitrary type.
    """
    is_equal = True
    if value[0] == '!':
        is_equal = False
        value = value[1:]
    if xform is not None:
        return is_equal, xform(value)
    return is_equal, value


def _parse_next_value(field_iter, xform=None) -> Tuple[bool, Any]:
    """Parse the next value from the iterator.
    Allow for the following syntax:
        ! value  (2 fields)
        !value (1 field)
    Returns the tuple (is_negative, value)
    the 'value' may also be transformed by the xform callable; this allows
    returning a value of an arbitrary type.
    """
    value = next(field_iter)
    if value == '!':
        is_equal = False
        value = next(field_iter)
    elif value[0] == '!':
        is_equal = False
        value = value[1:]
    else:
        is_equal = True
    if xform is not None:
        return is_equal, xform(value)
    return is_equal, value


def parse_criteria(field_iter) -> List[Match]:
    """Parse criteria and return a match list
    """
    match_list = []
    try:
        match_name = None
        for match_name in field_iter:
            #
            # For state/ctstate (maybe others), newer versions of iptables
            # (e.g. 1.8.4) display negation as:
            #   ! state NEW
            # where older versions (e.g. 1.4.7) would show all states
            # except NEW
            #
            negation = None
            if match_name == '!':
                negation = match_name
                match_name = next(field_iter)
            #
            # This code parses only a subset of possible criteria
            # It needs to be expanded.
            #
            parser = _parser_map.get(match_name)
            if parser is not None:
                match = parser(field_iter, match_name, negation)
            else:
                # We don't know if it is a match criterion that we don't
                # know about, a target name, or a target option.
                # Let the caller figure it out.
                field_iter.put_back(match_name)
                if negation is not None:
                    field_iter.put_back(negation)
                break
            match_list.append(match)
            match_name = None
    except StopIteration as stopiter:
        if match_name is not None:
            raise IptablesParsingError(
                'insufficient number of values for '
                f'match {match_name}') from stopiter
    return match_list

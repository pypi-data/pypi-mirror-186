# Copyright (c) 2022, Panagiotis Tsirigotis

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

"""Unit-test code for linuxnet.iptables
"""

import logging
import os
import subprocess
import unittest
import sys

from ipaddress import IPv4Network, IPv4Address

curdir = os.getcwd()
if os.path.basename(curdir) == 'tests':
    sys.path.insert(0, '..')
    TESTDIR = '.'
else:
    sys.path.insert(0, '.')
    TESTDIR = 'tests'

from linuxnet.iptables import IptablesPacketFilterTable
from linuxnet.iptables import IptablesError
from linuxnet.iptables import ChainRule, ChainTarget, Targets
from linuxnet.iptables import CommentMatch
from linuxnet.iptables import TcpmssMatch, TcpMatch
from linuxnet.iptables import UdpMatch, IcmpMatch
from linuxnet.iptables import PacketTypeMatch
from linuxnet.iptables import ConnmarkMatch

root_logger = logging.getLogger()
root_logger.addHandler(logging.FileHandler('test.log', 'w'))
root_logger.setLevel(logging.INFO)


class SimulatedIptablesRun:     # pylint: disable=too-few-public-methods
    """Simulate a run of iptables
    """
    def __init__(self, exitcode, output):
        self.__output = output
        self.__exitcode = exitcode

    def __call__(self, *args, **kwargs):
        proc = subprocess.CompletedProcess(args, self.__exitcode)
        proc.stdout = self.__output
        return proc


class TestParsing(unittest.TestCase):
    """Test parsing of iptables output.

    This class contains generic tests; match-specific
    or target-specific tests have their own class below.
    """

    EMPTY_FORWARD = """\
Chain FORWARD (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_OUTPUT = """\
Chain OUTPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_PREROUTING = """\
Chain PREROUTING (policy ACCEPT 429581 packets, 46536920 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_POSTROUTING = """\
Chain POSTROUTING (policy ACCEPT 26246841 packets, 13324987010 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_INPUT = """\
Chain INPUT (policy ACCEPT 28770515 packets, 54867569862 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""

    def test_parsing_goto(self):
        """Parse output with goto
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
   51546 10772289 ingress_eth0  all  --  eth0   *       0.0.0.0/0            0.0.0.0/0           [goto]
  541002 34654910 ingress_lo  all  --  lo     *       0.0.0.0/0            0.0.0.0/0           [goto]

Chain ingress_lo (1 references)
    pkts      bytes target     prot opt in     out     source               destination
  541002 34654910 RETURN     all  --  *      *       127.0.0.0/8          0.0.0.0/0
       0        0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain ingress_eth0 (1 references)
    pkts      bytes target     prot opt in     out     source               destination
   51517 10762427 RETURN     all  --  *      *       172.30.1.0/24        0.0.0.0/0
       0        0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        for rule in input_chain.get_rules():
            self.assertNotEqual(rule.get_target_chain(), None)
            self.assertTrue(rule.uses_goto())

    def test_parsing_refcounts(self):
        """Parse output with chain refcounts
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
196245663 314408786102 bad_traffic  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain bad_traffic (2 references)
    pkts      bytes target     prot opt in     out     source               destination
       8      524 DROP         tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           tcpmss match 1:500

Chain FORWARD (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
173219064 146017114276 bad_traffic  all  --  *      *       0.0.0.0/0            0.0.0.0/0
""" + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_chain('bad_traffic')
        self.assertEqual(input_chain.get_reference_count(), 2)

    def test_parsing_missing_chain(self):
        """Parse output with missing chain
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
196245663 314408786102 prod_INPUT  all  --  *      *       0.0.0.0/0            0.0.0.0/0
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        init_ok = pft.init_from_output(output, log_parsing_failures=False)
        self.assertFalse(init_ok, 'failed bad output')


class TestMatchParsing(unittest.TestCase):
    """Test parsing of matches in iptables output
    """

    EMPTY_FORWARD = """\
Chain FORWARD (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_OUTPUT = """\
Chain OUTPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_PREROUTING = """\
Chain PREROUTING (policy ACCEPT 429581 packets, 46536920 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_POSTROUTING = """\
Chain POSTROUTING (policy ACCEPT 26246841 packets, 13324987010 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_INPUT = """\
Chain INPUT (policy ACCEPT 28770515 packets, 54867569862 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""

    def test_parsing_packet_match(self):
        """Parse output with packet match (protocol, fragment,
        source addr, dest addr).
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
       0        0 DROP         all  -f  *      *       127.0.0.0/8          0.0.0.0/0
      29     9862 ACCEPT     udp  --  *      *       0.0.0.0/0            10.10.0.0/16
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        rules = input_chain.get_rules()
        self.assertEqual(len(rules), 2)
        match_list = rules[0].get_match_list()
        self.assertEqual(len(match_list), 1)
        match = match_list[0]
        self.assertTrue(match.fragment().is_positive())
        src = match.source_address()
        self.assertTrue(src.is_positive() and
                src.get_value() == IPv4Network('127.0.0.0/8'))
        match_list = rules[1].get_match_list()
        match = match_list[0]
        prot = match.protocol()
        self.assertTrue(prot.is_positive() and
                prot.get_value() == 'udp')
        dest = match.dest_address()
        self.assertTrue(dest.is_positive() and
                dest.get_value() == IPv4Network('10.10.0.0/16'))

    def test_parsing_packet_type_match(self):
        """Parse output with packet type match
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
      29     9862 DROP       all  --  *      *       0.0.0.0              0.0.0.0/0           PKTTYPE = broadcast
      29     9862 ACCEPT     udp  --  *      *       0.0.0.0/0            10.10.0.0/16
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        rules = input_chain.get_rules()
        match_list = rules[0].get_match_list()
        self.assertEqual(len(match_list), 2)
        match = match_list[1]
        self.assertTrue(isinstance(match, PacketTypeMatch))
        ptype = match.packet_type()
        self.assertTrue(ptype.is_positive() and
                        ptype.get_value() == 'broadcast')

    def test_parsing_tcp_match(self):
        """Parse output with match related to TCP (port, flags, MSS)
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
       8      524 DROP  tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           tcpmss match 1:500
    2182   251300 DROP  tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           tcp flags:!0x17/0x02
      17      732 ACCEPT  tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           tcp dpt:22
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        rules = input_chain.get_rules()
        self.assertEqual(len(rules), 3)
        for rule in rules:
            rulenum = rule.get_rulenum()
            match_list = rule.get_match_list()
            # There is a PacketMatch matching prot
            self.assertEqual(len(match_list), 2)
            match = match_list[-1]
            if rulenum == 1:
                self.assertTrue(isinstance(match, TcpmssMatch))
                mss = match.mss()
                self.assertTrue(mss.is_positive() and
                                        mss.get_value() == '1:500')
            elif rulenum == 2:
                self.assertTrue(isinstance(match, TcpMatch))
                flags = match.tcp_flags()
                self.assertTrue(flags.is_syn_only() and
                                        not flags.is_positive())
            elif rulenum == 3:
                self.assertTrue(isinstance(match, TcpMatch))
                dport = match.dest_port()
                self.assertTrue(dport.is_positive() and
                        dport.get_value()[0] == 22)

    def test_parsing_udp_match(self):
        """Parse output with match related to UDP
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
      17      732 ACCEPT  tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           udp dpt:53
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        rules = input_chain.get_rules()
        self.assertEqual(len(rules), 1)
        rule = rules[0]
        match_list = rule.get_match_list()
        # There is a PacketMatch matching prot
        self.assertEqual(len(match_list), 2)
        match = match_list[-1]
        self.assertTrue(isinstance(match, UdpMatch))
        dport = match.dest_port()
        self.assertTrue(dport.is_positive() and
                        dport.get_value()[0] == 53)

    def test_parsing_icmp_match(self):
        """Parse output with match related to ICMP
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
  143588 11622518 DROP         icmp --  *      *       0.0.0.0/0            0.0.0.0/0           icmp type 8
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        rules = input_chain.get_rules()
        self.assertEqual(len(rules), 1)
        rule = rules[0]
        match_list = rule.get_match_list()
        # There is a PacketMatch matching prot
        self.assertEqual(len(match_list), 2)
        match = match_list[-1]
        self.assertTrue(isinstance(match, IcmpMatch))
        icmp_type = match.icmp_type()
        self.assertTrue(icmp_type.is_positive() and
                        icmp_type.get_value()[0] == 'echo-request')

    def test_parsing_connmark_match(self):
        """Parse output with connmark match
        """
        output = ("""\
Chain PREROUTING (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
  558864 28503489 CONNMARK   all  --  *      *       0.0.0.0/0            0.0.0.0/0           connmark match 0x0 CONNMARK set 0x11 
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT + '\n' +
                self.EMPTY_INPUT + '\n' + self.EMPTY_POSTROUTING)
        pft = IptablesPacketFilterTable('mangle')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('PREROUTING')
        rules = input_chain.get_rules()
        self.assertEqual(len(rules), 1)
        rule = rules[0]
        match_list = rule.get_match_list()
        self.assertEqual(len(match_list), 1)
        match = match_list[-1]
        self.assertTrue(isinstance(match, ConnmarkMatch))
        cmark = match.mark()
        self.assertTrue(cmark.is_positive() and cmark.get_value() == (0, None))

    def test_parsing_limit_match(self):
        """Parse output with limit match
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
  487148 21609270 LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0           limit: avg 15/min burst 5 LOG flags 0 level 6 prefix `DROP-INPUT: '
  520139 23069461 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        rule = input_chain.get_rules()[0]
        match_list = rule.get_match_list()
        self.assertEqual(len(match_list), 1)
        match = match_list[0]
        limit = match.limit()
        self.assertTrue(limit.is_positive() and
                limit.get_value() == 21600)       # 21600/day
        burst = match.burst()
        self.assertTrue(burst.is_positive() and
                burst.get_value() == 5)

    def test_parsing_comment_match(self):
        """Parse output with comment matches
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
       0        0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0           /* my comment */ 
       0        0 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0           /* another comment */ state NEW reject-with icmp-port-unreachable 
       0        0 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0           /* another comment */ state NEW /* foo bar */ reject-with icmp-port-unreachable 
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        for rule in input_chain.get_rules():
            rulenum = rule.get_rulenum()
            if rulenum == 1:
                for match in rule.get_match_list():
                    if isinstance(match, CommentMatch):
                        comment = match.comment().get_value()
                        self.assertEqual(comment, 'my comment')
                        break
            elif rulenum == 2:
                for match in rule.get_match_list():
                    if isinstance(match, CommentMatch):
                        comment = match.comment().get_value()
                        self.assertEqual(comment, 'another comment')
                        break
            elif rulenum == 3:
                cit = iter(['another comment', 'foo bar'])
                for match in rule.get_match_list():
                    if isinstance(match, CommentMatch):
                        comment = match.comment().get_value()
                        self.assertEqual(comment, next(cit))

    def test_parsing_unknown_match(self):
        """Parse output with unknown match
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
196245663 314408786102 prod_INPUT  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain prod_INPUT (1 references)
    pkts      bytes target     prot opt in     out     source               destination         
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0           DSCP match 0x10
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        init_ok = pft.init_from_output(output, log_parsing_failures=False)
        self.assertFalse(init_ok, 'failed bad output')



class TestTargetParsing(unittest.TestCase):
    """Test parsing of targets in iptables output
    """

    EMPTY_FORWARD = """\
Chain FORWARD (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_OUTPUT = """\
Chain OUTPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_PREROUTING = """\
Chain PREROUTING (policy ACCEPT 429581 packets, 46536920 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_POSTROUTING = """\
Chain POSTROUTING (policy ACCEPT 26246841 packets, 13324987010 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""
    EMPTY_INPUT = """\
Chain INPUT (policy ACCEPT 28770515 packets, 54867569862 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
"""

    def test_parsing_log_target(self):
        """Parse output with LOG target
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
  487148 21609270 LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0           limit: avg 15/min burst 5 LOG flags 0 level 6 prefix `DROP-INPUT: '
  520139 23069461 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        rule = input_chain.get_rules()[0]
        target = rule.get_target()
        self.assertEqual(target.get_log_prefix(), 'DROP-INPUT: ')
        self.assertEqual(target.get_log_level(), '6')
        self.assertEqual(target.get_log_options(), [])

    def test_parsing_reject_target(self):
        """Parse output with REJECT target
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
     144    57620 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0           reject-with icmp-host-unreachable
  520139 23069461 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        self.assertTrue(pft.init_from_output(output))
        input_chain = pft.get_builtin_chain('INPUT')
        rule = input_chain.get_rules()[0]
        target = rule.get_target()
        self.assertEqual(target, Targets.REJECT)
        self.assertEqual(target.get_rejection_message(),
                                'icmp-host-unreachable')

    def test_parsing_connmark_target(self):
        """Parse output with CONNMARK target
        """
        output = ("""\
Chain PREROUTING (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
  558864 28503489 CONNMARK   all  --  *      *       0.0.0.0/0            0.0.0.0/0           connmark match 0x0 CONNMARK set 0x11 
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT + '\n' +
                self.EMPTY_INPUT + '\n' + self.EMPTY_POSTROUTING)
        pft = IptablesPacketFilterTable('mangle')
        self.assertTrue(pft.init_from_output(output))
        prerouting_chain = pft.get_builtin_chain('PREROUTING')
        rule = prerouting_chain.get_rules()[0]
        target = rule.get_target()
        self.assertEqual(target, Targets.CONNMARK)
        self.assertEqual(target.get_mark(), 0x11)

    def test_parsing_snat_target(self):
        """Parse output with SNAT target
        """
        output = (self.EMPTY_PREROUTING + '\n' + """\
Chain POSTROUTING (1 references)
    pkts      bytes target     prot opt in     out     source               destination         
  466007 51946882 SNAT       all  --  *      eth1    0.0.0.0/0            0.0.0.0/0           to:10.10.10.18 
""" + '\n' + self.EMPTY_OUTPUT)
        pft = IptablesPacketFilterTable('nat')
        self.assertTrue(pft.init_from_output(output))
        postrouting_chain = pft.get_builtin_chain('POSTROUTING')
        rule = postrouting_chain.get_rules()[0]
        target = rule.get_target()
        self.assertEqual(target.get_target_name(), 'SNAT')
        self.assertEqual(target.get_address(), IPv4Address('10.10.10.18'))

    def test_parsing_unknown_target(self):
        """Parse output with unknown target
        """
        output = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
196245663 314408786102 prod_INPUT  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain prod_INPUT (1 references)
    pkts      bytes target     prot opt in     out     source               destination         
    0     0 AUDIT      all  --  *      *       1.2.3.4              0.0.0.0/0           AUDIT accept
""" + '\n' + self.EMPTY_FORWARD + '\n' + self.EMPTY_OUTPUT
        pft = IptablesPacketFilterTable('filter')
        init_ok = pft.init_from_output(output, log_parsing_failures=False)
        self.assertFalse(init_ok, 'failed bad output')



class TestPrefix(unittest.TestCase):
    """Test chain prefix handling
    """

    GOOD_OUTPUT = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
129651288 230406442471 prod_INPUT  all  --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain FORWARD (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
378613942 278529707859 prod_FORWARD  all  --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain OUTPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
62441650 9685307040 prod_OUTPUT  all  --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain prod_FORWARD (1 references)
    pkts      bytes target     prot opt in     out     source               destination         
377452936 278361749795 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain prod_INPUT (1 references)
    pkts      bytes target     prot opt in     out     source               destination         
128158511 230312235930 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain prod_OUTPUT (1 references)
    pkts      bytes target     prot opt in     out     source               destination         
55238105 5261597979 ACCEPT  all  --  *      eth1    0.0.0.0/0            0.0.0.0/0
"""

    def test_creating_table_using_prefix(self):
        """Parse valid output with no errors when a prefix is specified
        """
        prefix = 'prod_'
        pft = IptablesPacketFilterTable('filter', chain_prefix=prefix)
        init_ok = pft.init_from_output(self.GOOD_OUTPUT)
        self.assertTrue(init_ok)
        for chain in pft.get_user_chains():
            self.assertTrue(chain.get_real_name().startswith(prefix))

    def test_creating_table_using_nonexistent_prefix(self):
        """Create a table using non-existent prefix
        """
        pft = IptablesPacketFilterTable('filter', chain_prefix='foo_')
        init_ok = pft.init_from_output(self.GOOD_OUTPUT)
        self.assertTrue(init_ok)

    def test_prefix_setting(self):
        """Check that setting the prefix works
        """
        pft = IptablesPacketFilterTable('filter')
        init_ok = pft.init_from_output(self.GOOD_OUTPUT)
        self.assertTrue(init_ok)
        chain_map_copy = pft.get_chain_map().copy()
        prefix = 'prod_'
        pft.set_prefix('prod_')
        for chain in pft.get_user_chains():
            self.assertTrue(chain.get_real_name().startswith(prefix))
        pft.set_prefix(None)
        self.assertTrue(chain_map_copy == pft.get_chain_map())


class TestMiscellaneous(unittest.TestCase):
    """Test miscellaneous operations
    """

    GOOD_OUTPUT = """\
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
129651288 230406442471 prod_INPUT  all  --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain FORWARD (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
378613942 278529707859 prod_FORWARD  all  --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain OUTPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
62441650 9685307040 prod_OUTPUT  all  --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain prod_FORWARD (1 references)
    pkts      bytes target     prot opt in     out     source               destination         
377452936 278361749795 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain prod_INPUT (1 references)
    pkts      bytes target     prot opt in     out     source               destination         
128158511 230312235930 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain prod_OUTPUT (1 references)
    pkts      bytes target     prot opt in     out     source               destination         
55238105 5261597979 ACCEPT  all  --  *      eth1    0.0.0.0/0            0.0.0.0/0
"""

    def test_epoch(self):
        """Check that the epoch is initialized properly
        """
        pft = IptablesPacketFilterTable('filter')
        for i in range(1, 3):
            init_ok = pft.init_from_output(self.GOOD_OUTPUT)
            self.assertTrue(init_ok)
            self.assertEqual(pft.get_epoch(), i)


class TestChainOperations(unittest.TestCase):
    """Test chain operations. The runner is a no-op
    """

    @staticmethod
    def _runner(*args, **kwargs):
        """Runner that logs the arguments without invoking iptables(8)
        """
        root_logger.info("Executing: args=%s kwargs=%s", args, kwargs)
        proc = subprocess.CompletedProcess(args, 0)
        proc.stdout = ""
        return proc

    def test_chain_creation_deletion(self):
        """Create, then delete a chain.
        """
        try:
            pft = IptablesPacketFilterTable('filter', runner=self._runner)
            chain = pft.create_chain('test_chain')
            pft.delete_chain(chain)
            result = True
        except IptablesError:
            result = False
        self.assertTrue(result)

    def test_multi_chain_creation_deletion(self):
        """Create 3 chains, with 2 of them jump'ing to the 3rd.
        Then delete the chain that serves as the terget.
        Rules referencing that chain should be automatically removed.
        """
        try:
            pft = IptablesPacketFilterTable('filter', runner=self._runner)
            chain1 = pft.create_chain('test_chain_1')
            chain2 = pft.create_chain('test_chain_2')
            chain3 = pft.create_chain('test_chain_3')
            chain2.append_rule(ChainRule(target=ChainTarget(chain=chain1)))
            chain3.append_rule(ChainRule(target=ChainTarget(chain=chain1)))
            # The following should trigger the automatic deletion of
            # the rules referencing chain1
            pft.delete_chain(chain1)
            self.assertEqual(len(chain2.get_rules()), 0)
            self.assertEqual(len(chain3.get_rules()), 0)
            pft.delete_chain(chain2)
            pft.delete_chain(chain3)
            result = True
        except IptablesError:
            result = False
        self.assertTrue(result)

    def test_chain_rule_ownership(self):
        """Attempt to insert a rule into a chain twice.
        The 2nd attempt should fail as the rule already has an owner.
        """
        pft = IptablesPacketFilterTable('filter', runner=self._runner)
        chain = pft.create_chain('test_chain')
        rule = ChainRule(target=Targets.ACCEPT)
        chain.append_rule(rule)
        try:
            chain.append_rule(rule)
            inserted = True
        except IptablesError:
            inserted = False
        self.assertFalse(inserted)
        # Remove the rule, verify it now has no owner
        chain.flush()
        self.assertEqual(rule.get_chain(), None)
        try:
            chain.append_rule(rule)
            inserted = True
        except IptablesError:
            inserted = False
        self.assertTrue(inserted)
        # Delete it by rule number
        chain.delete_rulenum(rule.get_rulenum())
        self.assertEqual(rule.get_chain(), None)

    def test_chain_rule_numbering(self):
        """Verify rule numbering when rules are inserted/deleted.
        """
        pft = IptablesPacketFilterTable('filter', runner=self._runner)
        chain = pft.create_chain('test_chain')
        rule_list = []
        # Always inserting as rule #1 forces previously inserted
        # rules to be renumbered.
        for i in range(4):
            rule = ChainRule(target=Targets.ACCEPT)
            chain.insert_rule(rule, rulenum=1)
            rule_list.append(rule)
        for i in range(4):
            expected_num = 4-i
            self.assertEqual(rule_list[i].get_rulenum(), expected_num)


if __name__ == '__main__':
    unittest.main()

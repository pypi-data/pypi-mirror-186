..
    Copyright (c) 2022, Panagiotis Tsirigotis
    
    This file is part of linuxnet-iptables.
    
    linuxnet-iptables is free software: you can redistribute it and/or
    modify it under the terms of version 3 of the GNU Affero General Public
    License as published by the Free Software Foundation.
    
    linuxnet-iptables is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
    License for more details.
    
    You should have received a copy of the GNU Affero General
    Public License along with linuxnet-iptables. If not, see
    <https://www.gnu.org/licenses/>.

.. iptables_api:

.. module:: linuxnet.iptables

iptables interface
==================

The iptables interface provides programmatic access to the
**iptables** command. It is structured around the following classes:

* :class:`IptablesPacketFilterTable`
* :class:`Chain`
* :class:`ChainRule`
* :class:`Match`
* :class:`Target`

An :class:`IptablesPacketFilterTable` contains :class:`Chain` objects
representing the chains of the corresponding table.

A :class:`Chain` object contains :class:`ChainRule` objects
representing the rules of the corresponding chain.

A :class:`ChainRule` object consists of a list of :class:`Match` objects
and a :class:`Target` object.


Programming notes
-----------------

An :class:`IptablesPacketFilterTable` can be populated by reading
the current system configuration using the **iptables** command.
The :class:`Chain` objects it returns via its accessor methods
are *stable*: for a given chain name, the same :class:`Chain` object
will always be returned. This holds true until the next time
the :class:`IptablesPacketFilterTable`
is populated by reading the system configuration.

A :class:`Chain` object keeps track of the
:class:`IptablesPacketFilterTable` that it belongs to.
This association is reset when
the :class:`IptablesPacketFilterTable`
is repopulated.

A :class:`ChainRule` object provides methods to construct **iptables** rules.
The :class:`ChainRule` can then be inserted into a :class:`Chain`.
:class:`ChainRule` objects that are part of a :class:`Chain` are immutable.
They are also *stable*: the same objects will be returned by the
:class:`Chain` accessor methods.

:class:`ChainRule` objects that are part of a :class:`Chain` keep track
of their rule number. This number is updated as rules are inserted or
deleted from the :class:`Chain`.

The packet and byte count statistics that are part of every
:class:`Chain` and :class:`ChainRule` object are current as of the time of
reading the system configuration.

:class:`Target` objects can be compared to each other. Comparison is
by name; target arguments are not considered.


IptablesPacketFilterTable
-------------------------

.. autoclass:: IptablesPacketFilterTable
    :inherited-members:

Chain
-----

.. autoclass:: Chain
    :inherited-members:


ChainRule
---------

.. autoclass:: ChainRule
    :inherited-members:


Matches and criteria
--------------------

The programmatic interface to packet matching is based on the concept
of a :class:`Match` object that provides methods returning
:class:`Criterion` objects which in turn allow for equality (and
inequality) testing against a stored value.

In the following example, :class:`PacketMatch` (a subclass of
:class:`Match`) provides matching against packet attributes
such as protocol, source address, etc.

::

    m = PacketMatch()
    m.protocol().equals('udp')

The :meth:`protocol` method returns a
:class:`ProtocolCriterion` object which stores the value that
we want to compare against (``udp`` in this case).

A :class:`Match` object may have multiple criteria; such criteria
are specific to the :class:`Match` subclass.

Continuing the example::

    a = IPv4Network('1.2.3.4/32')
    mcast = IPV4Network('224.0.0.0/4')
    m.source_address().equals(a).dest_address().not_equals(mcast)

The :meth:`source_address` method returns a
:class:`SourceAddressCriterion` object, while 
the :meth:`dest_address` method returns a
:class:`DestAddressCriterion` object.
The resulting :class:`Match` object now matches UDP packets with
a source address of 1.2.3.4 and a destination address that is not
a multicast address.


Generic classes: :class:`Match`, :class:`Criterion`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: Match
    :members:

-------

.. autoclass:: Criterion
    :members:


:class:`PacketMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: PacketMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: InputInterfaceCriterion
    :class-doc-from: class

-------

.. autoclass:: OutputInterfaceCriterion
    :class-doc-from: class

-------

.. autoclass:: SourceAddressCriterion
    :class-doc-from: class

-------

.. autoclass:: DestAddressCriterion
    :class-doc-from: class

-------

.. autoclass:: FragmentCriterion
    :class-doc-from: class

:class:`MarkMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: MarkMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: MarkCriterion
    :class-doc-from: class


:class:`ConnmarkMatch`
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: ConnmarkMatch
    :members:
    :inherited-members: Match


:class:`ConntrackMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: ConntrackMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: CtStateCriterion
    :class-doc-from: class

-------

.. autoclass:: CtStatusCriterion
    :class-doc-from: class

:class:`StateMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: StateMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: StateCriterion
    :class-doc-from: class

:class:`TcpmssMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: TcpmssMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: MssCriterion
    :class-doc-from: class


:class:`TcpMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: TcpMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: TcpFlagsCriterion
    :class-doc-from: class

-------

.. autoclass:: SourcePortCriterion
    :class-doc-from: class

-------

.. autoclass:: DestPortCriterion
    :class-doc-from: class

:class:`UdpMatch`
~~~~~~~~~~~~~~~~~

.. autoclass:: UdpMatch
    :members:
    :inherited-members: Match

:class:`IcmpMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: IcmpMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: IcmpTypeCriterion
    :class-doc-from: class

:class:`LimitMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: LimitMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: RateLimitCriterion
    :class-doc-from: class

-------

.. autoclass:: BurstCriterion
    :class-doc-from: class

:class:`PacketTypeMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: PacketTypeMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: PacketTypeCriterion
    :class-doc-from: class

:class:`CommentMatch` and related criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: CommentMatch
    :members:
    :inherited-members: Match

-------

.. autoclass:: CommentCriterion
    :class-doc-from: class


:class:`MatchNone`
~~~~~~~~~~~~~~~~~~

.. autoclass:: MatchNone
    :members:
    :inherited-members: Match


Target
------

.. autoclass:: Target
    :inherited-members:

-------

.. autoclass:: LogTarget
    :members:
    :inherited-members: Target

-------

.. autoclass:: RejectTarget
    :members:
    :inherited-members: Target

-------

.. autoclass:: MarkTarget
    :members:
    :inherited-members: Target

-------

.. autoclass:: ConnmarkTarget
    :members:
    :inherited-members: Target

-------

.. autoclass:: SnatTarget
    :members:
    :inherited-members: Target

-------

.. autoclass:: DnatTarget
    :members:
    :inherited-members: Target

-------

.. autoclass:: ChainTarget
    :members:
    :inherited-members: Target

-------

.. autoclass:: Targets
    :members:
    :member-order: bysource


Exceptions
----------

.. autoexception:: IptablesError

.. autoexception:: IptablesParsingError

.. autoexception:: IptablesExecutionError


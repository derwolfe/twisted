# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Tests for L{twisted.internet.abstract}, a collection of APIs for implementing
reactors.
"""

from __future__ import division, absolute_import

from twisted.trial.unittest import SynchronousTestCase

from twisted.internet.abstract import isIPv6Address, isIPAddress



class IsIPAddressTests(SynchronousTestCase):
    """
    Tests for L{isIPAddress}, a function for determining if a particular
    string (or bytes) is an IPv4 address literal.
    """
    def test_empty(self):
        """
        The empty literal is not an IPv4 address.
        """
        self.assertFalse(isIPAddress(u""))
        self.assertFalse(isIPAddress(b""))


    def test_nonAscii(self):
        """
        If an IP address literal contains non-ASCII unicode code points or
        bytes contain values outside of the ASCII range, no error should be
        raised and the function should return C{False}.
        """
        umlaut = u"\u00FC" # non-ASCII code point
        try:
            result = isIPAddress(umlaut + u".0.0.0")
        except:
            self.fail("isIPAddress shouldn't raise if addr contains non-ASCII"
                " code points")
        self.assertFalse(result)

        nonAscii = b'\x80' # 0x80 == 128
        try:
            result = isIPAddress(nonAscii + b".0.0.0")
        except:
            self.fail("isIPAddress shouldn't raise if addr contains values "
                "outside of the ASCII range")
        self.assertFalse(result)


    def test_fourParts(self):
        """
        An IPv4 address literal consists of four parts, separated by dots.
        """
        self.assertTrue(isIPAddress(u"1.2.3.4"))
        self.assertFalse(isIPAddress(u"1"))
        self.assertFalse(isIPAddress(u"1.2.3.4.5"))

        self.assertTrue(isIPAddress(b"1.2.3.4"))
        self.assertFalse(isIPAddress(b"1"))
        self.assertFalse(isIPAddress(b"1.2.3.4.5"))


    def test_decimalNotation(self):
        """
        Each part of an IPv4 address literal consists of a decimal number.
        """
        self.assertTrue(isIPAddress(u"0.0.0.0"))
        self.assertFalse(isIPAddress(u"a.b.c.d"))
        self.assertTrue(isIPAddress(b"0.0.0.0"))
        self.assertFalse(isIPAddress(b"a.b.c.d"))


    def test_eachPartIsEightBitValue(self):
        """
        In dot-decimal notation, the value of each part is permitted to be in
        range from 0 to 255.
        """
        self.assertFalse(isIPAddress(u"0.300.0.0"))
        self.assertTrue(isIPAddress(u"0.0.0.0"))
        self.assertTrue(isIPAddress(u"255.255.255.255"))
        self.assertFalse(isIPAddress(b"0.300.0.0"))
        self.assertTrue(isIPAddress(b"0.0.0.0"))
        self.assertTrue(isIPAddress(b"255.255.255.255"))



class IPv6AddressTests(SynchronousTestCase):
    """
    Tests for L{isIPv6Address}, a function for determining if a particular
    string (or bytes) is an IPv6 address literal.
    """
    def test_empty(self):
        """
        The empty string is not an IPv6 address literal.
        """
        self.assertFalse(isIPv6Address(u""))
        self.assertFalse(isIPv6Address(b""))


    def test_colon(self):
        """
        A single C{":"} is not an IPv6 address literal.
        """
        self.assertFalse(isIPv6Address(u":"))
        self.assertFalse(isIPv6Address(b":"))


    def test_loopback(self):
        """
        C{"::1"} is the IPv6 loopback address literal.
        """
        self.assertTrue(isIPv6Address(u"::1"))
        self.assertTrue(isIPv6Address(b"::1"))


    def test_scopeID(self):
        """
        An otherwise valid IPv6 address literal may also include a C{"%"}
        followed by an arbitrary scope identifier.
        """
        self.assertTrue(isIPv6Address(u"fe80::1%eth0"))
        self.assertTrue(isIPv6Address(u"fe80::2%1"))
        self.assertTrue(isIPv6Address(u"fe80::3%en2"))
        self.assertTrue(isIPv6Address(b"fe80::1%eth0"))
        self.assertTrue(isIPv6Address(b"fe80::2%1"))
        self.assertTrue(isIPv6Address(b"fe80::3%en2"))


    def test_invalidWithScopeID(self):
        """
        An otherwise invalid IPv6 address literal is still invalid with a
        trailing scope identifier.
        """
        self.assertFalse(isIPv6Address(u"%eth0"))
        self.assertFalse(isIPv6Address(u":%eth0"))
        self.assertFalse(isIPv6Address(u"hello%eth0"))
        self.assertFalse(isIPv6Address(b"%eth0"))
        self.assertFalse(isIPv6Address(b":%eth0"))
        self.assertFalse(isIPv6Address(b"hello%eth0"))


    def test_nonAscii(self):
        """
        If an IPv6 address literal contains non-ASCII unicode code points or
        bytes contain values outside of the ASCII range, no error should be
        raised and the function should return C{False}.
        """
        umlaut = u"\u00FC" # non-ASCII code point
        try:
            result = isIPv6Address(umlaut + u"e80::1")
        except:
            self.fail("isIPv6Address shouldn't raise if addr contains non-ASCII"
                " code points")
        self.assertFalse(result)

        nonAscii = b'\x80' # 0x80 == 128
        try:
            result = isIPv6Address(nonAscii + b"e80::1")
        except:
            self.fail("isIPv6Address shouldn't raise if addr contains values "
                "outside of the ASCII range")
        self.assertFalse(result)


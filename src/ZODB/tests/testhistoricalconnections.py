##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

def test_suite():
    import manuel.doctest
    import manuel.footnote
    import manuel.testing
    from ZODB.tests.util import setUp
    from ZODB.tests.util import tearDown
    return manuel.testing.TestSuite(
        manuel.doctest.Manuel() + manuel.footnote.Manuel(),
        '../historical_connections.txt',
        setUp=setUp, tearDown=tearDown,
        )

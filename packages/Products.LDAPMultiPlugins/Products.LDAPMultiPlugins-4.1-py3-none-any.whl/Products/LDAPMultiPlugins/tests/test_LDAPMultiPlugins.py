##############################################################################
#
# Copyright (c) 2005-2021 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" LDAPMultiPlugin and ActiveDirectoryMultiPlugin unit tests
"""

import unittest


class LMPBaseTests(unittest.TestCase):

    def _makeOne(self):
        return self._getTargetClass()('testplugin')

    def _getTargetClass(self):
        from ..LDAPPluginBase import LDAPPluginBase
        return LDAPPluginBase

    def test_demangle_invalid_userid(self):
        plugin = self._makeOne()
        plugin.prefix = 'prefix_'

        self.assertEqual(plugin._demangle(None), None)
        self.assertEqual(plugin._demangle('incorrectprefix'), None)
        self.assertEqual(plugin._demangle('prefix_user1'), 'user1')


class InterfaceTestMixin:

    def test_interfaces(self):
        from zope.interface.verify import verifyClass

        from Products.PluggableAuthService.interfaces.plugins import \
            IAuthenticationPlugin
        from Products.PluggableAuthService.interfaces.plugins import \
            ICredentialsResetPlugin
        from Products.PluggableAuthService.interfaces.plugins import \
            IGroupEnumerationPlugin
        from Products.PluggableAuthService.interfaces.plugins import \
            IGroupsPlugin
        from Products.PluggableAuthService.interfaces.plugins import \
            IPropertiesPlugin
        from Products.PluggableAuthService.interfaces.plugins import \
            IRoleEnumerationPlugin
        from Products.PluggableAuthService.interfaces.plugins import \
            IRolesPlugin
        from Products.PluggableAuthService.interfaces.plugins import \
            IUserEnumerationPlugin

        from ..interfaces import ILDAPMultiPlugin

        verifyClass(ILDAPMultiPlugin, self._getTargetClass())

        verifyClass(IAuthenticationPlugin, self._getTargetClass())
        verifyClass(ICredentialsResetPlugin, self._getTargetClass())
        verifyClass(IUserEnumerationPlugin, self._getTargetClass())
        verifyClass(IGroupsPlugin, self._getTargetClass())
        verifyClass(IGroupEnumerationPlugin, self._getTargetClass())
        verifyClass(IGroupsPlugin, self._getTargetClass())
        verifyClass(IPropertiesPlugin, self._getTargetClass())
        verifyClass(IRoleEnumerationPlugin, self._getTargetClass())
        verifyClass(IRolesPlugin, self._getTargetClass())


class ADMPTests(LMPBaseTests, InterfaceTestMixin):

    def _getTargetClass(self):
        from ..ActiveDirectoryMultiPlugin import ActiveDirectoryMultiPlugin
        return ActiveDirectoryMultiPlugin


class LMPTests(LMPBaseTests, InterfaceTestMixin):

    def _getTargetClass(self):
        from ..LDAPMultiPlugin import LDAPMultiPlugin
        return LDAPMultiPlugin

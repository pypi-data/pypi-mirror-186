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
""" LDAPMultiPlugins product initialization
"""

from AccessControl.Permissions import add_user_folders

from Products.PluggableAuthService.PluggableAuthService import \
    registerMultiPlugin

from .ActiveDirectoryMultiPlugin import ActiveDirectoryMultiPlugin
from .ActiveDirectoryMultiPlugin import addActiveDirectoryMultiPluginForm
from .ActiveDirectoryMultiPlugin import manage_addActiveDirectoryMultiPlugin
from .LDAPMultiPlugin import LDAPMultiPlugin
from .LDAPMultiPlugin import addLDAPMultiPluginForm
from .LDAPMultiPlugin import manage_addLDAPMultiPlugin


registerMultiPlugin(LDAPMultiPlugin.meta_type)
registerMultiPlugin(ActiveDirectoryMultiPlugin.meta_type)


def initialize(context):
    """ Initialize the LDAPMultiPlugin
    """

    context.registerClass(LDAPMultiPlugin,
                          permission=add_user_folders,
                          constructors=(addLDAPMultiPluginForm,
                                        manage_addLDAPMultiPlugin),
                          visibility=None)

    context.registerClass(ActiveDirectoryMultiPlugin,
                          permission=add_user_folders,
                          constructors=(addActiveDirectoryMultiPluginForm,
                                        manage_addActiveDirectoryMultiPlugin),
                          visibility=None)

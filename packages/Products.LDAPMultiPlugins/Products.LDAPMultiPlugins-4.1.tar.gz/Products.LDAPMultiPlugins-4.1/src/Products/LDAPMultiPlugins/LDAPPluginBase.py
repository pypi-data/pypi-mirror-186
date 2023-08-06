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
""" Base class for LDAPMultiPlugins-based PAS plugins
"""

import copy
import logging

from AccessControl import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from AccessControl.SecurityManagement import getSecurityManager
from Acquisition import aq_base
from OFS.Cache import Cacheable
from OFS.Folder import Folder

from Products.PluggableAuthService.interfaces.plugins import \
    IAuthenticationPlugin
from Products.PluggableAuthService.interfaces.plugins import \
    ICredentialsResetPlugin
from Products.PluggableAuthService.interfaces.plugins import IPropertiesPlugin
from Products.PluggableAuthService.interfaces.plugins import IRolesPlugin
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.utils import classImplements

from .interfaces import ILDAPMultiPlugin


logger = logging.getLogger('event.LDAPMultiPlugin')


class LDAPPluginBase(Folder, BasePlugin, Cacheable):
    """ Base class for LDAP-based PAS plugins """
    security = ClassSecurityInfo()

    manage_options = (BasePlugin.manage_options[:1] +
                      Folder.manage_options[:1] +
                      Folder.manage_options[2:] +
                      Cacheable.manage_options)

    _properties = BasePlugin._properties + Folder._properties

    # default 'id' attribute for groups
    groupid_attr = 'cn'

    def __init__(self, id, title=''):
        """ Initialize a new instance """
        self.id = id
        self.title = title

    @security.private
    def _getLDAPUserFolder(self):
        """ Safely retrieve a LDAPUserFolder to work with """
        embedded_luf = getattr(aq_base(self), 'acl_users', None)

        return embedded_luf

    @security.private
    def authenticateCredentials(self, credentials):
        """ Fulfill AuthenticationPlugin requirements """
        acl = self._getLDAPUserFolder()
        login = credentials.get('login')
        password = credentials.get('password')

        if not acl or not login or not password:
            return None, None

        user = acl.getUser(login, pwd=password)

        if user is None:
            return None, None

        return (user.getId(), user.getUserName())

    @security.private
    def resetCredentials(self, request, response):
        """ Fulfill CredentialsResetPlugin requirements """
        user = getSecurityManager().getUser()
        acl = self._getLDAPUserFolder()

        if user:
            acl._expireUser(user)

    @security.private
    def getPropertiesForUser(self, user, request=None):
        """ Fullfill PropertiesPlugin requirements """
        acl = self._getLDAPUserFolder()

        if acl is None:
            return {}

        unmangled_userid = self._demangle(user.getId())
        if unmangled_userid is None:
            return {}

        ldap_user = acl.getUserById(unmangled_userid)

        if ldap_user is None:
            return {}

        # XXX Direct attribute access. Waaa!
        properties = copy.deepcopy(ldap_user._properties)

        # Need to clean up: The propertysheet mechanism will
        # blow up if "None" is encountered
        for key, val in properties.items():
            if val is None:
                properties[key] = ''

        return properties

    @security.private
    def getRolesForPrincipal(self, user, request=None):
        """ Fullfill RolesPlugin requirements """
        acl = self._getLDAPUserFolder()

        if acl is None:
            return ()

        unmangled_userid = self._demangle(user.getId())
        if unmangled_userid is None:
            return ()

        ldap_user = acl.getUserById(unmangled_userid)
        if ldap_user is None:
            return ()

        groups = self.getGroupsForPrincipal(user, request)
        roles = list(acl._mapRoles(groups))
        roles.extend(acl._roles)

        return tuple(roles)

    @security.private
    def updateUser(self, user_id, login_name):
        """ Update the login name of the user with id user_id.

        No-op to satisfy the IUserEnumerationPlugin interface. This plugin
        cannot be used to update records, so we simply return False.
        """
        return False

    @security.private
    def updateEveryLoginName(self, quit_on_first_error=True):
        """Update login names of all users to their canonical value.

        No-op to satisfy the IUserEnumerationPlugin interface. This plugin
        cannot be used to update records, so we simply return False.
        """
        return False

    @security.private
    def _demangle(self, princid):
        # Sanity check
        if not isinstance(princid, (str, bytes)):
            return None

        # User must start with our prefix (which is likely to be blank anyway)
        if not princid.startswith(self.prefix):
            return None
        return princid[len(self.prefix):]

    # Helper methods for simple group caching
    @security.private
    def _getGroupInfoCacheKey(self, gid):
        """_getGroupInfoCacheKey(id) -> (view_name, keywords)

        given a group id, return view_name and keywords to be used when
        querying and storing into the group cache
        """
        view_name = self.getId() + '__GroupInfoCache'
        keywords = {'id': gid}
        return view_name, keywords

    @security.private
    def _setGroupInfoCache(self, info):
        """Cache a group info"""
        gid = info['id']
        view_name, keywords = self._getGroupInfoCacheKey(gid)
        self.ZCacheable_set(info, view_name=view_name, keywords=keywords)

    @security.private
    def _getGroupInfoCache(self, gid, default=None):
        """Retrieve a group info from cache, given its group id.

        Returns None or the passed-in default if the cache
        has no group with such id
        """
        view_name, keywords = self._getGroupInfoCacheKey(gid)
        result = self.ZCacheable_get(view_name=view_name, keywords=keywords,
                                     default=default)
        return result


classImplements(LDAPPluginBase,
                IAuthenticationPlugin,
                ICredentialsResetPlugin,
                IPropertiesPlugin,
                IRolesPlugin,
                ILDAPMultiPlugin)

InitializeClass(LDAPPluginBase)

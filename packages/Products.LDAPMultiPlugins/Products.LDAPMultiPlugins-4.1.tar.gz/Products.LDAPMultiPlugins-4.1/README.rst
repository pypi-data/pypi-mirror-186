.. image:: https://github.com/dataflake/Products.LDAPMultiPlugins/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/dataflake/Products.LDAPMultiPlugins/actions/workflows/tests.yml
   :alt: Automated test results

.. image:: https://coveralls.io/repos/github/dataflake/Products.LDAPMultiPlugins/badge.svg
   :target: https://coveralls.io/github/dataflake/Products.LDAPMultiPlugins
   :alt: Test coverage

.. image:: https://img.shields.io/pypi/v/Products.LDAPMultiPlugins.svg
   :target: https://pypi.python.org/pypi/Products.LDAPMultiPlugins
   :alt: Current version on PyPI

.. image:: https://img.shields.io/pypi/pyversions/Products.LDAPMultiPlugins.svg
   :target: https://pypi.org/project/Products.LDAPMultiPlugins
   :alt: Supported Python versions


===========================
 Products.LDAPMultiPlugins
===========================

The LDAPMultiPlugins package provides `PluggableAuthService
<https://productspluggableauthservice.readthedocs.io>`_ plugins that use
LDAP as the backend for the services they provide. The PluggableAuthService
is a Zope user folder product that can be extended in modular fashion using
so-called plugins.

The plugins in this package provide a PluggableAuthService-compatible shim
around a `LDAPUserFolder <https://productsldapuserfolder.readthedocs.io>`_
instance. After instantiating a plugin all further configuration is done on the
LDAPUserFolder object itself, which is created automatically inside the plugin.
Visit the `ZMI` `Configure` tab to find it.


Bug tracker
===========
Please post questions, bug reports or feature requests to the bug tracker
at https://github.com/dataflake/Products.LDAPMultiPlugins/issues


Special features - Active Directory Multi Plugin
================================================
Properties of the ADMultiPlugin instance:

- groupid_attr - the LDAP attribute used for group ids.

- grouptitle_attr - the LDAP attribute used to compose group titles.

- group_class - the LDAP class of group objects.

- group_recurse - boolean indicating whether to determine group
  memberships of a user by unrolling nested group relationships
  (expensive). This feature is not guaranteed to work at this moment.


Active Directory configuration hints
====================================
In order for groups support to work correctly, you may have to set the
following properties. Every situation is different, but this has helped
some people succeed:

- On the "Properties" tab for the ActiveDirectoryMultiPlugin, set the
  groupid_attr property to "name".

- On the contained LDAPUserFolder's "Configure" tab, choose a 
  property other than "objectGUID", e.g. "sAMAccountName" for the
  User ID property. To get to the LDAPUserFolder, click on the
  ActiveDirectoryMultiPlugin "Content" tab.

Please see README.ActiveDirectory from the LDAPUserFolder package for
additional information.

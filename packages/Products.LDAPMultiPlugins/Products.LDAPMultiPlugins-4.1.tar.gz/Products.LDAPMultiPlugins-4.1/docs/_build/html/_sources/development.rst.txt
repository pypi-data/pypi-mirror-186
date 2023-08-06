Development
===========

Getting the source code
-----------------------
The source code is maintained on GitHub. To check out the trunk:

.. code-block:: console

  $ git clone https://github.com/dataflake/Products.LDAPMultiPlugins.git

You can also browse the code online at
https://github.com/dataflake/Products.LDAPMultiPlugins


Bug tracker
-----------
For bug reports, suggestions or questions please use the
GitHub issue tracker at
https://github.com/dataflake/Products.LDAPMultiPlugins/issues.


Running the tests
-----------------
:mod:`Products.LDAPMultiPlugins` ships with its own :file:`buildout.cfg`
buildout configuration file. The buildout procedure will set up all
requirements for running the unit tests and building the documentation.

.. code-block:: console

    $ cd Products.LDAPMultiPlugins
    $ python3.7 -m venv .
    $ bin/pip install -U pip wheel       # Make sure pip is compatible
    $ bin/pip install "setuptools<52" zc.buildout tox twine
    $ bin/buildout
    ...

Once you have a buildout, the tests can be run as follows:

.. code-block:: console

   $ bin/test
   Running tests at level 1
   Running zope.testrunner.layer.UnitTests tests:
     Set up zope.testrunner.layer.UnitTests in 0.000 seconds.
     Running:
   ..............................................................
     Ran 62 tests with 0 failures and 0 errors in 0.043 seconds.
   Tearing down left over layers:
     Tear down zope.testrunner.layer.UnitTests in 0.000 seconds.

Code coverage and linting is done through the script at ``bin/tox``:

.. code-block:: console

  $ bin/tox -pall  # This runs all tests in parallel to save time

Calling it without any arguments will run the unit tests, code coverage
report and linting. You can see the tests configured for it with the ``-l``
switch:

.. code-block:: console

  $ bin/tox -l
  lint
  py35
  py36
  py37
  py38
  py39
  coverage

``py27`` represents the unit tests, run under Python 2.7. You can run each
of these by themselves with the ``-e`` switch:

.. code-block:: console

  $ bin/tox -e coverage

Coverage report output is as text to the terminal, and as HTML files under
``parts/coverage/``.

The result of linting checks are shown as text on the terminal as well as
HTML files under ``parts/flake8/``


Building the documentation using :mod:`zc.buildout`
---------------------------------------------------
The :mod:`Products.LDAPMultiPlugins` buildout installs the Sphinx
scripts required to build the documentation, including testing
its code snippets:

.. code-block:: console

    $ cd docs
    $ make html
    ...
    build succeeded.

    Build finished. The HTML pages are in _build/html.


Making a release
----------------
These instructions assume that you have a development sandbox set
up using :mod:`zc.buildout` as the scripts used here are generated
by the buildout.

.. code-block:: console

    $ cd Products.LDAPMultiPlugins
    $ bin/buildout -N
    $ bin/buildout setup setup.py sdist bdist_wheel
    $ bin/twine upload -s dist/Products.LDAPMultiPlugins-<VERSION>*

The ``bin/buildout`` step will make sure the correct package information
is used.

.. _dev-setup:

===========================
Developer Setup for Portmod
===========================

There are a few additional requirements beyond what is necessary to run
portmod if you want to develop portmod.

First, you need a local version of the git repository. You probably want
to `fork <https://gitlab.com/portmod/portmod/-/forks/new>`__ the
project, and clone your fork rather than cloning portmod itself.

In addition to the normal runtime requirements, you will also need:

- pytest (at least, to run tests locally after you’ve made changes, which you need to do).
- setuptools_scm (needed for getting the version number of your local development version).
- setuptools_rust (needed for compiling the native library).

Note that working with the development version means you’ll need to
compile the rust native extension yourself, hence Rust is a required
dependency. See the notes included on the :ref:`installation` page.

Pip editable install
--------------------

You can use the command ``pip install --editable .[test]`` from within
your local copy of the repository to install both the regular
dependencies and the above development dependencies, in addition to
linking to this version of portmod from within site-packages.

Note that this will not be able to coexist with an installed release
version of portmod, and you will need to uninstall it prior to
installing in non-editable mode.

When running portmod from within an editable install, it's necessary
to add the location of the portmod code repository to ``PYTHONPATH``,
as editable installs are not fully compatible with the way portmod sets
up the sandbox. If this is not done, portmod will not detect the location
of the portmod install when setting up the sandbox for src_unpack, and
portmodlib will fail to import.

Manual setup
------------

There are executable files that mimic all of portmod’s entry points in
the ``bin`` directory in the root of the project. You can execute those
manually, or add the directory to your path to be able to run portmod
commands using your development version.

Native Library
--------------

A native rust library is compiled alongside portmod and is required at
runtime.

It will be built automatically if you use ``pip install -e .``, or can
be invoked manually using ``python setup.py build_rust --inplace``. You
may want to also use the ``--release`` option to build the optimized
version.

If any rust code changes, the native extension will need to be rebuilt,
and also note that if the optimized version is used, changes to
localized ``.ftl`` files will not come into effect until the library is
rebuilt, as they are compiled into the native library. When compiled in
debug mode the ``.ftl`` files will be parsed at runtime instead, at a
small performance penalty.

(Optional) Pre Commit
---------------------

You can use `pre-commit <https://pre-commit.com/>`__ to run most of the
checks that will later be done by CI before each commit is made (this
includes everything but running inquisitor against the openmw-mods
repository, and running the test suite).

All that needs to be done to set it up is run ``pre-commit install``
from within the portmod repository once you have pre-commit installed
(via either your distribution’s package manager or pip).

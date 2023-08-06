.. _package-development:

Package Development
===================

Basic Packaging
---------------

.. toctree::
   :maxdepth: 1

   naming
   manifest
   dependencies
   use-flags
   archives
   guidelines
   pybuild/pybuild

Advanced Packaging
------------------

.. toctree::
   :maxdepth: 1

   common
   modules

Setup
-----

To be able to create packages that you can use you will need to fork the repository you want to contribute to, and set up a clone of your fork (this is described in :ref:`contributing`):

You will also need to adjust :ref:`repos.cfg` to reference your fork instead of the original package repository. This will allow you to install packages you have added or modified via the ``merge`` prefix subcommand, which is necessary for testing the package before you submit it.

.. code-block:: ini
   :caption: Example repos.cfg

   [<repo>]
   location = /path/to/your/cloned/fork
   # You may want to disable auto_sync, as it may not work properly on your fork
   auto_sync = False
   ...

When you have finished working with the repository, you may want to revert your changes to repos.cfg to make sure the repository is kept up to date when you run ``portmod sync``. Otherwise you will need to manually make sure your fork is up to date.

Packaging Mods
~~~~~~~~~~~~~~
Refer to the guides on `the wiki <https://gitlab.com/portmod/portmod/-/wikis/home>`_. The package repositories for each supported game have different packaging conventions to match the installation requirements of the engines.

You may also want to consult the base :py:mod:`pybuild` documentation, which package repositories build on top of.

Custom Repositories
~~~~~~~~~~~~~~~~~~~

Alternatively, you can create your own package repository as described in :ref:`repos.cfg`. Full details of repository metadata are described in :ref:`repositories`.

If you publish your custom repository other people can

This guide does not currently document the necessary requirements to set up a package repository for a completely new game. If you wish to do so, contact the authors for assistance (contact details are provided in Portmod's `README <https://gitlab.com/portmod/portmod#communication>`_).

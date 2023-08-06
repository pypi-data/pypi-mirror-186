:orphan:

.. _repositories:

====================
Package Repositories
====================

Repositories have the following basic file structure:

::

   ./profiles/repo_name
   ./CATEGORY_NAME/metadata.yaml
   ./CATEGORY_NAME/PACKAGE_NAME/PACKAGE_NAME-VER.pybuild
   ./CATEGORY_NAME/PACKAGE_NAME/PACKAGE_NAME-OTHER_VER.pybuild
   ./CATEGORY_NAME/PACKAGE_NAME/Manifest
   ./CATEGORY_NAME/PACKAGE_NAME/metadata.yaml

Profiles
--------

.. toctree::
   :maxdepth: 2

   profiles
   metadata.yaml
   layout.conf

Categories
----------

Any category must be listed in ``profiles/categories`` and contain a
:ref:`metadata.yaml` file.

Packages
--------

Mod directories must be in a subdirectory of a category and their
directory name should be the same as the base name of the mod’s pybuilds
(excluding version).

The ``Manifest`` file is optional, but is required to contain a manifest
entry for each source file listed in SRC_URI (i.e. only optional for
pybuilds without sources).

:ref:`metadata.yaml` is optional.

Profiles Directory
------------------

The files in profiles are optional, except for repo_name.

+------------------+---------------------------------------------------+
| File             | Description                                       |
+==================+===================================================+
| arch.list        | A newlline-separated list of architectures. An    |
|                  | architecture may refer to a game-engine variant   |
|                  | or an operating system, and is used to            |
|                  | distinguish configurations where a package may be |
|                  | stable when used in the context of one, but       |
|                  | unstable in the context of another.               |
+------------------+---------------------------------------------------+
| categories       | A newline-separated list of categories. These     |
|                  | determine which directories in the root of the    |
|                  | repository are considered categories containing   |
|                  | packages. Directories not listed in this file     |
|                  | will not be detected as containing packages.      |
+------------------+---------------------------------------------------+
| lic\             | A yaml file containing a mapping from license     |
| ense_groups.yaml | groups to a whitespace-separated list of license  |
|                  | names. Each group can be referenced within        |
|                  | ACCEPT_LICENSE by prefixing it with an ``@``, and |
|                  | they also reference each other using the same     |
|                  | method.                                           |
+------------------+---------------------------------------------------+
| package.mask     | A :ref:`package.mask`                             |
|                  | file which applies regardless of profile          |
+------------------+---------------------------------------------------+
| profiles.yaml    | A yaml file containing profile declarations. See  |
|                  | :ref:`profiles`.                                  |
+------------------+---------------------------------------------------+
| repo_name        | A file containing a single line with the name of  |
|                  | this repository                                   |
+------------------+---------------------------------------------------+
| use.yaml         | A file describing the global use flags,           |
|                  | containing a mapping of use flag names to         |
|                  | descriptions                                      |
+------------------+---------------------------------------------------+
| use.alias.yaml   | A file describing global use flags which have     |
|                  | their values tied to packages. Contains a mapping |
|                  | of use flag names to package atoms.               |
+------------------+---------------------------------------------------+
| desc             | A directory containing USE_EXPAND descriptor      |
|                  | files. Each file has the same form as             |
|                  | ``use.yaml``.                                     |
+------------------+---------------------------------------------------+

Metadata Directory
------------------

The metadata directory is optional

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - File
     - Description
   * - groups.yaml
     - Defines maintainer groups
   * - layout.conf
     - See :ref:`layout.conf`
   * - news
     - See `GLEP 42 <https://www.gentoo.org/glep/glep-0042.html>`__, noting
       that news files are in yaml format rather than XML. Specification for
       the files can be found `here <https://gitlab.com/portmod/portmod/-/blob/master/src/news.rs>`__
       (TODO: Rustdoc), and the directory structure follows GLEP 42.

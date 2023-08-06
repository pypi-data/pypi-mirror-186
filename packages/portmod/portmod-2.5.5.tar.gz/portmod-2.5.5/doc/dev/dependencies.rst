Dependencies
============

One of portmod's most useful features is automated dependency resolution.
You can mark packages as requiring or conflicting with other packages, as well as having these relationthips be conditional on both the configuration of the package and the packages being depended on.

Runtime Dependencies
--------------------
Most mod dependencies are runtime dependencies, that is, they are dependencies that must be satisfied eventually (so that the game can run), but may not need to be satisfied for package installation.

Runtime dependencies should be specified in :py:attr:`pybuild.Pybuild2.RDEPEND`.

See :py:attr:`pybuild.Pybuild2.DEPEND` for the format details.

Build Dependencies
------------------
Unlike software package managers, build dependencies are less frequently used by mods, as htey are usually packaged so that they can be installed without changes to their files, however build dependencies are still useful if mods require tools to patch them prior to installation.

Build dependencies differ from Runtime dependencies in that they ensure that packages will have these dependencies satisfied before the package is installed. In addition, any runtime dependencies of a package's build dependencies will be satisfied before package installation begins.

Build dependencies should be specified in :py:attr:`pybuild.Pybuild2.DEPEND`, which also includes format details.

External Resources
------------------

Portmod's dependency specification is heavily based on Gentoo/Portage's specification, documented both on the `Gentoo Developer Manual <https://devmanual.gentoo.org/general-concepts/dependencies/index.html>`_ and the `Package Manager Specification Section 8 <https://projects.gentoo.org/pms/7/pms.html#x1-670008>`_.

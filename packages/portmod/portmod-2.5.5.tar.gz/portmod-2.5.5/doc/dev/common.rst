Common Packages
===============

Packages in the `common` category are a special type of package which can be imported within other packages without needing to be installed.

E.g. Usage

.. code-block:: python

   from common.git import Git

   class Package(Git):
      ...

Properties
~~~~~~~~~~

These packages are implicitly included in :py:attr:`pybuild.Pybuild2.DEPEND` for packages importing them. When installed, this implicit dependency is pinned to the version, but not the revision, meaning that version changes to ``common`` packages will result in any installed package which uses the ``common`` package being rebuilt. This means that version bumps should only be used for changes which result in the package installing differently.

If you don't want to trigger rebuilds, for example, when fixing bugs which cause a fatal error when they occur, you can bump the revision instead.

``common`` dependencies are not versioned by default, so if the interface for a ``common`` package changes in a way which is not backwards-compatible, it should be moved to a new package (e.g. ``common/git2``).

The consequence of this is that ``common`` packages should only include patch versions [1]_ and revisions, while major/minor versions should be part of the package name.


.. [1] See https://semver.org/ for a description of patch vs major/minor version components.

Creating common packages
~~~~~~~~~~~~~~~~~~~~~~~~

``common`` packages are themselves regular packages and need to be installed, which means
that they must also include a ``Package`` class with basic information about the ``common`` package itself.

E.g. the ``common/git`` package:

.. code-block:: python
   :caption: ``common/git/git-1.0.pybuild``

   from pybuild import Pybuild2

   class Package(Pybuild2):
      NAME = "Git"
      DESC = "Pybuild Class that directly fetches from Git repos"
      # This package relies on no repository or profile infrastructure,
      # so it is safe to consider stable on all architectures once stabilized
      KEYWORDS = "**"

   class Git(Pybuild1):
      # A description is useful to provide instructions to anyone who wants
      # to use the package
      # Currently there is no sphinx APIDoc created for common packages, so it is
      # recommended to create a wiki page duplicating this description.
      """
      Pybuild Class that directly fetches from Git repos

      Subclasses should specify GIT_SRC_URI, containing a use-reduce-able
      list of remote git repositories
      Optionally, GIT_BRANCH, GIT_COMMIT and GIT_COMMIT_DATE can be used to specify
      what branch and commit should be used.
      """
      GIT_SRC_URI: str
      GIT_BRANCH: Optional[str] = None
      GIT_COMMIT: Optional[str] = None
      GIT_COMMIT_DATE: Optional[str] = None

      def __init__(self):
         # You can use __init__ to modify the package's attributes so that they are
         # not overridden as they would be by attributes defined in the class scope.
         if not self.GIT_BRANCH and not self.GIT_COMMIT and not self.GIT_COMMIT_DATE:
              self.PROPERTIES = self.PROPERTIES + " live"

      def src_unpack(self):
         # You may want to call the super version of the method, so that any other
         # classes in the package's class heirarchy get invoked.
         # If you specifically want to ignore the default behaviour, you can
         # omit this, but this means that packages with multiple superclasses will
         # need to call their parent class phase functions manually.
         super().src_unpack()
         # The remainder of the code has been omitted for brevity
         ...

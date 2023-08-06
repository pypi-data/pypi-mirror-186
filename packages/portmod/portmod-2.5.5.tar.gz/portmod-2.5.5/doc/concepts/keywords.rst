.. _keywords:

========
Keywords
========

Most packages declare one of the following engine-specific keywords in
their KEYWORDS field:

1. Stable: ``arch`` (E.g. ``openmw``) - This version of the mod
   and the pybuild are tested and not known to have any serious issues
   with the given platform.
2. Testing: ``~arch`` (E.g. ``~openmw``) - The version of the
   mod and the pybuild are believed to work and do not have any known
   serious bugs, but more testing should be performed before being
   considered stable.
3. No keyword: If a package has no keyword for a given arch, it means it
   is not known whether the package will work, or that insufficient
   testing has occurred for ~arch.
4. Masked: ``-arch`` (E.g. ``-openmw``) The package version will
   not work on the arch. This likely means it relies on a feature not
   supported by the engine, or contains serious bugs that make it
   unusable.

By default, only stable versions of packages are installed. For unstable
versions you will need to accept the keyword.

You can enable testing packages by default by overriding the default
``ACCEPT_KEYWORDS`` in :ref:`portmod.conf` with the testing keyword appropriate
for your engine.

You can accept keywords for specific packages by adding the mod version
and keyword to :ref:`package.accept_keywords`. E.g:

::

   =base/patch-for-purists-3.2.1 ~openmw
   # To ignore keywords and make the package visible regardless of keywords
   >=base/patch-for-purists-3.1.3 **

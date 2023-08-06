.. _package.accept_keywords:

=======================
package.accept_keywords
=======================

The file ``{CONFIG_DIR}/package.accept_keywords`` can be used to configure the visibility of packages via their :ref:`keywords`.

E.g.::

    # This is a custom option
    >category/foo-1.2.3-r1 ~arch

Syntax
======
``package.accept_keywords`` should contain a list of package atoms, one per line, followed by the accepted :ref:`keywords`. The atoms must specify the package category, but other components such as the version are optional. The special ``**`` keyword can also be used to make a package visible regardless of keywords.

The file can also include comments, beginning with a ``#``.

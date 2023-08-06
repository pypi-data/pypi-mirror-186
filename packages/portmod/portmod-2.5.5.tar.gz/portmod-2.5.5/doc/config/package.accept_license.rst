.. _package.accept_license:

=======================
package.accept_license
=======================

The file ``{CONFIG_DIR}/package.accept_license`` can be used to allow the installation of packages with a license which is not accepted using the global ``ACCEPT_LICENSE`` setting.

E.g.::

    # This license is not accepted by default
    >category/foo-1.2.3-r1 license_name

Syntax
======
``package.accept_license`` should contain a list of package atoms, one per line, followed by the accepted license. The atoms must specify the package category, but other components such as the version are optional. The special ``*`` keyword can also be used to accept all licenses for a package, and license groups (see :ref:`repositories`) can be specified by prefixing them with a ``@``.

The file can also include comments, beginning with a ``#``.

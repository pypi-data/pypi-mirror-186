.. _package.use:

===========
package.use
===========

The file ``{CONFIG_DIR}/package.use`` can be used to configure :ref:`use-flags` for individual packages or package versions.

E.g.::

    # This is a custom option
    >category/foo-1.2.3-r1 flag -otherflag

Syntax
======
``package.use`` should contain a list of package atoms, one per line, followed by flags. The atoms must specify the package category, but other components such as the version are optional. Flags prefixed with a ``-`` are considered disabled, otherwise they are considered enabled.

The file can also include comments, beginning with a ``#``.

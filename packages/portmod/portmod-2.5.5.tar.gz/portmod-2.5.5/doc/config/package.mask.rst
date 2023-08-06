.. _package.mask:

============
package.mask
============
The file `{CONFIG_DIR}/package.mask` can be used to prevent certain packages from being installed.

If a package is broken, and you want to skip that version, you can add the exact version to the file::

    # Version is broken
    =category/foo-1.2.3-r1

This can also be useful for packages where you need a particular version so that your savegame doesn't break.
E.g.::

    # Newer versions break savegame
    >category/foo-1.2.3-r1

Syntax
======
`package.mask` should contain a list of package atoms, one per line. These atoms must specify the package category, but other components such as the version are optional.

The file can also include comments, beginning with a `#`. Any comments immediately preceding an atom will be treated as descriptive comments and will be displayed if the package mask causes any error messages. Descriptive comments are also linked to atoms which follow, until a newline is encountered.

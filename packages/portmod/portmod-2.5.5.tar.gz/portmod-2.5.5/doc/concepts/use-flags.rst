.. _use-flags:

=========
Use Flags
=========

Use flags are the primary method of configuring portmod’s packages.

Global Flags
------------

Global use flags are enabled by default for all packages (unless
explicitly disabled for a specific package). You can enable or disable a
use flag by including it in the ``USE`` variable in :ref:`portmod.conf`. If
prefixed by a ``-``, the flag will be considered disabled, otherwise it
will be considered enabled.

E.g. :ref:`portmod.conf`

.. code:: python

   USE = "tribunal -bloodmoon"

You can also enable a global use flag using
``portmod <prefix> use -E <flag>``, and explicitly disable a flag using
``portmod <prefix> use -D <flag>``.

You should note that explicitly disabling a flag is not the same as
unsetting the flag. When explicitly disabled (e.g. ``-tribunal``), all
packages using the flag will disable it. You can unset a use flag using
``portmod <prefix> use -R <flag>``, which will remove the flag from the
``USE`` variable in ``portmod.conf`` if it’s been either enabled or
disabled, and will make packages revert to their default behaviour for
that flag (individual packages declare whether a flag is enabled or
disabled by default).

Local Flags
-----------

Local flags are similar to global flags, but only apply to a specific
package. Local flags are declared in the file :ref:`package.use` in the
``CONFIG_DIR``.

Each line in this file should begin with a package specifier, and end
with a (space separated) list of flags.

E.g. :ref:`package.use`

::

   base/morrowind tribunal -bloodmoon
   >=landmasses/tamriel-rebuilt-19.12 travels music -preview

You can also enable or disable local flags using the ``-m`` argument to
the ``use`` subcommand, with the atom for the package you want to
disable. E.g. ``portmod <prefix> use -E <flag> -m <atom>``.

Temporary use flags
-------------------

You can temporarily set flags using the ``USE`` environment variable.

E.g. in bash

.. code:: bash

   USE=-tribunal portmod <prefix> merge -uDN @world

After changing use flags
------------------------

After making changes to your use flag configuration, you should always
run an update ( ``portmod <prefix> merge -uD @world``) to make sure that
any packages are rebuilt if they need to be. Just changing a use flag
will not modify your installed mod packages.

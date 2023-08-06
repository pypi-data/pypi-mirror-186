.. _user-sets:

====
sets
====

You can create your own :ref:`sets` by adding set files to the ``sets``
directory in the ``CONFIG_DIR``. A set file is a file where the
filename (no file extension) corresponds to the set name, and the
contents are a newline-separated list of mod atoms. Set files can also
include comments (lines starting with ``#``).

E.g. ``CONFIG_DIR/sets/mymods``

::

   # This is a list of mods
   gameplay-advancement/ncgd
   assets-meshes/rr-better-meshes

User sets with the same name as a builtin set will be ignored in favour of the
builtin sets, as user sets have the lowest priority when loading.

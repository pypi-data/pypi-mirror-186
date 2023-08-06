===========
Basic Usage
===========

There are a number of executables installed with Portmod, however for
the most part you only need to use the ``portmod`` executable, combined
with the prefix name you created using the ``portmod init`` subcommand,
which will be represented here by ``<prefix>``.

Mods can be installed by passing the relevant atoms as command line
arguments to the merge command. E.g.: ``portmod <prefix> merge omwllf``

You can search for mods using the ``search`` subcommand. By default, it
searches the name only but will also search the description if you
include the ``--description``/``-d`` option. E.g.:
``portmod <prefix> search --description foo``

Specific versions of mods can be installed by including the version
number: ``portmod <prefix> merge abandoned-flat-2.0``

Specified mods will be automatically be downloaded, configured and
installed.

The ``-c``/``--depclean`` flag will remove the specified mods and all
mods that depend on, or are dependencies of, the specified mods.

The ``-C``/``--unmerge`` flag will remove the specified mods, ignoring
dependencies

You can view useful information about your current setup using
``portmod <prefix> info``.

Changes to package repositories can be fetched using the ``portmod sync`` command.

You can update all installed mods (including dependencies and dependency
changes) using the command
``portmod <prefix> merge --update --deep @world`` (or
``portmod <prefix> merge -uD @world``)

After updates, you should clean unneeded dependencies using
``portmod <prefix> merge --depclean`` (without any arguments). This can
also be done during updates using the ``--auto-depclean``/``-x`` flag,
however you should carefully examine the transaction list to make sure
that it isn’t removing anything you wanted to keep.

Downloads
---------

Downloaded source files are stored in ``$CACHE_DIR/downloads`` (as
reported by ``portmod <prefix> info``). Additionally, portmod will
also detect files found in ``~/Downloads``, in ``XDG_DOWNLOAD_DIR`` (on Linux),
as well as the path stored in the ``DOWNLOADS`` environment variable, if present.
These files will be moved into ``$CACHE_DIR/downloads`` during installation.

Note that due to technical limitations of the ``SRC_URI`` syntax,
download files cannot include spaces, and in the case of manual
downloads these will usually be replaced by underscores in the file
expected by portmod. To handle this, portmod will detect and rename such
files containing spaces to include only underscores, there is no need to
rename them manually.

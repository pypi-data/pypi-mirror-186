Setup
=====

Portmod has two different levels of configuration: Prefixes, and
profiles.

Prefixes are user-created and allow multiple configurations to exist
side-by-side on a system.

Profiles are defined by the repository, and provide default settings for
a prefix.

Game-specific Guides
--------------------

Some game engines have their own setup guides which provide information
specific to that game engine.

See `The Wiki <https://gitlab.com/portmod/portmod/-/wikis/home>`__
for details.

Creating a prefix
-----------------

You can create a prefix using the command
``portmod init <prefix> <arch>``.

``<prefix>`` is the name of the prefix you want to create. This name can
be arbitrary, but it is recommended, unless you are intending on setting
up multiple prefixes for the same architecture, to use the architecture
as the prefix name (e.g. ``openmw``).

``<arch>`` is the architecture of the prefix (i.e. the game engine).
Known supported architectures are listed in
`profiles/arch.list <https://gitlab.com/portmod/meta/-/blob/master/profiles/arch.list>`__,
but you may want to consult the specific package repository you are
using.

Unless you pass the ``--no-confirm`` argument to ``portmod init``, it
will prompt you to select package repositories and a profile.
Details on how to do this manually are provided in the sections below.

Optionally, you can include a directory as a third argument to
``portmod init``. Doing so will install the prefix into that directory,
something which is necessary for certain DRM systems where the game can
only be launched if the files are in a certain place (and also removes
the need to copy source files for engines which don’t support any sort
of virtual file system).

Add and Synchronize Package repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the command ``portmod <prefix> select repo list`` to list
available repositories, and add them using
``portmod <prefix> select repo add <repo>``, where repo is either the
name of the repo, or the number in the list.

This will both initialize and synchronize the selected repository, and
add it to the ``REPOS`` variable in your prefix’s :ref:`portmod.conf`.
Repositories are shared between prefixes, but only those listed in ``REPOS``
will be used.

Select a Profile
~~~~~~~~~~~~~~~~

The profile provides default settings that are tailored for your game
setup. See :ref:`profiles` for details about the different profile options.

In addition to during prefix initialization, you can use
``portmod <prefix> select profile list`` to see a list of available
profiles, and ``portmod <prefix> select profile set NUM`` can be used to
select the profile you want.

Install System packages
-----------------------

Most profiles require certain “system” packages, which are necessary for
the proper generation of configuration files and the proper functioning
of mods after they have been installed.

Once prefix creation is complete you should install these system
packages by performing a world update:
``portmod <prefix> merge --update --deep @world`` (or
``portmod <prefix> merge -uD @world``).

Technically, ``--deep`` and ``--update`` are not necessary the first
time, as they have no effect on packages which have not been installed,
however it is a good idea to familiarize yourself with this command
since it also is how you should install package updates.

(Optional) Creating a Prefix Alias
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*For users of shells other than bash, you will need to look elsewhere
for this information, and note that other unix shells have similar
features, though the syntax may vary. Consult your shell’s documentation
for information on how to create aliases.*

If you use the bash shell, you can create an alias for prefix-related
commands by adding ``alias <alias_name>="portmod <prefix>"``.

For example, for an ``openmw`` prefix, you could do the following:

.. code:: bash

   alias omw="portmod openmw"

This would allow you to use the command ``omw merge`` in place of
``portmod openmw merge``.

You could even create an alias for each of the subcommands (“merge”,
“select”, “search”, “query”, “use”). E.g.
``alias omwmerge="portmod openmw merge"``.

Note that the documentation on this wiki will not assume that you have
created an alias, and will always give the command in full.

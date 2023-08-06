.. _repos.cfg:

=========
repos.cfg
=========

The repos.cfg file in the portmod config directory (See :ref:`portmod.conf`)
can be used to specify the various repositories that Portmod pulls information
from.

The following entry is for the meta repository which is automatically
included and does not need to be specified in ``repos.cfg``.

.. code:: ini

   [meta]
   location = ${PORTMOD_LOCAL_DIR}/repos/meta
   auto_sync = True
   sync_type = git
   sync_uri = https://gitlab.com/portmod/meta.git
   priority = -1000

Local Repository
----------------

A local repository can be specified by setting ``auto_sync = False`` (or
omitting it, as it is false by default).

E.g. to create a custom repository where you can add your own pybuilds,
add the following entry to repos.cfg.

.. code:: ini

   [user]
   location = /path/to/repo
   auto_sync = False
   priority = 0

You also likely want to create the file ``/metadata/layout.conf`` within
the repository, and specify a parent repository using
``masters = "<repo>"``. This makes your custom repo inherit metadata
from the other repo, such as categories and global use flags.
If you omit this then portmod won’t be able to find your packages without
you ensuring that their category exists in the ``profiles/categories``
file in your repo.

``metadata/layout.conf``:

.. code:: ini

   masters = "<repo>"

The priority needs to be higher than the priority of the default
repository if you have packages with the same name as those in the main
repo, as if a package is otherwise identical to the loader (i.e. the packages
have the same name and version) Portmod will attempt to load the package in
the higher priority repo.

The only required file that must exist in a repo is
``profiles/repo_name``, which should include a single line containing
the name of your repository.

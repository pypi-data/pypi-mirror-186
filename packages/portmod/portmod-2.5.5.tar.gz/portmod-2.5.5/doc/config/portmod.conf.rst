.. _portmod.conf:

============
portmod.conf
============

The portmod.conf file is used for configuring Portmod’s global options.
It can be found in the portmod config directory, found in one of the
following locations:

.. list-table::
   :widths: 15 85

   * - Linux
     - ``~/.config/portmod``
   * - macOS
     - ``~/Library/Application\ Support/portmod``
   * - Windows
     - ``C:\Documents and Settings\<User>\Application Data\Local Settings\portmod\portmod``
       or
       ``C:\Documents and Settings\<User>\Application Data\portmod\portmod``

All config entries can be overridden using environment variables of the
same name. In the case of USE, ACCEPT_LICENSE and ACCEPT_KEYWORDS, this
will extend the value, rather than override it. E.g. setting the
environment variable ``USE=foo`` will use all use flags in your config
file (and profile) and also set the ``foo`` flag. Similarly,
``USE=-foo`` will disable foo if it is set in your config file or
profile.

You can also create a prefix-specific version of portmod.conf which will
apply the same options just to one prefix. This can be done by creating or
modifying the ``portmod.conf`` in the subdirectory of the portmod config
directory with the name of the prefix. E.g. ``~/.config/portmod/<prefix>/portmod.conf``

Format
======

The portmod config file uses a restricted subset of python with
extremely limited support for builtins. No imports are allowed.

Available builtins:

* ``join``: equivalent to ``os.path.join`` and can be
  used for specifying paths in a platform independant manner.
* ``PLATFORM``: equivalent to ``sys.platform``.


Variables used by Portmod
=========================

You may define arbitrary variables, but there are several that are
reserved for the use of Portmod and have a special meaning

All variables defined in portmod.conf are set as environment variables
during portmod execution.

ACCEPT_KEYWORDS
---------------

A string of whitespace separated keywords that indicate stability of
mods that you allow to be installed. By default this is generally the
stable keyword (equal to your arch, e.g. ``openmw`` or ``tes3mp``
without qualifiers).

If you also want to include unstable mods, prefix the keyword with a
``~``. E.g. ``ACCEPT_KEYWORDS = ~openmw`` or
``ACCEPT_KEYWORDS = ~tes3mp``.

PORTMOD_MIRRORS
---------------

Specifies a list of mirrors to use to fetch source files (mod archives).
Currently the only mirror is the default:
``https://gitlab.com/portmod/mirror/raw/master/``

ACCEPT_LICENSE
--------------

Specifies the globally accepted licenses. By default this is all except
EULA licenses, i.e. a value of ``* -@EULA``. If you want to only install
mods with Free licenses, you could, for example set this to
``ACCEPT_LICENSE = -* @FREE``.

See ``profiles/license_groups.yaml`` in the repo for details on the
available license groups.

.. _TEXTURE_SIZE:

TEXTURE_SIZE
------------

Specifies a function for choosing between texture size options. This
must contain an operator ``min`` or ``max``, followed by an optional
inequality.

-  ``min``: Chooses the smallest texture size available
-  ``max``: Chooses the largest texture size available
-  ``min >= NUM``: Chooses the smallest texture size available that is
   larger than NUM.
-  ``max <= NUM``: Chooses the largest texture size available that is
   smaller than NUM.

USE
---

Sets global use flags. See :ref:`use-flags` for details.

OMWMERGE_DEFAULT_OPTS
---------------------

The default options passed to ``portmod <prefix> merge`` (e.g flags such
as ``--verbose``, ``--no-confirm``, etc.). Will be ignored if
``--ignore-default-opts`` is passed.

REPOS
-----

The list of repositories (as a whitespace-separated string) which are
enabled for this prefix. Only packages from these repositories will
be found when installing or searching for packages.

MERGE_TOOL
----------

A command to be used to merge updates to configuration files.

The placeholders ``${orig}``, ``${new}`` and ``${merged}`` should be used
to specify the input files.

E.g.

.. code-block:: python

   MERGE_TOOL = "kdiff3 ${orig} ${new} --output ${merged}"

.. admonition:: Version

   Added in portmod 2.3

Use Expand Variables
--------------------

Use expand variables represent categories of global use flags for
enabling features across all packages that support them.

They can be enabled similarly to USE flags, but use a custom field. E.g.
for L10N flags, you can set

.. code:: python

   L10N = "ru"

Which will enable the flag ``l10n_ru`` globally, building support for
Russian localization into packages.

Note that supported use expand flags vary depending on your profile and architecture.

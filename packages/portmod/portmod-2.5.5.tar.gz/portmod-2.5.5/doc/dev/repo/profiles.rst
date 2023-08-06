.. _profiles:

========
Profiles
========

Profiles are used to provide preset configurations for users.

profiles.yaml
-------------

The file ``profiles/profiles.yaml`` describes the available profiles. It
contains a mapping with the architecture as the key at the root,
followed by a mapping of profile paths to profile stability keywords
(either stable or unstable). These paths should refer to a directory
within the profiles directory.

E.g.

.. code:: yaml

   openmw:
       dev: unstable
       default/openmw/1.0: stable

Profile Files
-------------

Within each profile directory the following files can be used to
customize the profile.

.. contents::
   :depth: 1
   :local:

packages
^^^^^^^^

A list of atoms to be included in the system set and thus installed by
default. Each line to be included in the system set should start with an
asterisk (``*``), followed by the atom to include. Lines not beginning
in an asterisk will be ignored.

package.mask
^^^^^^^^^^^^

A profile-specific list of masked packages.

See :ref:`package.mask`

.. _dev/package.use:

package.use
^^^^^^^^^^^

Default per-package use flags. The file can contain comments (starting
with ``#``) and lines containing a qualified atom (i.e. containing a
category, can also include versions and operators) followed by a
whitespace-separated list of flags. Flags can be disabled by prefixing
them with a ``-``.

See :ref:`package.use`

.. _use.force:

use.force
^^^^^^^^^

Global use flags that are required to always be enabled in this profile.
The format is the same as the contents of the ``USE`` variable in
:ref:`defaults.conf`.

.. _package.use.force:

package.use.force
^^^^^^^^^^^^^^^^^

Per-package use flags that are required to always be enabled in this
profile. The format is the same as package.use.

parent
^^^^^^

Defines another directory (via relative path) to be included in the
current profile. This allows profiles to share configuration, and it is
recommended that all profiles include the ``profiles/base`` directory in
their hierarchy.

.. _license_groups.yaml:

license_groups.yaml
^^^^^^^^^^^^^^^^^^^

A mapping of license group names to the licenses in the group. Licenses should be a whitespace-separated list.
Licenses listed are merged with the license groups in master repositories.

The special ``REDISTRIBUTABLE`` license group is used to determine if a package can be mirrored (and also if mirrors should be checked when fetching the file).

E.g.

.. code-block:: yaml
   :caption: profiles/license_groups.yaml

   REDISTRIBUTABLE: CC-BY CC-0 GPL-3

.. _defaults.conf:

defaults.conf
^^^^^^^^^^^^^

The format is the same as :ref:`portmod.conf`, but additional
variables are available. Also note that unlike the user-defined
defaults.conf, variables defined in defaults.conf which are not listed
on this page will not be set as environment variables (this is for
security reasons, as there are variables such as PATH which could be
abused).

As portmod.conf is a python file (albeit a restricted subset of the
language), other variables defined earlier in the same file can be
referenced directly. Additionally, you can reference the final value of
a variable using string templating. I.e. strings containing values of
the form ``${VAR}`` will be substituted for the final value of the
referenced variable once all conf files have been parsed.

Collapsible Variables

These variables contain whitespace-delimited sets (as strings), the
entries of which can be disabled (if enabled in a previously loaded conf
file) by prefixing them with a minus/hyphen (``-``).

+-----------------------------+----------------------------------------+
| Variable                    | Description                            |
+=============================+========================================+
| USE                         | Enabled use flags. These provide the   |
|                             | profile default enabled use flags.     |
+-----------------------------+----------------------------------------+
| ACCEPT_LICENSE              | A list of accepted licenses. License   |
|                             | groups, as specified in                |
|                             | profiles/:ref:`license_groups.yaml`,   |
|                             | can be included by prefixing the group |
|                             | name with an ``@``. An asterisk        |
|                             | (``*``) can be used to accept all      |
|                             | licenses by default, with the ability  |
|                             | to disable specific licenses by        |
|                             | default by prefixing them with ``-``.  |
|                             | Recommended defaults are ``* -@EULA``  |
|                             | or ``@FREE``.                          |
+-----------------------------+----------------------------------------+
| ACCEPT_KEYWORDS             | The default keywords to accept. Should |
|                             | usually only contain                   |
+-----------------------------+----------------------------------------+
| INFO_VARS                   | Variables to display when              |
|                             | ``portmod <prefix> info`` is run.      |
+-----------------------------+----------------------------------------+
| INFO_PACKAGES               | Packages to display when               |
|                             | ``portmod <prefix> info`` is run.      |
+-----------------------------+----------------------------------------+
| USE_EXPAND                  | The names of USE_EXPAND variables. The |
|                             | values they can take should be         |
|                             | described in the ``profiles/desc``     |
|                             | directory in a yaml file with a name   |
|                             | equal to the lowercased variable name, |
|                             | followed by ``.yaml``.                 |
+-----------------------------+----------------------------------------+
| USE_EXPAND_HIDDEN           | A subset of USE_EXPAND that should be  |
|                             | hidden to the user and not show up in  |
|                             | searches and transaction lists.        |
+-----------------------------+----------------------------------------+
| PROFILE_ONLY_VARIABLES      | This defines which variables cannot be |
|                             | modified by the user in their          |
|                             | portmod.conf (technically,             |
|                             | portmod.conf can configure everything  |
|                             | that defaults.conf can, with the       |
|                             | exception of the variables listed      |
|                             | here). Note that users can still use   |
|                             | ``profile.user`` to create a custom    |
|                             | profile and override these variables.  |
+-----------------------------+----------------------------------------+
| CACHE_FIELDS                | A list of fields that should be cached |
|                             | (e.g. fields that may be added by      |
|                             | classes in this repo which it would be |
|                             | useful to have accessible to external  |
|                             | software).                             |
+-----------------------------+----------------------------------------+

Other Variables

+-----------------------------+----------------------------------------+
| Variable                    | Description                            |
+=============================+========================================+
| ARCH                        | The architecture for the profile. See  |
|                             | `arch.list`. This is set automatically |
|                             | and should not be modified             |
+-----------------------------+----------------------------------------+
| TEXTURE_SIZE                | The algorithm for choosing texture     |
|                             | size. See :ref:`portmod.conf`          |
+-----------------------------+----------------------------------------+
| PORTMOD_MIRRORS             | The list of download mirrors. See      |
|                             | :ref:`portmod.conf`                    |
+-----------------------------+----------------------------------------+
| CASE_INSENSITIVE_FILES      | Whether or not files in the VFS should |
|                             | be case-insensitive. When enabled,     |
|                             | portmod will treat files of identical  |
|                             | path other than their case as the same |
|                             | when installing. Otherwise, such files |
|                             | may be installed side by side instead  |
|                             | of overriding each other.              |
+-----------------------------+----------------------------------------+
| OMWMERGE_DEFAULT_OPTS       | The default options passed to          |
|                             | ``portmod <prefix> merge``. See        |
|                             | :ref:`portmod.conf`                    |
+-----------------------------+----------------------------------------+
| MODULEPATH                  | The directory (relative to ``ROOT``)   |
|                             | which stores :ref:`modules`.           |
+-----------------------------+----------------------------------------+
| DOC_DEST                    | The default installation directory     |
|                             | for documentation when the `dodoc`     |
|                             | function is called.                    |
+-----------------------------+----------------------------------------+
| VARIABLE_DATA               | The directory, relative to ``ROOT``    |
|                             | should contain generated portmod files |
|                             | such as the package database.          |
|                             |                                        |
|                             | This variable should never be changed  |
|                             | since it takes effect immediately.     |
|                             | Instead, it is recommended to create   |
|                             | a new profile with a new value and     |
|                             | a migration tool to update the         |
|                             | filesystem.                            |
+-----------------------------+----------------------------------------+
| CFG_PROTECT                 | A glob-style patterns (or list of      |
|                             | patterns) indicating files which       |
|                             | should not be overwritten on           |
|                             | installation if they have been         |
|                             | modified since the file was first      |
|                             | installed. Instead, a ``.new`` file    |
|                             | will be created and users will be able |
|                             | to run the cfg updater to merge the    |
|                             | modifications.                         |
+-----------------------------+----------------------------------------+

===========================
Package Creation Guidelines
===========================

Source files which contain spaces in their name
-----------------------------------------------

The string-based syntax which is used for fields such as SRC_URI doesn’t
support spaces in names (given that spaces are used to separate tokens).
As such, source files which contain spaces should be renamed so that
they do not.

For source files that need to be manually downloaded, you should use the
same filename, but replace the spaces with underscores. Portmod will
automatically rename source files that contain spaces so that they
instead contain underscores (note: this is only done if the file’s hash
matches the hash of the file it’s looking for, to avoid interrupting
in-progress downloads).

E.g. ``Glow in the Dahrk-45886-2-8-2-1584579862.7z``, a file which must
be downloaded from NexusMods, should be included in SRC_URI as
``Glow_in_the_Dahrk-45886-2-8-2-1584579862.7z``

Patches go with the Mods they Patch
-----------------------------------

Rather than patches having their own build files, they should be
included with the mod they patch and applied automatically.

In the case of compatibility patches between two mods, they can be
included in either of the mods being patched (and should not be included
in both). It’s generally beneficial to include the patch with the mod
that is loaded last, as makes it easier to describe file overrides (it
is possible to have mod A with an install directory that overrides mod
B, even if mod B overrides mod A, however this is complicated and is
best avoided if possible).

*If you want to fix cycles when patching a mod that is loaded
afterwards, and still have the patch load last, you need to specify a
``PATCHDIR`` for the ``InstallDir``, in addition to specifying
``DATA_OVERRIDES``, allowing the InstallDir to be treated separately
from the other directories in the mod when sorting.*

Only include dependencies that are necessary
--------------------------------------------

Dependencies are strictly enforced, so unnecessary dependencies will get
in the way of users. If a dependency is not strictly necessary, such as
to satisfy the masters in a plugin, or to supply necessary assets, it
should not be included. There are currently no plans to support
recommended dependencies, but this may be revisited in future.

Source Archives should contain version numbers
----------------------------------------------

Many mods may include source archives which just include the mod name,
often updating them without changing that name at all.

So that portmod can track multiple versions simultaneously, and so that
one version of the file doesn’t get mistaken for another, you should
always include the version in the filename. This also helps better
convey the contents of the archive when viewed in isolation (e.g. when
looking at your download cache, or the file mirror).

Note that you can use arrow notation to specify the local name of a
source archive. E.g. ``https://foo.com/bar.zip -> bar-1.0.zip``.

.. _guidelines-naming:

Naming
------

Mod Package names should generally be the same as the upstream mod’s
name. Package names should also be short and abbreviations can be used
where they are appropriate. Do remember that, since portmod is a CLI
application, users need to type the name to interact with it, so it
might be useful to use abbreviations, or even adjust the name of the
package, when mods have names which are extremely long or complicated.

Note that it is also highly recommended that package names use
lowercase, non-accented characters, numbers and hyphens only, noting
that hyphens should be used where separators are required (e.g. instead
of spaces or underscores), and numbers in the name should not be used to
signify a version.

E.g. Skies .IV should be ``skies-4`` (i.e. ``{NAME}-{VERSION}``) not
``skies4`` or even
``skiesiv``. It might also be useful to use a more unique name, as
``skies/skies``, to include the category, is not a very descriptive
name.

The other supported characters, uppercase characters (``A-Z``), plus
signs (``+``), and underscores (``_``) should be avoided and are
basically only included due to allow certain unusual package names
(e.g. if there was a mod called Textures+, it could be included with the
name ``textures+``, or names where capitalization provides necessary
context could use capitals).

Also note that while hyphens are used to separate the mod name and
version, this trailing component is only considered the version if it is
a valid version.

E.g. in the atom ``foo-1``, the name is ``foo`` and the version ``1``,
but for ``foo-v1``, the name is ``foo-v1`` and no version is specified,
since ``v1`` is not considered a valid version number. See :ref:`version-syntax`
for details on what is considered a valid version.

Collections
-----------

Generally, mods that are simply multiple mods bundled together should
only be included as individual packages (a metamod could be created that
depends on all of the parts though). If the bundled mod contains new
content, then it may be included, if the new content is not available by
itself.

Also note that this usually doesn’t apply to mods by the same author
which contain multiple related, but otherwise independent parts,
particularly if they are distributed together. In general, having fewer
packages in the repository is simpler and easier to maintain.

``land-flora/ozzy-grass`` and ``assets-meshes/rr-better-meshes`` are
good examples for mods which are like collections, but can still be
included as a single package (the scopes of each component are closely
related, and they are created by the same author or group), while the
Morrowind Graphics and Sound Overhaul is a good example of a mod which
should not be included, as it collects a variety of mods from different
authors and with at times very different styles and scopes.

Scripting
---------

Avoid unnecessary scripts, such as in ``src_prepare``, as they are hard
to maintain and hard to process automatically.

Prefer instead to use the functionality of the INSTALL_DIRS array if
possible, which has several features for modifying source directories
(e.g. BLACKLIST, WHITELIST, RENAME, REQUIRED_USE. Note that multiple
InstallDirs can be created for the same directory, with different
blacklists/whitelists/REQUIRED_USE, and they are merged, in order,
during ``src_install``).

Bundled Dependencies
--------------------

Bundled dependencies should be de-bundled when possible.

Download Locations
------------------

Direct downloads are preferred, as they do not require user intervention
to install. If a mod does not have a direct download, but can be
redistributed, it can instead be hosted on one of portmod's mirrors.

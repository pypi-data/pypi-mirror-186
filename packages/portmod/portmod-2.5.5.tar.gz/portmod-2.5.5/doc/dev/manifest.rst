Generating the Manifest
-----------------------

In the tree, every package has a ``Manifest`` file. The Manifest file contains
various hashes and file size data for every external source that is to
be fetched. This is used primarily to verify the integrity of external files.

To generate the Manifest, use ``inquisitor manifest foo.pybuild``. When
new sources are added or removed, the ``Manifest`` must be regenerated.

Package Archives
================

Pybuild2.unpack
---------------
:py:func:`pybuild.Pybuild2.unpack` supports unpacking archives via :py:func:`shutil.unpack_archive`.

This includes support for the following formats:

- zip: ZIP file.
- tar: uncompressed tar file.
- gztar: gzip’ed tar-file
- bztar: bzip2’ed tar-file
- xztar: xz’ed tar-file

Pybuild1.unpack
---------------
:py:func:`pybuild.Pybuild1.unpack` supports unpacking archives via `patool <http://wummel.github.io/patool/>`__

Primary archive formats:

- zip
- tar, tar.gz
- 7z (requires 7zip, or p7zip, to be installed)

Secondary Archive Formats:

- rar (proprietary format which is only supported through the proprietary rar/unrar programs, as well as a non-free extension to 7zip. [1]_).
- tar.bz2 (has issues on windows due to the builtin windows ``tar`` command not properly supporting it).
- tar.xz (has had some issues related to detecting archives, since fixed in the development version of patool).


.. [1] Free implementations exist in `libarchive <https://github.com/libarchive/libarchive>`__,
   and `unar <https://theunarchiver.com/command-line>`__, but these are not supported by patool.
   libarchive's support is also incomplete (some archives fail to extract with the message
   "Parsing filters is unsupported").

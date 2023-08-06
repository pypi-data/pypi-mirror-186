.. _sandbox:

Sandbox
=======

The portmod sandbox allows safe access to dangerous functions such as
``shutil.rmtree`` while still allowing pybuilds to be as pythonic as
possible.

This is achieved through the use of RestrictedPython for loading package
metadata in an environment without access to file i/o or any dangerous
commands. During package installation and removal where file i/o is
necessary, package functions are run through the use of a sandbox
program such as
`bubblewrap <https://github.com/projectatomic/bubblewrap>`__ on Linux
and sandbox-exec on OSX.

In general, the following is restricted:

- File I/O in the global scope. All file I/O must be within functions
  in the Package class.
- Use of imports in the global scope, other than imports from the
  ``common`` or ``pybuild`` modules (the imports themselves can be in
  the global scope, however they will be ignored during package loading
  and using imported functions will cause an exception). - File I/O
  outside the build directory in ``src_unpack`` and ``can_update_live``.
- Network access outside ``src_unpack`` and ``can_update_live``
- File writes outside the build directory in all scopes

The idea is that this prevents:

1. Poorly written code from accidentally performing dangerous actions such
   as deleting your files.
2. Malicious actors from creating a seemingly benign third-party
   repository (or sneaking packages into a repository which is otherwise
   trustworthy) and causing either deliberate damage to your system or
   stealing your personal information when you try to install or update
   packages from that repository.

Python Sandbox
--------------

Note that for compatibility reasons, packages should be written to
target the minimum version of python portmod supports (this is currently
Python 3.7). Using features introduced in later versions of python will
break the packages on systems which are using an older version of
python.

Additionally, the following restrictions apply to the pybuild code:

- *Prior to Portmod 2.4*, you could only access the following modules:

  * ``pybuild``
  * ``pybuild.info``
  * ``pybuild.winreg``
  * ``filecmp``
  * ``glob``
  * ``os``
  * ``os.path``
  * ``sys``
  * ``shutil``
  *  ``stat``
  *  ``fnmatch``
  * ``re``
  * ``csv``
  * ``json``
  * ``typing``
  * ``collections``
  * ``common`` submodules (noting that ``common`` modules are subject to the
    same restrictions as pybuilds).

  *Since Portmod 2.4* all module imports are allowed. Modules outside the
  standard library and ``pybuild``/``common`` must be installed within the prefix
  and the package must depend on them.
- Use of the ``str.format`` function is banned. This is known to be
  unsafe and is disabled by RestrictedPython by default. It is
  encouraged to used f-strings instead.
- Access to attributes that begin with underscores is banned. The convention
  in python is that these attributes are considered hidden, and represent
  internal functions and variables which could change at any time.
  By blocking the use of them pybuilds are forced to use the more stable
  public module APIs.
- Use of the ``super`` function is allowed, however note that
  ``super().__init__(self)`` cannot be invoked manually due to underscored
  functions being banned. As such, it is automatically called in any
  Package class that overrides ``__init__``.
- Use of builtins that allow arbitrary code execution is banned.
  This includes ``exec``, ``compile``, ``eval``, etc.
- *Prior to Portmod 2.4*: The ``dir`` function was not implemented. The
  implementation omits private underscored fields, which are inaccessible
  anyway.

Executable Sandbox
------------------

All external executable calls are sandboxed using a platform-specific
sandbox command. This prevents filesystem write access outside the build
directory and prevents filesystem read access until all
potentially-unsafe network access has been completed (i.e. prevents a
malicious pybuild from scanning your system and uploading data to a
remote server).

Windows
~~~~~~~

Portmod uses Sandboxie on Windows. Please note that there are known
issues with Sandboxie (see #102), however in general it appears to be
working. If you encounter issues, please report them, as current tests
have been done almost exclusively via the test suite.

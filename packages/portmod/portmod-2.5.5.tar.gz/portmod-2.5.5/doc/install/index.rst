.. _installation:

==================
Installing Portmod
==================

Python
------

Portmod requires Python 3.7 or later.

Build dependencies
------------------

Since portmod 2.0 beta5, portmod compiles a rust extension using
`setuptools-rust <https://github.com/PyO3/setuptools-rust>`__
and `pyo3 <https://github.com/PyO3/pyo3>`__.
As such source installations of Portmod requires a rust compiler (1.58+).
If you are installing using a
pre-compiled wheel from pypi (which, as long as a wheel for your
platform is available, is usually what is installed when using pip), you
do not need a rust compiler to install.

https://www.rust-lang.org/tools/install

Python Dependencies
-------------------

Can be installed through pip, or via your package manager. When
installing using the pip commands given later in this file these will be
installed automatically.

-  patool: http://wummel.github.io/patool/

   -  Archive manager
   -  Note that patool relies on helper programs to handle may file
      types, you will need these programs installed and in your PATH to
      be able to extract files of types not supported natively by patool
      (built-in types include TAR, ZIP, BZIP2 and GZIP). Archive types
      encountered by Portmod vary, but you probably want to have tools
      that can handle at least RAR, 7z and XZ archives.

-  colorama
-  black
-  GitPython
-  progressbar2 >= 3.2
-  pywin32 - Windows only
-  RestrictedPython >= 4.0
-  redbaron
-  python-sat
-  requests
-  chardet
-  importlib_metadata (for python 3.7)
-  packaging
-  fasteners >= 0.16
-  argcomplete (optional)

Documentation
~~~~~~~~~~~~~

Portmod also includes sphinx documentation. This can produce a number of different output formats. On Linux and macOS, portmod will build man pages if sphinx and sphinx-argparse are available.

To build other formats, you can use `sphinx-build` within the `doc` directory, or invoke `sphinx-build` via the included Makefile.

E.g.

.. code:: bash

    make -C doc html man

- sphinx
- sphinx-argparse
- sphinx_rtd_theme (html only)
- sphinx-autodoc-typehints (html only)


Installation Methods
--------------------

Also see the following pages for platform-specific installation information

.. toctree::

   linux
   macos
   windows

Package Manager
~~~~~~~~~~~~~~~

The recommended way of installing portmod is to install it through your
system package manager, if possible.

|Packaging status|

Pip
~~~

If your system package manager doesn’t include portmod, you can also
install via pip. Note that the ``--upgrade`` flag is used to ensure that
you have the latest version.

::

   pip3 install portmod --upgrade

Development Version
~~~~~~~~~~~~~~~~~~~

The recommended way to install the development version of Portmod is by
pointing pip directly at the repository. Note that this version may be
more unstable than the releases.

::

   pip3 install git+https://gitlab.com/portmod/portmod

If you want to make changes to portmod, you probably want to instead
create a local clone of the git repository and work with that version.
See :ref:`dev-setup` for details.

Command Line Completion
-----------------------

Portmod supports command line tab completion using
`argcomplete <https://github.com/kislyuk/argcomplete>`__. Since Portmod
uses entry points, the global autocompletion used by argcomplete doesn’t
work, so you need to register scripts individually by including the
following line in ``~/.bashrc``.

.. code:: bash

   eval "$(register-python-argcomplete portmod)"

Other Supported shells include (see `argcomplete
readme <https://github.com/kislyuk/argcomplete>`__ for details):

- zsh
- tcsh
- fish
- git bash (I.e. for Windows. Requires additional configuration compared to regular bash shells)

.. |Packaging status| image:: https://repology.org/badge/vertical-allrepos/portmod.svg
   :target: https://repology.org/project/portmod/versions

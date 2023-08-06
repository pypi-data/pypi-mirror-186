User Configuration
------------------

These files are found in the ``CONFIG_DIR`` (as displayed by ``portmod <prefix> info``).
This is typically one of the following locations, depending on your platform.

.. list-table::
   :widths: 15 85

   * - Linux
     - ``~/.config/portmod/<prefix>``
   * - Windows
     - ``C:\Documents and Settings\<User>\Application Data\Local Settings\portmod\portmod\<prefix>``
       or
       ``C:\Documents and Settings\<User>\Application Data\portmod\portmod\<prefix>``

.. toctree::
   :maxdepth: 2

   package.accept_license
   package.accept_keywords
   package.mask
   package.use
   portmod.conf
   profile
   repos.cfg
   sets

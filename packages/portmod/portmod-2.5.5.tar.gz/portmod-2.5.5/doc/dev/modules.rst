.. _modules:

=======
Modules
=======

Modules can be used to apply global updates, or other configuration which
needs to be done more frequently than just at package installation.
This commonly takes the form of updating configuration files.

Modules can also provide interfaces for the user to manually configure their system.

Modules are python files, similar to pybuilds, and contain functions of
the form ``do_{name}`` or ``describe_{name}``, where name is the name of
the operation. Do variants should execute the function, while describe
should return a string which describes the operation.

They use the ``.pmodule`` extension.

Installation
------------

Modules must be installed into the ``MODULEPATH`` for them to be activated.

Special Functions
-----------------

The ``update`` operation is invoked by default (if present) after
installation or removal of mods. It is recommended that update not
produce any output unless changes are necessary. Other helper functions
can be included, but will not have any special meaning.

The ``prerm`` operation is invoked before the module is removed from the
system. Any changes made should be reverted if possible.

Functions of the form ``describe_{name}``, ``describe_{name}_options`` and
``describe_{name}_parameters`` can also be used to describe functions and their
parameters. ``describe_{name}`` should return a single string describing the
function (prior to portmod 2.5 this was specified in the doc string), and the
others should each return a list of strings, one for each
parameter, with ``describe_{name}_options`` listing argument names,
and ``describe_{name}_parameters`` listing the corresponding argument
descriptions. Unlike ``update`` and the ``do_*`` functions, ``describe_*``
functions have the same restrictions as global scope code (i.e. no using
imported objects, file i/o, etc. See :ref:`sandbox`).

Module Description
------------------

Module files which contain operations other than update must also
contain a docstring, which is used to describe the module when invoking
``portmod <prefix> select``.

Function arguments
------------------

Module functions take up to two arguments: ``state``, which is an object
with a number of constants that describe the module’s environment, and
``args``, which contains the arguments passed by the user (if any), in
the form of an object.

-  ``do_update`` only gets passed the ``state`` and is not provided with
   args.
-  All other ``do_`` functions are provided both ``state`` and ``args``.

Note that functions expecting too many or too few arguments will case
runtime exceptions.

Module state
------------

New constants may be introduced, however they will not be removed
between major versions of Portmod.

Valid variables include:

+-------------------------------+---------------------------------------+
| Name                          | Value                                 |
+===============================+=======================================+
| ROOT                          | The root of the module’s installed    |
|                               | tree. This location can be used to    |
|                               | store custom files which are designed |
|                               | to be used at runtime (e.g. patches)  |
+-------------------------------+---------------------------------------+
| CACHE                         | A directory that can be used to cache |
|                               | temporary files between runs. It is   |
|                               | not guaranteed to persist, however    |
|                               | its contents are not automatically    |
|                               | deleted                               |
+-------------------------------+---------------------------------------+
| TEMP                          | A directory which can be used to      |
|                               | store temporary files during module   |
|                               | execution. This directory and all     |
|                               | files will be removed after the       |
|                               | module has finished executing         |
+-------------------------------+---------------------------------------+
| VERSION                       | The currently installed version       |
|                               | number of the module. Useful for      |
|                               | determining if information needs to   |
|                               | be regenerated due to an update to    |
|                               | the module itself                     |
+-------------------------------+---------------------------------------+

Sandbox
-------

Module files execute within the :ref:`sandbox`.

File access is only permitted within the ``ROOT``, ``CACHE`` and ``TEMP``
directories passed in the state objects (see above).

The python module ``portmod.module_util`` provides access to two helper
functions:

1. ``execute(command)``: Permits execution of binaries. The interface is
   the same as the `pybuild.Pybuild2.execute` function.
2. ``create_file(path)``: Permits access to arbitrary files on the
   filesystem via redirection. This returns a path to a file within a
   temporary directory, and the user will be shown the difference
   between the existing file and the contents of this new file and
   prompted to allow the changes to proceed after the module is done
   executing.

Example module
--------------

.. code:: python

   """Shopping list module"""
   import os

   def do_update(state):
       """This function isn't actually necessary here. We're not updating anything"""

   def describe_list():
       return "Displays shopping list"

   def do_list(state, args):
       """Displays shopping list"""
       path = os.path.join(state.ROOT, "shopping.txt")
           if os.path.exists(path):
               with open(path, "r") as file:
                   for line in file.readlines():
                       print(line)

       # Essentials!
       print("Eggs")
       print("Milk")
       print("Carrots")
       print("Marmite")
       print("Hackle-lo leaves")

   def describe_add():
       return "Add to list"

   def do_add(state, args):
       """Add to list"""
       with open(os.path.join(state.ROOT, "shopping.txt"), "a") as file:
           print(args.item, file)

   def describe_add_options():
       return ["item"]

   def describe_add_parameters():
       return ["item to add to the list"]

*Note: while it may be possible to use Portmod for shopping lists, this
is outside the scope of the project and is not something which is
officially supported. The above is provided as an example of the format
only.*

Notes
-----

Like Pybuilds, global scope code is not permitted!
Modules must be sourced to get information such as descriptions when running
``portmod <prefix> select``, and global code running at this point would
be undesirable.

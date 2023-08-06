.. _metadata.yaml:

=============
metadata.yaml
=============

metadata.yaml files are used to store additional information about mods
and categories. Note that no information stored in metadata.yaml should
be specific to a particular version of a mod.

+-----------------------------------+-----------------------------------+
| Key                               | Value                             |
+===================================+===================================+
| longdescription                   | Description of the mod or         |
|                                   | category.                         |
+-----------------------------------+-----------------------------------+
| maintainer                        | Maintainer, or list of            |
|                                   | maintainers for the package in    |
|                                   | the form of Person (email is      |
|                                   | required, name and desc are       |
|                                   | optional) or Group                |
+-----------------------------------+-----------------------------------+
| use                               | Use flags and their descriptions. |
|                                   | Key is the flag name, value is    |
|                                   | the description                   |
+-----------------------------------+-----------------------------------+
| upstream                          | Description of the mod’s upstream |
|                                   | information. Is a dictionary with |
|                                   | one or more of the entries listed |
|                                   | in the table below                |
+-----------------------------------+-----------------------------------+
| tags                              | A set of tags which describe this |
|                                   | package.                          |
|                                   | These tags are primarily used by  |
|                                   | the search indexer, and may be    |
|                                   | used by external software to      |
|                                   | categorise packages.              |
+-----------------------------------+-----------------------------------+

Upstream contents
-----------------

+-----------------------------------+-----------------------------------+
| Key                               | Value                             |
+===================================+===================================+
| maintainer                        | maintainers/authors of the        |
|                                   | original mod. Must be either a    |
|                                   | Person or a list of Person with a |
|                                   | name attribute and/or an email    |
|                                   | attribute.                        |
+-----------------------------------+-----------------------------------+
| changelog                         | URL where a changelog for the mod |
|                                   | can be found. Must be version     |
|                                   | independent                       |
+-----------------------------------+-----------------------------------+
| doc                               | URL where the location of the     |
|                                   | upstream documentation can be     |
|                                   | found. The link must not point to |
|                                   | any third party documentation and |
|                                   | must be version independent       |
+-----------------------------------+-----------------------------------+
| bugs-to                           | A place where bugs can be         |
|                                   | reported in the form of an URL or |
|                                   | an e-mail address prefixed with   |
|                                   | ``mailto:``                       |
+-----------------------------------+-----------------------------------+

Person
------

+-----------------------------------+-----------------------------------+
| Key                               | Value                             |
+===================================+===================================+
| name                              | Name of maintainer                |
+-----------------------------------+-----------------------------------+
| email                             | email address of maintainer       |
+-----------------------------------+-----------------------------------+
| desc                              | Can be used to note details about |
|                                   | the current maintainership E.g.   |
|                                   | Willing to pass this off to       |
|                                   | someone else                      |
+-----------------------------------+-----------------------------------+

E.g.

.. code:: yaml

   name: foo
   email: foo@example.org
   # If provided with one argument, that argument is the name of the maintainer
   # The person tag can be omitted and a string can be provided instead,
   # in which case the string is treated as the maintainer's name,
   # with email optionally following in angle brackets.
   baz <foo@example.org>
   # Note that maps can also be written in a single line using braces:
   { name: foo, email: foo@example.org }

Groups
~~~~~~

===== ========================================================
Key   Value
===== ========================================================
group Group identifier (as listed in ``metadata/groups.yaml``)
===== ========================================================

E.g.

.. code:: yaml

   group: foo
   # Note that the groups cannot be provided as just a string,
   # as strings are treated as person maintainers

Mod Metadata
------------

Example

.. code:: yaml

   maintainer:
       - name: foo
         email: foo@example.org
         desc: E.g. Willing to pass this off to someone else
       - group: Group name, as defined in metadata/groups.yaml
   longdescription: "Long mod description. Can be multiple lines long, but
   should not contain version-specific information.
   That being said, confine this to a general description only and link to
   upstream documentation rather than put extremely large amounts of detail
   in this string"
   use:
       flag: description of flag
       otherflag: description
   upstream:
       maintainer:
           name: foo
           email: foo@example.org
       changelog: http://doc.example.org/changelog
       doc: http://doc.example.org/doc
       bugs-to: mailto:foo@example.org

Category Metadata
-----------------

Example

.. code:: yaml

   longdescription: The patches category contains mods that combine information from other mods to build a patch.

When categories are created, a metadata.yaml containing a
longdescription is required.

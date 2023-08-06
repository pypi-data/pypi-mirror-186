Package Names and Versions
==========================

.. note::
   Valid characters are displayed as a regular expression, so that they
   can be concisely specified while still being exhaustive. Brackets (``[]``)
   are part of the regex and are not considered valid characters in any context.

Category Names
--------------

A category name may contain any of the characters ``[A-Za-z0-9+_.-]``.
It must not begin with a hyphen, a dot or a plus sign.

For consistency, the :ref:`Naming Guidelines <guidelines-naming>` for
packages should also be followed for categories.

Package Names
-------------

A package name may contain any of the characters ``[A-Za-z0-9+_-]``.
It must not begin with a hyphen or a plus sign, and must not end in a
hyphen followed by anything matching the :ref:`version-syntax`.

Also see :ref:`Naming Guidelines <guidelines-naming>`.

.. note::
   A package name does not include the category.
   The term qualified package name is used where a category/package pair is meant.

USE flag names
--------------
A USE flag name may contain any of the characters ``[A-Za-z0-9+_-]``.
It must begin with an alphanumeric character.

Underscores should be considered reserved for USE_EXPAND, as described
in the :ref:`use-expand` section of the USE flag guide.

Repository Names
----------------
A repository name may contain any of the characters ``[A-Za-z0-9_-]``.
It must not begin with a hyphen.
In addition, every repository name must also be a valid package name.

License Names
-------------

A license name may contain any of the characters ``[A-Za-z0-9+_.-]``.
It must not begin with a hyphen, a dot or a plus sign.

Keyword names
-------------

A keyword name may contain any of the characters ``[A-Za-z0-9_-]``.
It must not begin with a hyphen.
In contexts where it makes sense to do so, a keyword name may be prefixed by a tilde or a hyphen.
In :py:attr:`pybuild.Pybuild2.KEYWORDS`, -* is also acceptable as a keyword.

.. _version-syntax:

Version Syntax
--------------

A version may optionally begin with an epoch, in the form ``[0-9]+-`` (One or more digits followed by a hyphen). This epoch is a packaging-only component used to indicate that a package has changed to a new versioning system which is incompatible with the old versioning system. If the epoch is omitted, the version is considered to be epoch 0.

A version starts with the number part, which is in the form ``[0-9]+(\.[0-9]+)*`` (an unsigned integer, followed by zero or more dot-prefixed unsigned integers). E.g. ``1.2.3``

This may optionally be followed by one of ``[a-z]`` (a lowercase letter).

This may be followed by zero or more of the suffixes ``_alpha``, ``_beta``, ``_pre``, ``_rc`` or ``_p``,
each of which may optionally be followed by an unsigned integer.
Suffix and integer count as separate version components.

This may optionally be followed by the suffix ``-r`` followed immediately by an unsigned integer (the “revision number”, used to indicate changes to the package which require rebuilding, when there are no changes to the upstream project).
If this suffix is not present, it is assumed to be ``-r0``.

E.g. Using all the components: ``2-1.2.3a_alpha12-r3``.

For the version comparison algorithm, see `Section 3.3 of the Package Manager Specification <https://projects.gentoo.org/pms/7/pms.html#x1-260003.3>`_. Note that epochs are not included in that algorithm, but are checked first and the package with the larger epoch is always the greater version.

External Resources
------------------

Ignoring slots, Portmod's version specifiers are identical to Portage's version specifiers. The following Gentoo resources may be helpful.

- https://wiki.gentoo.org/wiki/Version_specifier
- https://devmanual.gentoo.org/ebuild-writing/file-format/index.html#file-naming-rules.

Portmod's package names and versions generally follow `Section 3 of the Package Manager Specification <https://projects.gentoo.org/pms/7/pms.html#x1-150003>`_, with some exceptions. Excerpts of this section have been copied verbatim and are licensed `CC-BY-SA-3.0 <http://creativecommons.org/licenses/by-sa/3.0/>`_.

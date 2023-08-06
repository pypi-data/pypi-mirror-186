.. _layout.conf:

===========
layout.conf
===========

Describes the repository metadata.

E.g.

.. code-block:: python

    # Comments can be included
    masters = "python openmw"

    # 2 is new, so it's not a bad idea to stick with 1 for now
    pybuild_versions_banned = [2]

    # Obviously this isn't helpful if you also include the above statement,
    # But eventually you will want to deprecate Pybuild1 since support for
    # it will be dropped.
    pybuild_versions_deprecated = [1]

Fields
======

masters
~~~~~~~
A space-separated string list of repository masters


pybuild_versions_banned
~~~~~~~~~~~~~~~~~~~~~~~

A python list of banned pybuild versions. E.g. if this list includes ``2``, :py:class:`pybuild.Pybuild2` will be considered banned and will not be able to be loaded. :ref:`inquisitor` will also produce an error for packages which use banned pybuild versions.

This is primarily a QA feature, but is also enforced at runtime.

pybuild_versions_deprecated
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A python list of deprecated pybuild versions. E.g. if this list includes ``2``, :py:class:`pybuild.Pybuild2` will be considered deprecated and :ref:`inquisitor` will emit a warning when encountering packages which use it.


Syntax
======

Same as :ref:`defaults.conf`. I.e. a restricted subset of python using only basic primitives and no imports.

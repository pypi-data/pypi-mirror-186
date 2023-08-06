.. _contributing:

Contributing to Portmod
=======================

There are many different ways you can contribute to Portmod. With the exception of :ref:`l10n`, all of these contributions will require the use of git.

If you are unfamiliar with git you may want to check out the `GitLab Basics Guide <https://docs.gitlab.com/ee/topics/git/>`_.

In particular, you may want to look at:

- `Making your first commit <https://docs.gitlab.com/ee/tutorials/make_your_first_git_commit.html>`_, which guides you through the basics of git, gitlab, and commits.
- `Forking Workflow <https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html>`_, which describes how to use forks to contribute to projects you don't have write access to.

Contributing to Portmod or its subprojects means that you are licensing your contributions under the GPL version 3 or later.

Setting up a local clone
------------------------

You will need to fork the repository you wish to contribute to (look for the fork button in the top right of the project page).

Make a local copy of your fork:

.. code:: bash

   git clone git@gitlab.com:<user>/<repo>.git


Documentation
-------------

Documentation is written using `Sphinx <https://www.sphinx-doc.org>`_ and `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.

All documentation should be written in British English (en-GB). Sphinx documentation can be `internationalised <https://www.sphinx-doc.org/en/master/usage/advanced/intl.html>`_, but this has not yet been set up. If you are interested in contributing translations of the documentation, please open an issue on `the issue tracker <https://gitlab.com/portmod/portmod/-/issues>`_.

Localisation
------------

See :ref:`l10n`

Packaging Mods
--------------

See :ref:`package-development`

Contributing to Portmod's Package Mangager Code
-----------------------------------------------

See :ref:`dev-setup`

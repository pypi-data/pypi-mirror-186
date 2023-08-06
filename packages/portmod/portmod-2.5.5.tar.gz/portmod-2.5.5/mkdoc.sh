#!/bin/bash

rm -r apidoc
sphinx-apidoc -o apidoc . test setup.py -e -H "API"
cd apidoc
rm modules.rst
echo ".. _portmod-api:

Welcome to Portmod's API Documentation
======================================

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   portmod
   portmodlib
   pybuild

Indices and tables
==================

* :ref:\`genindex\`
* :ref:\`modindex\`
* :ref:\`search\`" > index.rst
sphinx-build -c ../doc -b html . _build
RESULT=$?
cd ..
exit $RESULT

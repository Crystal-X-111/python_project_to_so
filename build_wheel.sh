#!/bin/bash

set -e

python3 module_setup.py bdist_wheel

# delete soucecode files from the whl package
# because the sourcecode files have already been built into the so
# and removing them helps protect the code 
zip -d dist/maidabu-*.whl maidabu/bootstrap.py \
  maidabu/main_module.py \
  maidabu/sub_module_a/* \
  maidabu/sub_module_b/* \
  maidabu/utils/*

cp dist/maidabu-*.whl .
rm -r dist
rm -r build
rm -r maidabu.egg-info

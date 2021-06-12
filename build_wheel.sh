#!/bin/bash

set -e

python3 module_setup.py bdist_wheel

zip -d dist/maidabu-*.whl maidabu/bootstrap.py \
  maidabu/main_module.py \
  maidabu/sub_module_a/* \
  maidabu/sub_module_b/* \
  maidabu/utils/*

cp dist/maidabu-*.whl .
rm -r dist
rm -r build
rm -r maidabu.egg-info

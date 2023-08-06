#!/bin/bash
# requires sdist, bdist_wheel, setuptools, and twine to be installed (pip install)
python setup.py sdist bdist_wheel &&
python -m twine upload dist/* --skip-existing

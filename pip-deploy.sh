#!/bin/zsh

sudo rm -rf dist
sudo rm -rf build
sudo rm -rf FairQt.egg-info

python3 setup.py sdist
twine upload dist/*
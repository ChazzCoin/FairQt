#!/bin/zsh

sudo rm -rf dist
sudo rm -rf build
sudo rm -rf FairQt.egg-info

git add .
git commit -m "automated changes"
git push origin main
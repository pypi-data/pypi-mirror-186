#!/usr/bin/env bash

# get enmapbox project
rm -rf context/enmapbox
git clone https://bitbucket.org/hu-geomatics/enmap-box.git ./context/enmapbox
# git clone https://bitbucket.org/hu-geomatics/enmap-box.git --branch develop --single-branch ./context/enmapbox
cd ./context/enmapbox/ || exit
git checkout v3.9  # checkout EnMAP-Box 3.9 which is last version compatible with QGIS 3.18
cd ../..

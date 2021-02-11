#!/bin/bash

## Show command and exit immediately if a command exits with a non-zero status.
set -ex

## Settings (we build essentially a noarch package
PKG_NAME=spectrochempy_data
OS=noarch

## get version string from setuptools_scm
PVS="$(git describe --tags)"
echo "Current version string = $PVS"

## Extract components
IFS=$"-"
read -ra arr <<< "$PVS"

## latest version string
LATEST="${arr[0]}"
IFS=$"."
read -ra tag <<< "$LATEST";

export VERSION="${tag[0]}.${tag[1]}"

export CONDA_BLD_PATH="$HOME/conda-bld"
mkdir -p "$CONDA_BLD_PATH"

## configure conda
conda update -q -n base conda
conda config -q --set anaconda_upload no
conda config -q --set always_yes yes

conda build conda

PKG_NAME_VERSION="$PKG_NAME-$VERSION-0.tar.bz2"
PKG_FILE="$CONDA_BLD_PATH/$OS/$PKG_NAME_VERSION"

echo 'anaconda -t "$CONDA_UPLOAD_TOKEN" upload --force -u "$ANACONDA_USER" "$PKG_FILE";'
anaconda -t "$CONDA_UPLOAD_TOKEN" upload --force -u "$ANACONDA_USER" "$PKG_FILE";

#!/bin/bash

# setup

SCP_DATA_DIR=$HOME/.spectrochempy
mkdir -p $SCP_DATA_DIR

DATA_DIR=$SCP_DATA_DIR//spectrochempy_data/
mkdir -p $DATA_DIR
cp -a $RECIPE_DIR/../testdata/ $DATA_DIR/

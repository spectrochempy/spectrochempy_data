#!/bin/bash
DATA_DIR=$PREFIX/share/spectrochempy_data/
mkdir -p $DATA_DIR

cp -a $RECIPE_DIR/../testdata/ $DATA_DIR/

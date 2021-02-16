
set HOME=%HOMEDRIVE%%HOMEPATH%

set DATA_DIR=%HOME%/.spectrochempy
set SRC_DIR=%CONDA_PREFIX%/share/spectrochempy_data

MOVE %SRC_DIR%/testdata %DATA_DIR%

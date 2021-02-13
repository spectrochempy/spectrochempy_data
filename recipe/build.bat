SET DATA_DIR="%PREFIX%|share\spectrochempy_data"
IF NOT EXIST "%DATA_DIR%" MKDIR "%DATA_DIR%"

XCOPY "%RECIPE_DIR%\..\testdata" "%DATA_DIR%"   /Y /S

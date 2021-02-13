SET DATA_DIR="%PREFIX%|share\spectrochempy_data"
IF NOT EXIST "%DATA_DIR%" MKDIR "%DATA_DIR%"

XCOPY "%RECIPE_DIR%\..\testdata" "%DATA_DIR%"   /Y /S

REM post-link script being not executed on windows this is a try for a workaround
XCOPY "%RECIPE_DIR%\post_link.bat" "%PREFIX%\Script\.spectrochempy_data-post-link.bat"

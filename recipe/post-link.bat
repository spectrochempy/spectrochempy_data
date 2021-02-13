MKLINK /d "%USERPROFILE%\.spectrochempy\testdata" "%PREFIX%\share\spectrochempy_data\testdata"
if %errorlevel% neq 0 exit /b %errorlevel%

SET BINDIR=%~dp0
CD /D "%BINDIR%"
REM tasklist /M python27.dll | find "python"
REM IF ERRORLEVEL 1 (
"C:\Python27\python.exe" run.py
REM )
REM IF ERRORLEVEL 0 (
REM taskkill /im python.exe /f /FI "modules eq python27.dll"
REM )
pause
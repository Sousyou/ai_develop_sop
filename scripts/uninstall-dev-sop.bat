@echo off
setlocal

set "PYTHON_CMD="

python -V >nul 2>&1
if %errorlevel%==0 (
    set "PYTHON_CMD=python"
) else (
    py -3 -V >nul 2>&1
    if %errorlevel%==0 (
        set "PYTHON_CMD=py -3"
    )
)

if not defined PYTHON_CMD (
    echo Could not find Python. Install Python 3 first.
    exit /b 1
)

echo Uninstalling ai-develop-sop
%PYTHON_CMD% -m pip uninstall -y ai-develop-sop
exit /b %ERRORLEVEL%

@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "REPO_ROOT=%SCRIPT_DIR%.."
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

pushd "%REPO_ROOT%" >nul
if /I "%~1"=="editable" (
    echo Installing ai-develop-sop in editable mode from "%CD%"
    %PYTHON_CMD% -m pip install -e .
) else (
    echo Installing ai-develop-sop from "%CD%"
    %PYTHON_CMD% -m pip install .
)
set "EXIT_CODE=%ERRORLEVEL%"
popd >nul

exit /b %EXIT_CODE%

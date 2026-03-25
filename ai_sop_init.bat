@echo off
chcp 65001 >nul
setlocal

set "SOP_ROOT=%~dp0"
set "SCRIPT_FILE=%SOP_ROOT%ai_sop_init.ps1"

if not exist "%SCRIPT_FILE%" (
    echo [ERROR] Missing ai_sop_init.ps1: "%SCRIPT_FILE%"
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_FILE%" -SopRoot "%SOP_ROOT%"
set "EXIT_CODE=%ERRORLEVEL%"

if "%EXIT_CODE%"=="0" (
    echo [DONE] AI SOP project injection init/reset completed.
    exit /b 0
)

echo [ERROR] Init failed with exit code: %EXIT_CODE%
exit /b %EXIT_CODE%

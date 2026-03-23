@echo off
chcp 65001 >nul
setlocal

set "ROOT=%~dp0"
set "AGENTS_FILE=%ROOT%AGENTS.md"
set "SCRIPT_FILE=%ROOT%ai_sop_clear.ps1"

if not exist "%AGENTS_FILE%" (
    echo [ERROR] 未找到 AGENTS.md: "%AGENTS_FILE%"
    exit /b 1
)

if not exist "%SCRIPT_FILE%" (
    echo [ERROR] 未找到 ai_sop_clear.ps1: "%SCRIPT_FILE%"
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_FILE%" -AgentsFile "%AGENTS_FILE%"

set "EXIT_CODE=%ERRORLEVEL%"

if "%EXIT_CODE%"=="0" (
    echo [DONE] 当前项目入口配置区块中的所有入口字段已重置为 None
    exit /b 0
)

if "%EXIT_CODE%"=="2" (
    echo [DONE] AGENTS.md 中没有需要重置的字段
    exit /b 0
)

echo [ERROR] 还原失败，退出码: %EXIT_CODE%
exit /b %EXIT_CODE%

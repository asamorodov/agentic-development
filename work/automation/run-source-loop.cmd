@echo off
setlocal EnableExtensions

set "SCRIPT_DIR=%~dp0"
for %%I in ("%SCRIPT_DIR%..\..") do set "REPO_ROOT=%%~fI"

call "%SCRIPT_DIR%ensure-node-tools.cmd"
if errorlevel 1 exit /b %ERRORLEVEL%

cd /d "%REPO_ROOT%"
call "%SOURCE_AUTOMATION_NODE_MODULES%\.bin\tsx.cmd" "%REPO_ROOT%\work\automation\src\run-source-loop.ts" --repo-root "%REPO_ROOT%" %*
exit /b %ERRORLEVEL%

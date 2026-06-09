@echo off

set "SCRIPT_DIR=%~dp0"
set "TOOL_HOME=%LOCALAPPDATA%\agentic-development-source-automation\node"
if "%LOCALAPPDATA%"=="" set "TOOL_HOME=%TEMP%\agentic-development-source-automation\node"

if not exist "%TOOL_HOME%" mkdir "%TOOL_HOME%" >nul 2>nul

if not exist "%TOOL_HOME%\node_modules\@openai\codex-sdk\package.json" goto install_tools
if not exist "%TOOL_HOME%\node_modules\.bin\tsx.cmd" goto install_tools
goto done

:install_tools
echo Installing source automation Node tools outside repository: %TOOL_HOME%
npm.cmd install --prefix "%TOOL_HOME%" --no-audit --no-fund --no-save tsx@4.20.0 @openai/codex-sdk@0.137.0
if errorlevel 1 exit /b %ERRORLEVEL%

:done
set "SOURCE_AUTOMATION_TOOL_HOME=%TOOL_HOME%"
set "SOURCE_AUTOMATION_NODE_MODULES=%TOOL_HOME%\node_modules"
exit /b 0

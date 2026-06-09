@echo off
setlocal EnableExtensions

set "SCRIPT_DIR=%~dp0"

rem Safe default: continue. This wrapper must not pass fresh/fresh-action.
rem If a story dossier file is missing, create a minimal stub before invoking this wrapper.
call "%SCRIPT_DIR%run-source-loop.cmd" ^
  --backend sdk ^
  --prompt work/prompts/STORY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md ^
  --min-pass 10 ^
  --max-pass 20 ^
  --mode continue ^
  %*

exit /b %ERRORLEVEL%

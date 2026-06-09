@echo off
setlocal EnableExtensions

set "SCRIPT_DIR=%~dp0"

call "%SCRIPT_DIR%run-source-loop.cmd" ^
  --prompt work/prompts/DOSSIER_LANGUAGE_STYLE_NORMALIZATION_PROMPT.md ^
  --min-pass 10 ^
  --max-pass 20 ^
  --mode continue ^
  %*

exit /b %ERRORLEVEL%

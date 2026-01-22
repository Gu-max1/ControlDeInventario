@echo off
title Configuracion de Email
REM Navigate to project root (two levels up from tools\scripts)
cd /d "%~dp0..\.."

REM Use virtual environment Python if available
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" tests/setup_email_config.py
) else (
    python tests/setup_email_config.py
)

pause

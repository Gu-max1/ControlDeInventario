@echo off
title Prueba de Email
REM Navigate to project root (two levels up from tools\scripts)
cd /d "%~dp0..\.."

REM Use virtual environment Python if available
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" tests/test_email_notification.py
) else (
    python tests/test_email_notification.py
)

pause

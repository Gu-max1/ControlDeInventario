@echo off
title Servicio de Notificaciones Email
REM Navigate to project root (two levels up from tools\scripts)
cd /d "%~dp0..\.."

REM Use virtual environment Python if available
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" server/email_monitor_service.py
) else (
    python server/email_monitor_service.py
)

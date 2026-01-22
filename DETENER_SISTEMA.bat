@echo off
REM ==========================================
REM   DETENER SISTEMA - Control de Inventario
REM ==========================================

:: Navigate to project root
cd /d "%~dp0..\.."

:: Use virtual environment Python if available
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" launcher.py stop
) else (
    python launcher.py stop
)

pause

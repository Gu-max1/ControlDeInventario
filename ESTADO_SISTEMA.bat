@echo off
REM ==========================================
REM   ESTADO DEL SISTEMA - Control de Inventario
REM ==========================================

:: Navigate to project root
cd /d "%~dp0..\.."

:: Use virtual environment Python if available
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" launcher.py status
) else (
    python launcher.py status
)

pause

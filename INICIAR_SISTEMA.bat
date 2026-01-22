@echo off
REM ==========================================
REM   INICIAR SISTEMA - Control de Inventario
REM ==========================================

:: Navigate to project root (two levels up from tools\scripts)
cd /d "%~dp0..\.."

:: Use virtual environment Python if available
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" launcher.py start
) else (
    python launcher.py start
)

pause

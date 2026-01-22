@echo off
REM ==========================================
REM   REINICIAR SISTEMA - Control de Inventario
REM ==========================================

:: Navigate to project root
cd /d "%~dp0..\.."

:: Use virtual environment Python if available
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" launcher.py restart
) else (
    python launcher.py restart
)

pause

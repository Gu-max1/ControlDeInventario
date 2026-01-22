@echo off
title Backend Server
REM Navigate to project root (two levels up from tools\scripts)
cd /d "%~dp0..\.."

REM Use virtual environment Python if available
if exist ".venv\Scripts\python.exe" (
    echo Starting Backend with .venv Python...
    ".venv\Scripts\python.exe" -m uvicorn server.main:app --host 0.0.0.0 --port 8001 --reload
) else (
    echo Starting Backend with system Python...
    python -m uvicorn server.main:app --host 0.0.0.0 --port 8001 --reload
)

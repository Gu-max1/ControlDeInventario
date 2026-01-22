@echo off
title Frontend Client
REM Navigate to project root (two levels up from tools\scripts)
cd /d "%~dp0..\.."

REM Add portable Node.js to PATH if exists
if exist "tools\node-v20.11.0-win-x64" (
    echo Using portable Node.js...
    set "PATH=%CD%\tools\node-v20.11.0-win-x64;%PATH%"
)

REM Navigate to client directory and start
cd client
echo Installing dependencies (if needed)...
call npm install
echo Starting Dev Server...
npm run dev

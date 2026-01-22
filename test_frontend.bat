@echo off
title Frontend Test
cd /d "%~dp0"

echo Adding Node.js to PATH...
set "PATH=%CD%\tools\node-v20.11.0-win-x64;%PATH%"

echo Navigating to client directory...
cd client

echo Starting Vite...
npm run dev

pause

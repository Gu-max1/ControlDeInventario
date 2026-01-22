@echo off
setlocal
title CONTROL DE INVENTARIO - ENTERPRISE

:: Cambiar al directorio del script para manejar rutas con espacios
pushd "%~dp0"

cls
echo ===============================================================================
echo   SISTEMA DE CONTROL DE INVENTARIO - ENTERPRISE EDITION
echo ===============================================================================
echo.
echo   Iniciando el Launcher Principal...
echo.

:: 1. Priority: Use Virtual Environment if it exists
if exist ".venv\Scripts\python.exe" (
    echo   [Boot] Usando entorno virtual ^(.venv^)...
    ".venv\Scripts\python.exe" launcher.py
    if errorlevel 1 goto :error
    goto :end
)

:: 2. Fallback: Use system python
echo   [Boot] ADVERTENCIA: No se encontro .venv.
echo   [Boot] Intentando iniciar con python del sistema...
python launcher.py
if errorlevel 1 goto :error
goto :end

:error
echo.
echo   [ERROR] Ocurrio un error durante la ejecucion.
echo.
pause
exit /b 1

:end
popd
if "%1"=="" pause
exit /b 0

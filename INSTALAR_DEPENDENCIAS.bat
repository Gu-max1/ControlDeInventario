@echo off
setlocal
title INSTALACION DE DEPENDENCIAS - ENTERPRISE

:: Ir al root del proyecto correctamente
pushd "%~dp0..\.."

echo ============================================================
echo   CONFIGURACION DE ENTORNO ENTERPRISE (Python 3.11)
echo ============================================================
echo.

:: 1. Crear VENV si no existe
if exist ".venv\Scripts\python.exe" goto :venv_exists

echo [1/4] Creando entorno virtual con Python 3.11...
:: Intentar con py launcher primero
py -3.11 -m venv .venv
if not errorlevel 1 goto :venv_created

echo     'py' launcher fallo o no encontrado. Intentando con 'python' del sistema...
python -m venv .venv
if not errorlevel 1 goto :venv_created

echo [ERROR] No se pudo crear .venv. Asegurate de tener Python 3.11 instalado.
pause
exit /b 1

:venv_created
echo     Entorno creado.
goto :verify_python

:venv_exists
echo [1/4] Entorno virtual ya existe (.venv).

:verify_python
:: 2. Validar Python del VENV
echo.
echo   [INFO] Verificando interprete...
".venv\Scripts\python.exe" -c "import sys; print(f'   - Python activo: {sys.version}')"
if errorlevel 1 (
    echo [ERROR] El entorno virtual parece corrupto.
    pause
    exit /b 1
)

:: 3. Instalar deps Backend
echo.
echo [2/4] Instalando dependencias del Backend desde pyproject.toml...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -e .
if errorlevel 1 (
    echo [ERROR] Fallo instalacion de dependencias.
    pause
    exit /b 1
)

:: 4. Instalar deps Frontend
echo.
echo [3/4] Instalando dependencias del Frontend...
:: Configurar path de node portable si existe
if exist "tools\node-v20.11.0-win-x64" (
    echo     Usando Node.js portable...
    set "PATH=%CD%\tools\node-v20.11.0-win-x64;%PATH%"
)

cd client
call npm install
if errorlevel 1 (
    echo [WARNING] Fallo npm install. Verifica tu instalacion de Node.js o internet.
)
cd ..

echo.
echo [4/4] Limpieza y finalizacion...
echo.
echo ============================================================
echo   INSTALACION COMPLETADA
echo ============================================================
echo.
popd
pause

@echo off
chcp 65001 >nul 2>&1
title Lorde Dark Edit - Launcher
color 0D
cd /d "%~dp0"

echo.
echo ========================================================
echo           LORDE DARK EDIT - INICIANDO...
echo ========================================================
echo.

python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERRO] Python nao encontrado!
    echo Execute INSTALAR_DEPENDENCIAS.bat primeiro.
    pause
    exit /b 1
)

python -c "import PyQt5" >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERRO] Dependencias nao instaladas!
    echo Execute INSTALAR_DEPENDENCIAS.bat primeiro.
    pause
    exit /b 1
)

echo Iniciando aplicativo...
echo.
python src/app.py

if %errorLevel% neq 0 (
    echo.
    echo ========================================================
    echo                    ERRO AO INICIAR
    echo ========================================================
    echo.
    echo 1. Verifique se Python esta instalado
    echo 2. Execute INSTALAR_DEPENDENCIAS.bat
    echo 3. Verifique crash.log para detalhes
    echo.
    pause
)

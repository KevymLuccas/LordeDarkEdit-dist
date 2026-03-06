@echo off
chcp 65001 >nul 2>&1
title LordeDarkEdit - Instalador de Dependencias
color 0A
cd /d "%~dp0"

echo.
echo ========================================================
echo        LORDEDARK EDIT - INSTALADOR DE DEPENDENCIAS
echo ========================================================
echo.

:: Verificar Python
echo [1/3] Verificando Python...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo.
    echo [ERRO] Python nao encontrado!
    echo.
    echo Baixe e instale o Python em: https://www.python.org/downloads/
    echo IMPORTANTE: Marque "Add Python to PATH" durante instalacao!
    echo.
    pause
    exit /b 1
)
echo [OK] Python encontrado!

:: Instalar dependencias Python
echo.
echo [2/3] Instalando dependencias Python...
pip install PyQt5 Pillow opencv-python requests flask numpy --upgrade -q
if %errorLevel% neq 0 (
    echo [AVISO] Algumas dependencias podem ter falhado
) else (
    echo [OK] Dependencias instaladas!
)

:: Verificar FFmpeg
echo.
echo [3/3] Verificando FFmpeg...
where ffmpeg >nul 2>&1
if %errorLevel% neq 0 (
    echo [AVISO] FFmpeg nao encontrado no PATH
    echo.
    echo O app tentara baixar automaticamente, ou voce pode instalar manualmente:
    echo https://ffmpeg.org/download.html
) else (
    echo [OK] FFmpeg encontrado!
)

echo.
echo ========================================================
echo              INSTALACAO CONCLUIDA!
echo ========================================================
echo.
echo Agora execute INICIAR.bat para abrir o aplicativo.
echo.
pause

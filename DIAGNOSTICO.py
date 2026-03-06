#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DIAGNÓSTICO - Lorde Dark Edit
Execute este arquivo para identificar problemas
"""

import sys
import os
import subprocess
from pathlib import Path

print("=" * 60)
print("       DIAGNÓSTICO - LORDE DARK EDIT")
print("=" * 60)
print()

# 1. Verificar Python
print("[1] Versão do Python:")
print(f"    {sys.version}")
print()

# 2. Verificar dependências
print("[2] Verificando dependências...")
deps = {
    'PyQt5': None,
    'cv2': 'opencv-python',
    'PIL': 'Pillow',
    'requests': 'requests'
}

all_ok = True
for module, pkg in deps.items():
    try:
        __import__(module)
        print(f"    ✓ {module} instalado")
    except ImportError:
        print(f"    ✗ {module} NÃO instalado (pip install {pkg or module})")
        all_ok = False
print()

# 3. Verificar FFmpeg
print("[3] Verificando FFmpeg...")
PROJECT_DIR = Path(__file__).parent

ffmpeg_locations = [
    PROJECT_DIR / "tools" / "ffmpeg" / "bin" / "ffmpeg.exe",
    PROJECT_DIR / "src" / "ffmpeg.exe",
    PROJECT_DIR / "ffmpeg.exe",
    PROJECT_DIR / "ffmpeg" / "bin" / "ffmpeg.exe",
]

ffmpeg_found = False
for loc in ffmpeg_locations:
    if loc.exists():
        print(f"    ✓ FFmpeg encontrado: {loc}")
        ffmpeg_found = True
        break

if not ffmpeg_found:
    # Verificar no PATH
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("    ✓ FFmpeg encontrado no PATH do sistema")
            ffmpeg_found = True
    except FileNotFoundError:
        pass

if not ffmpeg_found:
    print("    ✗ FFmpeg NÃO encontrado!")
    print("    SOLUÇÃO: Baixe o FFmpeg de https://ffmpeg.org/download.html")
    print("             e coloque em: tools/ffmpeg/bin/ffmpeg.exe")
print()

# 4. Verificar conexão com API
print("[4] Testando conexão com API de licença...")
try:
    import requests
    r = requests.get("https://lordedigital.vercel.app/api/ping", timeout=10)
    if r.status_code == 200:
        print("    ✓ API está online e respondendo")
    else:
        print(f"    ⚠ API respondeu com código: {r.status_code}")
except requests.exceptions.Timeout:
    print("    ✗ API demorou muito para responder (timeout)")
except requests.exceptions.ConnectionError:
    print("    ✗ Não foi possível conectar à API (verifique sua internet)")
except Exception as e:
    print(f"    ✗ Erro ao conectar: {e}")
print()

# 5. Verificar pasta de vídeos
print("[5] Verificando pasta de vídeos...")
input_folder = PROJECT_DIR / "input_videos"
if input_folder.exists():
    videos = list(input_folder.glob("*.mp4")) + list(input_folder.glob("*.avi")) + \
             list(input_folder.glob("*.mov")) + list(input_folder.glob("*.mkv"))
    print(f"    ✓ Pasta input_videos existe")
    print(f"    → {len(videos)} vídeo(s) encontrado(s)")
    
    if videos and ffmpeg_found:
        print("    → Testando leitura do primeiro vídeo...")
        try:
            import cv2
            cap = cv2.VideoCapture(str(videos[0]))
            if cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    print(f"    ✓ Vídeo '{videos[0].name}' pode ser lido")
                else:
                    print(f"    ✗ Vídeo '{videos[0].name}' não pode ser lido (frame inválido)")
                cap.release()
            else:
                print(f"    ✗ Não foi possível abrir '{videos[0].name}'")
        except Exception as e:
            print(f"    ✗ Erro ao testar vídeo: {e}")
else:
    print("    ✗ Pasta input_videos não existe")
print()

# 6. Verificar crash log
print("[6] Verificando logs de erro...")
crash_log = PROJECT_DIR / "crash.log"
if crash_log.exists():
    with open(crash_log, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if content.strip():
        print("    ⚠ Encontrado crash.log com erros!")
        print("    → Últimas linhas:")
        lines = content.strip().split('\n')
        for line in lines[-10:]:
            print(f"      {line}")
    else:
        print("    ✓ Nenhum erro no crash.log")
else:
    print("    ✓ Nenhum crash.log encontrado")
print()

# Resumo
print("=" * 60)
print("                      RESUMO")
print("=" * 60)

if not ffmpeg_found:
    print("❌ PROBLEMA PRINCIPAL: FFmpeg não encontrado!")
    print("   SOLUÇÃO: Baixe o FFmpeg e coloque em tools/ffmpeg/bin/")
    print()

if not all_ok:
    print("❌ PROBLEMA: Algumas dependências estão faltando!")
    print("   SOLUÇÃO: Execute 'pip install -r requirements.txt'")
    print()

if ffmpeg_found and all_ok:
    print("✓ Sistema parece estar configurado corretamente.")
    print("  Se o problema persistir, verifique:")
    print("  - Se os vídeos estão em formato compatível (MP4, AVI, MOV)")
    print("  - Se há espaço suficiente em disco")
    print("  - Se o antivírus não está bloqueando")
print()

input("Pressione ENTER para fechar...")

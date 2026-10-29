@echo off
setlocal
title CyberLab Windows
pushd "%~dp0"
if errorlevel 1 exit /b 1

py -3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if not errorlevel 1 goto use_py
python -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if not errorlevel 1 goto use_python

echo Python 3.10 ou superior nao encontrado.
echo Instale o Python em https://www.python.org/downloads/ e reabra o terminal.
echo Sem Python, voce ainda pode abrir index.html diretamente no navegador.
popd
pause
exit /b 1

:use_py
py -3 lab.py --open
set "CYBERLAB_EXIT=%ERRORLEVEL%"
goto finish

:use_python
python lab.py --open
set "CYBERLAB_EXIT=%ERRORLEVEL%"

:finish
popd
if not "%CYBERLAB_EXIT%"=="0" pause
exit /b %CYBERLAB_EXIT%

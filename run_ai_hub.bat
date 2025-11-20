@echo off
REM AI Hub Launcher and Troubleshooter
REM This script starts the AI Hub application with built-in diagnostics

setlocal enabledelayedexpansion
title AI Hub - Launcher & Troubleshooter
color 0A

cls
echo ============================================================
echo                    AI HUB - LAUNCHER
echo ============================================================
echo.

REM Set the project directory
set PROJECT_DIR=D:\AI-HUB 2 Claude
cd /d "%PROJECT_DIR%" || (
    echo ERROR: Could not change to project directory: %PROJECT_DIR%
    pause
    exit /b 1
)

echo [*] Starting diagnostics...
echo.

REM Check if Python is installed
echo [+] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo [ERROR] Python is not installed or not in PATH!
    echo [*] Please install Python 3.10+ from https://www.python.org
    echo.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo [OK] %PYTHON_VERSION% found
echo.

REM Check if pip is available
echo [+] Checking pip...
pip --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo [ERROR] pip is not available!
    pause
    exit /b 1
)
echo [OK] pip is available
echo.

REM Check if ai-hub package is installed
echo [+] Checking if ai-hub is installed...
pip show ai-hub >nul 2>&1
if errorlevel 1 (
    color 0C
    echo [ERROR] ai-hub package not found!
    echo [*] Attempting to install ai-hub from current directory...
    echo.
    pip install -e . --upgrade
    if errorlevel 1 (
        color 0C
        echo [ERROR] Failed to install ai-hub!
        pause
        exit /b 1
    )
    color 0A
    echo [OK] ai-hub installed successfully
) else (
    echo [OK] ai-hub is installed
)
echo.

REM Check if PySide6 is installed
echo [+] Checking PySide6...
python -c "import PySide6; print('OK')" >nul 2>&1
if errorlevel 1 (
    color 0C
    echo [ERROR] PySide6 not found!
    echo [*] Installing PySide6...
    pip install PySide6 --upgrade
    if errorlevel 1 (
        echo [ERROR] Failed to install PySide6!
        pause
        exit /b 1
    )
)
echo [OK] PySide6 is available
echo.

REM Check if other dependencies are installed
echo [+] Checking other dependencies...
python -c "import requests, keyboard, win32api" >nul 2>&1
if errorlevel 1 (
    echo [!] Some dependencies might be missing, installing...
    pip install requests keyboard pywin32 --upgrade >nul 2>&1
    echo [OK] Dependencies updated
) else (
    echo [OK] All dependencies are available
)
echo.

REM Check if config file exists
echo [+] Checking configuration...
if not exist "%PROJECT_DIR%\src\ai_hub\config.py" (
    color 0C
    echo [ERROR] Config file not found at src\ai_hub\config.py
    pause
    exit /b 1
)
echo [OK] Configuration file found
echo.

REM All checks passed
color 0B
echo ============================================================
echo         All checks passed! Starting AI Hub...
echo ============================================================
echo.
timeout /t 2 /nobreak

REM Start the application
color 0A
echo [+] Launching AI Hub...
echo.

python -m ai_hub.app

REM Handle exit code
if errorlevel 1 (
    color 0C
    echo.
    echo [ERROR] Application encountered an error (Exit Code: %errorlevel%)
    echo.
    echo Troubleshooting tips:
    echo 1. Check if all dependencies are installed: pip install -e .
    echo 2. Try updating PySide6: pip install PySide6 --upgrade
    echo 3. Check the error message above for more details
    echo.
) else (
    color 0B
    echo.
    echo [OK] AI Hub closed successfully
    echo.
)

echo ============================================================
echo Press Enter to close this window...
echo ============================================================
pause


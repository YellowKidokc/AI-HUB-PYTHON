@echo off
title AI Hub Startup - Checking Dependencies
color 0A
cls
echo.
echo ========================================
echo    AI HUB - STARTUP CHECKER
echo ========================================
echo.
echo [32mAll systems checking...[0m
echo.

REM Change to AI Hub directory
cd /d "%~dp0"
echo [1/5] Current Directory: %CD%
echo.

REM Check if Python is installed
echo [2/5] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo ❌ ERROR: Python is not installed or not in PATH!
    echo.
    echo TROUBLESHOOTING:
    echo   1. Install Python from https://www.python.org/downloads/
    echo   2. Make sure to check "Add Python to PATH" during installation
    echo   3. Restart your computer after installing
    echo.
    pause
    exit /b 1
)
python --version
echo ✅ Python found!
echo.

REM Check if virtual environment exists
echo [3/5] Checking for required packages...
pip show PySide6 >nul 2>&1
if %errorlevel% neq 0 (
    color 0E
    echo.
    echo ⚠️  WARNING: Some packages are missing!
    echo.
    echo Would you like to install/update all packages now?
    echo This may take a few minutes...
    echo.
    choice /C YN /M "Install missing packages"
    if errorlevel 2 goto skip_install
    if errorlevel 1 goto do_install
)

:do_install
echo.
echo [4/5] Installing/Updating packages...
echo This may take a moment...
echo.
pip install --upgrade pip
pip install -e .
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo ❌ ERROR: Package installation failed!
    echo.
    echo TROUBLESHOOTING:
    echo   1. Check your internet connection
    echo   2. Try running as Administrator
    echo   3. Check if antivirus is blocking pip
    echo   4. Try: pip install --upgrade pip
    echo.
    pause
    exit /b 1
)
echo ✅ Packages installed successfully!
echo.
goto start_app

:skip_install
echo.
echo ⚠️  Skipping package installation...
echo App may not work correctly if packages are missing!
echo.

:start_app
echo [5/5] Starting AI Hub...
echo.
color 0A
echo ========================================
echo    LAUNCHING AI HUB
echo ========================================
echo.
echo TIP: Closing the window minimizes to system tray
echo      Hotkeys will continue to work in background
echo      Right-click tray icon to fully exit
echo.
echo Press Ctrl+C to stop the application
echo.

REM Start AI Hub
python -m ai_hub.main

REM If app crashes, show error
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo ========================================
    echo    ❌ AI HUB CRASHED!
    echo ========================================
    echo.
    echo TROUBLESHOOTING:
    echo   1. Check the error messages above
    echo   2. Make sure all packages are installed: pip install -e .
    echo   3. Check settings.ini for valid API key
    echo   4. Try running: python -m ai_hub.main directly
    echo   5. Check if port 8080 is already in use
    echo.
    echo Common Issues:
    echo   - Missing API key: Edit settings.ini
    echo   - Import errors: Run pip install -e . again
    echo   - Permission errors: Run as Administrator
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo    AI HUB CLOSED NORMALLY
echo ========================================
echo.
pause

@echo off
title AI Hub - Remove Auto-Start
color 0E
echo.
echo ========================================
echo    AI HUB - REMOVE AUTO-START
echo ========================================
echo.
echo This will remove AI Hub from Windows Startup.
echo.
pause

REM Get the startup folder path
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SHORTCUT_PATH=%STARTUP_FOLDER%\AI Hub.lnk"

echo.
echo Checking for shortcut...
echo Path: %SHORTCUT_PATH%
echo.

if exist "%SHORTCUT_PATH%" (
    del "%SHORTCUT_PATH%"
    if %errorlevel% equ 0 (
        color 0A
        echo ✅ Auto-start removed successfully!
        echo AI Hub will no longer start automatically.
    ) else (
        color 0C
        echo ❌ Failed to remove shortcut.
        echo Try running as Administrator.
    )
) else (
    color 0E
    echo ⚠️  Auto-start shortcut not found.
    echo AI Hub is not set to auto-start.
)

echo.
pause

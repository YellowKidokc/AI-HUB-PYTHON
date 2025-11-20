@echo off
title AI Hub - Setup Auto-Start
color 0B
echo.
echo ========================================
echo    AI HUB AUTO-START SETUP
echo ========================================
echo.
echo This will add AI Hub to Windows Startup
echo so it launches automatically when you log in.
echo.
echo Current directory: %~dp0
echo.
pause

REM Get the startup folder path
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
echo.
echo Startup folder: %STARTUP_FOLDER%
echo.

REM Create a shortcut to the startup script
set "SHORTCUT_PATH=%STARTUP_FOLDER%\AI Hub.lnk"
set "TARGET_PATH=%~dp0startup_ai_hub.bat"

echo Creating shortcut...
echo Target: %TARGET_PATH%
echo.

REM Use PowerShell to create shortcut
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%SHORTCUT_PATH%'); $SC.TargetPath = '%TARGET_PATH%'; $SC.WorkingDirectory = '%~dp0'; $SC.WindowStyle = 1; $SC.Description = 'AI Hub - Auto-start on Windows login'; $SC.Save()"

if %errorlevel% equ 0 (
    color 0A
    echo.
    echo ========================================
    echo    ✅ SUCCESS!
    echo ========================================
    echo.
    echo AI Hub will now start automatically when you log in!
    echo.
    echo The startup script will:
    echo   ✓ Check Python installation
    echo   ✓ Verify all packages are installed
    echo   ✓ Offer to update packages if needed
    echo   ✓ Show troubleshooting if errors occur
    echo   ✓ Launch AI Hub
    echo.
    echo To disable auto-start:
    echo   1. Press Win+R
    echo   2. Type: shell:startup
    echo   3. Delete "AI Hub.lnk"
    echo.
    echo Or run: remove_autostart.bat
    echo.
) else (
    color 0C
    echo.
    echo ========================================
    echo    ❌ FAILED!
    echo ========================================
    echo.
    echo Could not create startup shortcut.
    echo.
    echo TROUBLESHOOTING:
    echo   1. Run this script as Administrator
    echo   2. Check if startup folder exists
    echo   3. Try manually:
    echo      - Press Win+R
    echo      - Type: shell:startup
    echo      - Create shortcut to startup_ai_hub.bat
    echo.
)

pause

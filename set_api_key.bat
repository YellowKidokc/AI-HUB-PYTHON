@echo off
title AI Hub - Set API Key
color 0B
echo.
echo ========================================
echo    AI HUB - API KEY SETUP
echo ========================================
echo.
echo This will help you set your OpenAI API key.
echo.
echo First, get your API key from:
echo https://platform.openai.com/api-keys
echo.
pause
echo.
echo ========================================
echo.
set /p API_KEY="Paste your API key here (starts with sk-): "
echo.

if "%API_KEY%"=="" (
    color 0C
    echo.
    echo ❌ ERROR: No API key entered!
    echo.
    pause
    exit /b 1
)

if not "%API_KEY:~0,3%"=="sk-" (
    color 0E
    echo.
    echo ⚠️  WARNING: API key should start with 'sk-'
    echo Are you sure this is correct?
    echo.
    pause
)

echo.
echo Updating settings.ini...
echo.

REM Backup settings.ini
if exist settings.ini (
    copy settings.ini settings.ini.backup >nul
    echo ✅ Backup created: settings.ini.backup
)

REM Update the API key line
powershell -Command "(Get-Content settings.ini) -replace 'api_key = .*', 'api_key = %API_KEY%' | Set-Content settings.ini"

if %errorlevel% equ 0 (
    color 0A
    cls
    echo.
    echo ========================================
    echo    SUCCESS!
    echo ========================================
    echo.
    echo [32mAPI key has been set in settings.ini[0m
    echo.
    echo [32mNext steps:[0m
    echo   1. Restart AI Hub
    echo   2. Try the Chat tab
    echo   3. All AI features should now work!
    echo.
    echo [32mThe API key is UNIVERSAL and works for:[0m
    echo   [32m✓[0m Chat
    echo   [32m✓[0m Spelling (Ctrl+Space)
    echo   [32m✓[0m Prompts (Ctrl+Alt+P)
    echo   [32m✓[0m AI Shortcuts
    echo   [32m✓[0m Hotstrings (;fix, ;clar, etc.)
    echo.
    echo [42m ALL SYSTEMS GREEN - READY TO GO! [0m
    echo.
) else (
    color 0C
    cls
    echo.
    echo ========================================
    echo    ERROR!
    echo ========================================
    echo.
    echo [31mFailed to update settings.ini[0m
    echo.
    echo Please manually edit settings.ini and replace:
    echo   api_key = sk-your-api-key-here
    echo With:
    echo   api_key = %API_KEY%
    echo.
    echo [41m MANUAL FIX REQUIRED [0m
    echo.
)

pause

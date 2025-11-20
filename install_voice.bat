@echo off
REM Install Voice Features for AI Hub
REM This installs TTS and STT capabilities

title AI Hub - Voice Features Installer
color 0B

cls
echo ============================================================
echo           AI HUB - VOICE FEATURES INSTALLER
echo ============================================================
echo.
echo This will install voice capabilities:
echo   - Text-to-Speech (edge-tts)
echo   - Speech-to-Text (faster-whisper)
echo   - Audio recording and playback
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause >nul

echo.
echo [*] Installing voice dependencies...
echo.

pip install edge-tts faster-whisper sounddevice scipy numpy pygame

if errorlevel 1 (
    color 0C
    echo.
    echo [ERROR] Installation failed!
    echo.
    echo Troubleshooting:
    echo 1. Make sure Python and pip are installed
    echo 2. Try running as Administrator
    echo 3. Check your internet connection
    echo.
    pause
    exit /b 1
)

color 0A
echo.
echo ============================================================
echo         VOICE FEATURES INSTALLED SUCCESSFULLY!
echo ============================================================
echo.
echo Next steps:
echo 1. Launch AI Hub: run_ai_hub.bat
echo 2. Open the "Voice" tab
echo 3. Test TTS: Type text and click "Speak"
echo 4. Test STT: Click "Record" or select an audio file
echo.
echo Read VOICE_SETUP_GUIDE.md for detailed instructions.
echo.
pause

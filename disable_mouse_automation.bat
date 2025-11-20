@echo off
echo ========================================
echo   Disable Mouse Automation
echo ========================================
echo.
echo This will disable mouse automation features.
echo The app will still work, just without mouse clicking.
echo.
pause

echo.
echo Uninstalling pyautogui...
pip uninstall pyautogui -y

echo.
echo ========================================
echo   Mouse Automation Disabled!
echo ========================================
echo.
echo Changes:
echo - Mouse click shortcuts will not work
echo - Position Recorder will show "unavailable"
echo - All other features work normally
echo.
echo To re-enable, run: pip install pyautogui
echo.
pause

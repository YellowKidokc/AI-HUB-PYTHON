@echo off
REM AI Hub Silent Launcher - No console window
REM This script starts AI Hub in the background

REM Force the script to run from the current folder
cd /d "%~dp0"

REM Run the app silently using pythonw (no console window)
start "" pythonw.exe -m ai_hub.app

REM Exit immediately
exit

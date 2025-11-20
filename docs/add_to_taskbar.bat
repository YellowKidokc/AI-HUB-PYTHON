@echo off
REM Add AI Hub to Taskbar
REM This script creates shortcuts and pins to taskbar

color 0B
title AI Hub - Taskbar Setup

echo.
echo ============================================================
echo              AI Hub - Taskbar Setup
echo ============================================================
echo.
echo This will create shortcuts and add AI Hub to your taskbar.
echo Administrator access is required...
echo.

REM Request admin privileges and run PowerShell script
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "Start-Process powershell.exe -Verb RunAs -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File \"%~dp0setup_taskbar.ps1\"'"

echo.
echo.
echo ============================================================
echo Setup complete! You can now find AI Hub in your taskbar.
echo ============================================================
echo.
pause


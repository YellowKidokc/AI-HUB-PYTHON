# Install AI Hub to Windows Startup
# Run this once to add AI Hub to startup
# Right-click and select "Run with PowerShell"

# Check if running as admin
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object System.Security.Principal.WindowsPrincipal($currentUser)
$isAdmin = $principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERROR: This script must be run as Administrator!" -ForegroundColor Red
    Write-Host "Right-click this file and select 'Run with PowerShell'" -ForegroundColor Yellow
    Pause
    Exit 1
}

$startupFolder = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
$batchFile = "D:\AI-HUB 2 Claude\startup.bat"
$shortcutPath = "$startupFolder\AI Hub.lnk"

if (-not (Test-Path $batchFile)) {
    Write-Host "ERROR: startup.bat not found at $batchFile" -ForegroundColor Red
    Pause
    Exit 1
}

# Create shortcut
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = $batchFile
$Shortcut.WorkingDirectory = "D:\AI-HUB 2 Claude"
$Shortcut.Description = "AI Hub - Starts on login"
$Shortcut.WindowStyle = 1  # Normal window
$Shortcut.Save()

Write-Host "✅ AI Hub has been added to Windows Startup!" -ForegroundColor Green
Write-Host "   Shortcut created at: $shortcutPath" -ForegroundColor Green
Write-Host "" -ForegroundColor Green
Write-Host "   AI Hub will now start automatically when you log in." -ForegroundColor Green
Write-Host "" -ForegroundColor Green
Write-Host "To remove from startup later:" -ForegroundColor Yellow
Write-Host "   1. Open Startup folder: $startupFolder" -ForegroundColor Yellow
Write-Host "   2. Delete 'AI Hub.lnk'" -ForegroundColor Yellow

Pause



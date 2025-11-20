# Add AI Hub to Windows Taskbar
# Run this once to pin AI Hub to taskbar
# Right-click and select "Run with PowerShell"

# Create app shortcut first
$appPath = "D:\AI-HUB 2 Claude\src\ai_hub\app.py"
$desktopPath = "$env:USERPROFILE\Desktop"
$shortcutPath = "$desktopPath\AI Hub.lnk"

# Python launcher path
$pythonLauncher = "$env:LOCALAPPDATA\Microsoft\WindowsApps\python.exe"

# Check if we can find Python
$pythonExe = (Get-Command python -ErrorAction SilentlyContinue).Source
if ($null -eq $pythonExe) {
    $pythonExe = $pythonLauncher
}

Write-Host "Creating AI Hub shortcut..." -ForegroundColor Cyan
Write-Host "Python location: $pythonExe" -ForegroundColor Cyan

# Create the shortcut
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = $pythonExe
$Shortcut.Arguments = "-m ai_hub.app"
$Shortcut.WorkingDirectory = "D:\AI-HUB 2 Claude"
$Shortcut.IconLocation = "C:\Windows\System32\python.exe,0"
$Shortcut.Description = "AI Hub - Productivity assistant"
$Shortcut.WindowStyle = 1
$Shortcut.Save()

Write-Host "✅ Shortcut created on Desktop: AI Hub.lnk" -ForegroundColor Green
Write-Host "" -ForegroundColor Green
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Right-click the 'AI Hub' icon on your Desktop" -ForegroundColor Yellow
Write-Host "  2. Select 'Pin to taskbar'" -ForegroundColor Yellow
Write-Host "" -ForegroundColor Yellow
Write-Host "Then you can delete the Desktop shortcut if you want." -ForegroundColor Yellow

Pause



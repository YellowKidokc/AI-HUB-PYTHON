# AI Hub Taskbar Setup Script
# This script creates shortcuts and attempts to pin AI Hub to the taskbar

param([switch]$RunAsAdmin)

# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

if (-not $isAdmin) {
    Write-Host "This script requires Administrator privileges to pin to taskbar."
    Write-Host "Attempting to restart with elevated privileges..."
    Start-Process powershell.exe -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`" -RunAsAdmin"
    exit
}

Write-Host "================================" -ForegroundColor Cyan
Write-Host "  AI Hub Taskbar Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

$batFile = "D:\AI-HUB 2 Claude\run_ai_hub.bat"
$projectDir = "D:\AI-HUB 2 Claude"
$shortcutName = "AI Hub"

# Verify files exist
if (-not (Test-Path $batFile)) {
    Write-Host "[ERROR] Batch file not found: $batFile" -ForegroundColor Red
    exit 1
}

# Create shortcut in current user's Start Menu
Write-Host "[+] Creating Start Menu shortcut..." -ForegroundColor Green
$startMenuPath = [Environment]::GetFolderPath("StartMenu")
$shortcutPath = Join-Path $startMenuPath "$shortcutName.lnk"

$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $batFile
$shortcut.WorkingDirectory = $projectDir
$shortcut.Description = "AI Hub - AI Assistant Application"
$shortcut.WindowStyle = 1
$shortcut.Save()

Write-Host "[OK] Shortcut created at: $shortcutPath" -ForegroundColor Green
Write-Host ""

# Create Desktop shortcut
Write-Host "[+] Creating Desktop shortcut..." -ForegroundColor Green
$desktopPath = [Environment]::GetFolderPath("Desktop")
$desktopShortcutPath = Join-Path $desktopPath "$shortcutName.lnk"

$shortcutDesktop = $shell.CreateShortcut($desktopShortcutPath)
$shortcutDesktop.TargetPath = $batFile
$shortcutDesktop.WorkingDirectory = $projectDir
$shortcutDesktop.Description = "AI Hub - AI Assistant Application"
$shortcutDesktop.WindowStyle = 1
$shortcutDesktop.Save()

Write-Host "[OK] Desktop shortcut created at: $desktopShortcutPath" -ForegroundColor Green
Write-Host ""

# Attempt to pin to taskbar
Write-Host "[+] Attempting to pin to taskbar..." -ForegroundColor Cyan
try {
    $verb = $null
    $shell = New-Object -ComObject shell.application
    $folder = $shell.Namespace((Split-Path $shortcutPath))
    $item = $folder.ParseName((Split-Path $shortcutPath -Leaf))
    
    # Get the verbs available
    $verbs = $item.Verbs()
    foreach ($v in $verbs) {
        if ($v.Name -match "Pin to Task&bar|Pin to &Start") {
            $v.DoIt()
            Write-Host "[OK] Pinned to taskbar successfully!" -ForegroundColor Green
            $verb = $v
            break
        }
    }
    
    if ($null -eq $verb) {
        Write-Host "[!] Could not automatically pin to taskbar." -ForegroundColor Yellow
        Write-Host "[*] Manual steps:" -ForegroundColor Yellow
        Write-Host "    1. Open Start Menu" -ForegroundColor Yellow
        Write-Host "    2. Find 'AI Hub'" -ForegroundColor Yellow
        Write-Host "    3. Right-click and select 'Pin to taskbar'" -ForegroundColor Yellow
    }
} catch {
    Write-Host "[!] Error pinning to taskbar: $_" -ForegroundColor Yellow
    Write-Host "[*] You can manually pin it: Right-click the shortcut > Pin to taskbar" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "You can now:" -ForegroundColor Green
Write-Host "  1. Search 'AI Hub' in Start Menu and click it" -ForegroundColor Green
Write-Host "  2. Use the Desktop shortcut" -ForegroundColor Green
Write-Host "  3. Pin the shortcut to your taskbar" -ForegroundColor Green
Write-Host ""
Read-Host "Press Enter to close this window"


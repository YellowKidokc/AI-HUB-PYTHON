# 🚀 AI Hub Launch Guide

## Quick Start

### Option 1: Use the Batch File (Recommended)
1. Double-click `run_ai_hub.bat` in your project folder
2. The script will:
   - ✅ Check Python is installed
   - ✅ Verify all dependencies
   - ✅ Install missing packages automatically
   - ✅ Launch AI Hub
   - 🔄 Troubleshoot any issues
   - ⏸️ Wait for you to press Enter before closing

### Option 2: Add to Taskbar (Windows)
1. Right-click on the desktop and select **"Open in Terminal"** (or open PowerShell)
2. Run this command:
   ```powershell
   powershell -ExecutionPolicy Bypass -File "D:\AI-HUB 2 Claude\setup_taskbar.ps1"
   ```
3. Click "Yes" when prompted for administrator access
4. The script will create shortcuts and pin AI Hub to your taskbar

### Option 3: Create Shortcuts Manually
1. Run `create_shortcut.vbs` to create Start Menu and Desktop shortcuts
2. Right-click the shortcut and select **"Pin to taskbar"**

## What the Batch Script Does

### 🔍 Diagnostics
- Checks Python 3.10+ is installed
- Verifies pip is available
- Confirms ai-hub package is installed
- Validates PySide6 and dependencies
- Confirms configuration files exist

### 🛠️ Auto-Repair
If something is missing:
- Automatically installs missing packages
- Updates PySide6 if needed
- Reinstalls dependencies

### ⏸️ Keeps Window Open
- Shows troubleshooting information
- Won't close until you press Enter
- Shows error messages clearly if something fails

## Files Included

| File | Purpose |
|------|---------|
| `run_ai_hub.bat` | Main launcher with diagnostics and troubleshooting |
| `setup_taskbar.ps1` | Creates shortcuts and pins to taskbar (requires admin) |
| `create_shortcut.vbs` | Creates Start Menu and Desktop shortcuts |
| `LAUNCH_GUIDE.md` | This file |

## Troubleshooting

### "Python is not installed or not in PATH"
- Install Python 3.10+ from https://www.python.org
- Make sure to check "Add Python to PATH" during installation

### "PySide6 not found"
- The batch file will automatically install it
- Or manually run: `pip install PySide6 --upgrade`

### "ai-hub package not found"
- The batch file will reinstall it
- Or manually run: `pip install -e .` in the project directory

### Application won't start
- Check the error message in the batch window
- Make sure all dependencies are installed: `pip install -e .`
- Try: `pip install PySide6 --upgrade`

## Shortcuts Created

After running `setup_taskbar.ps1`:
- ✅ Start Menu shortcut (searchable from Windows search)
- ✅ Desktop shortcut 
- ✅ Pinned to taskbar (if successful)

## Running from Command Line

```powershell
ai-hub
```

Or directly:
```powershell
python -m ai_hub.app
```

---

**Need help?** Check the batch script output for detailed diagnostic information.


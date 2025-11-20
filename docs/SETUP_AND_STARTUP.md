# 🚀 AI Hub - Setup and Startup Guide

## Quick Start (Choose One)

### Option 1: Manual Launch (Anytime)
```bash
# Open Command Prompt or PowerShell
# Navigate to folder
cd "D:\AI-HUB 2 Claude"

# Run the app
python -m ai_hub.app
```

Or simply:
```bash
# Double-click:
run_ai_hub.bat
```

---

## Option 2: Auto-Start on Login (Recommended!)

### Step 1: Install Startup
1. Right-click on `install_startup.ps1` in `D:\AI-HUB 2 Claude\`
2. Select **"Run with PowerShell"** (wait for the dialog)
3. Approve any security prompts
4. You'll see: ✅ **"AI Hub has been added to Windows Startup!"**

### Step 2: Verify
- Restart your computer
- AI Hub should launch automatically!

### Step 3: Remove from Startup (if needed)
1. Press `Win + R` and type: `shell:startup`
2. Delete the `AI Hub.lnk` file

---

## Option 3: Add to Taskbar (Quick Access)

### Step 1: Create Taskbar Shortcut
1. Right-click on `install_taskbar.ps1` in `D:\AI-HUB 2 Claude\`
2. Select **"Run with PowerShell"**
3. A shortcut will appear on your Desktop

### Step 2: Pin to Taskbar
1. Right-click the `AI Hub` shortcut on your Desktop
2. Select **"Pin to taskbar"**
3. Done! Now you can launch from taskbar anytime

### Step 3: Clean Up (Optional)
- Delete the Desktop shortcut if you want (it's already pinned)

---

## 📁 Folder Structure (Clean Organization)

```
D:\AI-HUB 2 Claude\
├── run_ai_hub.bat               ← Manual launch
├── startup.bat                  ← Auto-startup launch
├── install_startup.ps1          ← Setup auto-start
├── install_taskbar.ps1          ← Setup taskbar
├── settings.ini                 ← Configuration
├── pyproject.toml               ← Python project
├── src/                         ← Source code
│   └── ai_hub/                  ← Main application
│       ├── app.py
│       ├── config.py
│       ├── hotkeys/
│       ├── services/
│       └── ui/
├── config/                      ← Runtime config
│   ├── hotkeys.ini
│   ├── hotstrings.sav
│   ├── prompts.json
│   └── snippets.json
├── docs/                        ← Documentation (all guides/readmes)
│   ├── CLAUDE_INTEGRATION_PROMPTS.md
│   ├── PROMPTS_READY_TO_USE.txt
│   ├── QUICK_REFERENCE_CARD.txt
│   ├── SCALING_GUIDE.md
│   └── (20+ more docs)
└── reference_code/              ← Reference implementations
    └── AI-HUB-main/
```

---

## Windows Startup Folder Location

If you want to manually manage startup:

### Open Startup Folder:
1. Press `Win + R`
2. Type: `shell:startup`
3. Press Enter

You'll see shortcuts to programs that run at startup.

### Manual Setup:
1. Right-click in the Startup folder
2. Select **New → Shortcut**
3. Paste: `D:\AI-HUB 2 Claude\startup.bat`
4. Click Next
5. Name it: `AI Hub`
6. Click Finish

---

## Common Issues

### Issue: "python is not recognized"
**Solution:** Make sure Python 3.10+ is installed and in PATH
```bash
# Check Python version
python --version

# If not installed, download from python.org
```

### Issue: PowerShell script won't run
**Solution:** You might need to enable script execution
```powershell
# In PowerShell (as Administrator):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: App won't start
**Solution:** Check dependencies
```bash
cd "D:\AI-HUB 2 Claude"
pip install -e .
```

### Issue: AI Hub starts but closes immediately
**Solution:** Check for errors
```bash
# Run from command prompt to see errors
python -m ai_hub.app
```

---

## File Purposes

| File | Purpose | Use When |
|------|---------|----------|
| `run_ai_hub.bat` | Manual launch with troubleshooting | Debugging or testing |
| `startup.bat` | Minimal startup launcher | Used by Windows startup |
| `install_startup.ps1` | One-time setup for auto-start | First time setup |
| `install_taskbar.ps1` | One-time setup for taskbar | First time setup |

---

## Your Setup Checklist

### First Time:
- [ ] Extract/clone AI Hub to `D:\AI-HUB 2 Claude\`
- [ ] Install Python 3.10+ (if not already)
- [ ] Run `pip install -e .` to install dependencies

### Optional - Auto-Start:
- [ ] Right-click `install_startup.ps1` → Run with PowerShell
- [ ] Wait for success message
- [ ] Restart computer to verify

### Optional - Taskbar:
- [ ] Right-click `install_taskbar.ps1` → Run with PowerShell
- [ ] Right-click Desktop shortcut → Pin to taskbar
- [ ] Delete Desktop shortcut (optional)

### Done! 🎉
- [ ] AI Hub launches manually: Double-click `run_ai_hub.bat`
- [ ] AI Hub auto-starts: Restart computer
- [ ] AI Hub on taskbar: Click the taskbar icon

---

## Next Steps

1. **Test Manual Launch:**
   ```bash
   cd "D:\AI-HUB 2 Claude"
   python -m ai_hub.app
   ```

2. **Enable Auto-Start:** Run `install_startup.ps1`

3. **Add to Taskbar:** Run `install_taskbar.ps1`

4. **Restart Computer:** Verify everything works

5. **Get Started:** Read `docs/00_READ_THESE_FIRST.txt`

---

## Documentation

All guides and documentation are in the `docs/` folder:
- `docs/00_READ_THESE_FIRST.txt` ← Start here
- `docs/PROMPTS_READY_TO_USE.txt` ← Build with Claude
- `docs/QUICK_REFERENCE_CARD.txt` ← Developer reference
- `docs/SCALING_GUIDE.md` ← Understand the system

---

**You're all set! Let's build amazing things! 🚀**



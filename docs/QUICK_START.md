# 🚀 AI Hub - Quick Start

## Installation ✅ (DONE!)

Your AI Hub is **already installed**! 

Check: `pip list | findstr ai-hub` should show: `ai-hub 0.1.0`

---

## Run the App 🎮

### Easiest Way:
```
Double-click: run_ai_hub.bat
```

This will:
- ✅ Check Python is installed
- ✅ Verify all dependencies  
- ✅ Auto-install missing packages
- ✅ Launch the GUI
- ⏸️ Wait for you before closing

### Or from Command Line:
```powershell
ai-hub
```

---

## Add to Taskbar 📌

### Option 1 (Recommended):
```
Double-click: add_to_taskbar.bat
```
Creates shortcuts and pins to taskbar.

### Option 2 (Manual):
1. Right-click `run_ai_hub.bat`
2. Select "Create Shortcut"
3. Right-click the shortcut
4. Select "Pin to Taskbar"

---

## Configure API Key 🔑

AI Hub needs an OpenAI API key to chat with AI.

### Get Your Key:
1. Go to: https://platform.openai.com/api-keys
2. Create new API key
3. Copy it (starts with `sk-`)

### Add to Your Project:

**Option A - Via settings.ini:**
1. Open `settings.ini` in the project folder
2. Replace `sk-your-api-key-here` with your key
3. Save and restart the app

**Option B - Via Environment Variable:**
```powershell
$env:OPENAI_API_KEY = "sk-your-key-here"
ai-hub
```

**Option C - Keep it Secret:**
Add to Windows System Environment Variables:
1. Search "Environment Variables" in Windows
2. Add `OPENAI_API_KEY` with your key
3. Restart the app

---

## GUI Features 🎨

When you open AI Hub, you'll see:

### 📱 Three Tabs:

**1. Chat Tab** 💬
- Talk to OpenAI's AI
- Type message, send, get response
- Requires API key

**2. Prompts Tab** 📋  
- View and manage prompts
- Create custom prompts
- Organize your templates

**3. Spelling Tab** ✏️
- Check spelling and grammar
- AI-powered corrections
- Works with selected text

---

## Hotkeys ⌨️ (System-Wide)

These shortcuts work **anywhere on your computer**:

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+J` | Open spelling checker |
| `Ctrl+Shift+K` | Open prompt navigator |
| `Ctrl+Alt+Shift+K` | Bring window to focus |
| `Ctrl+Alt+H` | Toggle hotstrings on/off |

### Hotstrings (Auto-Text):
Type these and they expand:

- `;sig` → "Best regards, Your Name"
- `;date` → Today's date
- `;time` → Current time
- `;fix` → AI fixes your text
- `;clar` → AI clarifies your text
- `;short` → AI shortens text
- `;long` → AI expands text

---

## Files Explained 📁

| File | Purpose |
|------|---------|
| `run_ai_hub.bat` | 🎮 Main launcher with diagnostics |
| `add_to_taskbar.bat` | 📌 Add to taskbar shortcut |
| `settings.ini` | ⚙️ Configuration file (add API key here) |
| `QUICK_START.md` | 📖 This guide |
| `GUI_TESTING_GUIDE.md` | 🧪 Detailed testing & features |
| `LAUNCH_GUIDE.md` | 🚀 Advanced launcher guide |

---

## Troubleshooting 🔧

### "Python not found"
- Install from https://www.python.org
- Check "Add to PATH" during install

### "PySide6 not found"
- Run: `pip install PySide6 --upgrade`
- Or just use `run_ai_hub.bat` (it auto-fixes)

### "API key missing" warning
- Normal if not configured
- Get key from https://platform.openai.com/api-keys
- Add to `settings.ini` or environment variable

### App won't start
- Check batch file output for errors
- Run: `pip install -e .`
- Try: `pip install PySide6 --upgrade`

### Hotkeys not working
- Ensure app is running
- Make sure app window has focus
- Check `settings.ini` for correct keys

---

## Next Steps 🎯

1. **Try the GUI** - Double-click `run_ai_hub.bat`
2. **Get OpenAI API key** for AI features
3. **Add key to settings.ini**
4. **Customize hotkeys** in `settings.ini`
5. **Explore all three tabs**
6. **Try the hotkeys**
7. **Pin to taskbar** for easy access

---

## Support 💡

- Check `GUI_TESTING_GUIDE.md` for detailed features
- Check `LAUNCH_GUIDE.md` for advanced setup
- See error messages in batch window
- All dependencies auto-install via `run_ai_hub.bat`

---

**You're all set! 🎉 Go open AI Hub!**

```
Double-click: run_ai_hub.bat
```


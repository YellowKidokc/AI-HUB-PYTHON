# ⚡ AI Hub - 5-Minute Setup

## Step 1: Install Dependencies (First Time Only)

Open PowerShell or Command Prompt in this folder and run:

```bash
pip install -e .
```

This installs:
- PySide6 (GUI framework)
- keyboard (global hotkeys)
- pywin32 (clipboard handling)
- requests (API calls)
- All other dependencies

---

## Step 2: Configure Your API Key

1. Get an OpenAI API key from: https://platform.openai.com/api-keys
2. Open `settings.ini` in this folder
3. Replace `sk-your-api-key-here` with your actual key:

```ini
[openai]
api_key = sk-proj-YOUR_ACTUAL_KEY_HERE
```

**Note**: You can use the app without an API key, but AI features won't work.

---

## Step 3: Launch AI Hub

### Option A: Manual Launch (Recommended for First Time)
Double-click: `run_ai_hub.bat`

This shows a console window with diagnostics and error messages.

### Option B: Silent Launch (Background Mode)
Double-click: `Start_AI_Hub.bat`

This runs AI Hub silently in the background (no console window).

---

## Step 4: Create Your First Shortcut

1. **Open AI Hub** (it appears as a window)
2. **Click the "⚡ Shortcuts Manager" tab**
3. **Create a "Fix Everything" hotkey:**
   - Type: `Hotkey`
   - Action: `AI Rewrite`
   - Modifiers: Check `Ctrl`
   - Trigger: `space`
   - Description: `Fix grammar and spelling`
   - Output: `Fix all grammar, spelling, and punctuation errors. Keep the original tone.`
4. **Click "💾 Add / Save"**
5. **Restart AI Hub**

---

## Step 5: Test It!

1. Open Notepad or any text editor
2. Type some messy text: `this is a test with bad grammer and speling`
3. Select the text (Ctrl+A)
4. Press `Ctrl+Space`
5. Watch the magic happen! ✨

---

## 🎯 What You Get

### ✅ Global Hotkeys
- Work in **any app** (Chrome, Notepad, Slack, Discord, etc.)
- Press a key combo → AI fixes your text instantly

### ✅ Visual Manager
- AHK-style GUI for creating shortcuts
- No coding required!

### ✅ Three Action Types
1. **Send Text**: Type snippets instantly
2. **Run Program**: Launch apps with hotkeys
3. **AI Rewrite**: Transform text with AI

---

## 🚀 Auto-Start on Windows Boot (Optional)

Want AI Hub to start automatically when Windows starts?

1. Right-click: `install_startup.ps1`
2. Select: "Run with PowerShell"
3. Wait for: ✅ Success message
4. Restart your computer

AI Hub will now launch silently every time you boot Windows!

---

## 🐛 Troubleshooting

### "Python not found"
Install Python 3.10+ from: https://www.python.org/downloads/

Make sure to check "Add Python to PATH" during installation.

### "Module not found"
Run: `pip install -e .` in this folder

### "API key invalid"
Check `settings.ini` and make sure your key starts with `sk-proj-` or `sk-`

### Hotkeys not working
1. Restart AI Hub after creating shortcuts
2. Make sure the hotkey isn't already used by Windows
3. Try running `run_ai_hub.bat` as Administrator

---

## 📚 Next Steps

- Read: `SHORTCUTS_MANAGER_GUIDE.md` for detailed examples
- Check: `settings.ini` for more configuration options
- Explore: The other tabs (Chat, Prompts, Spelling)

---

**You're all set! Enjoy your AI-powered shortcuts! 🎉**

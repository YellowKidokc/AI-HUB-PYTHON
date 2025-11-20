# 🎯 AI Hub - Shortcuts Manager Guide

## What Is This?

The **Shortcuts Manager** is your visual control panel for creating custom keyboard shortcuts and text replacements. It works like your old AutoHotkey script but runs entirely in Python with AI superpowers! 🚀

---

## 🚀 Quick Start

### 1. Launch AI Hub
- **Option A**: Double-click `run_ai_hub.bat` (shows console for debugging)
- **Option B**: Double-click `Start_AI_Hub.bat` (silent background mode)
- **Option C**: For auto-start on Windows boot, run `install_startup.ps1`

### 2. Open Shortcuts Manager
- Click the **⚡ Shortcuts Manager** tab in the AI Hub window

### 3. Create Your First Shortcut
1. **Type**: Choose "Hotkey" (keyboard shortcut) or "Hotstring" (text replacement)
2. **Action**: Choose what happens when triggered
3. **Modifiers**: Check Ctrl, Alt, Shift, or Win (for hotkeys only)
4. **Trigger**: Type the key (e.g., "space", "k", "f1")
5. **Description**: Brief note about what this does
6. **Output**: The text, program path, or AI instruction
7. Click **💾 Add / Save**
8. **Restart AI Hub** for changes to take effect

---

## 📋 Action Types Explained

### 1. **Send Text**
Instantly types text when you press the hotkey.

**Example:**
- **Hotkey**: `Ctrl+Shift+S`
- **Output**: 
  ```
  Best regards,
  John Smith
  john@example.com
  ```
- **Use Case**: Email signatures, common responses, templates

---

### 2. **Run Program**
Launches any program or file.

**Example:**
- **Hotkey**: `Ctrl+Alt+N`
- **Output**: `notepad.exe`
- **Use Case**: Quick access to apps, scripts, or files

**Pro Tip**: You can use full paths:
```
C:\Program Files\Google\Chrome\chrome.exe https://google.com
```

---

### 3. **AI Rewrite** ⭐ (The Magic One!)
Uses AI to transform selected text based on your instruction.

**Example 1: Grammar Fixer**
- **Hotkey**: `Ctrl+Space`
- **Output**: `Fix all grammar and spelling errors. Keep the original tone.`
- **How to Use**: 
  1. Select messy text anywhere (Chrome, Notepad, Slack, etc.)
  2. Press `Ctrl+Space`
  3. AI fixes it and replaces the text automatically!

**Example 2: Make It Professional**
- **Hotkey**: `Ctrl+Shift+P`
- **Output**: `Rewrite this in a professional business tone.`

**Example 3: Simplify**
- **Hotkey**: `Ctrl+Shift+E`
- **Output**: `Explain this like I'm 10 years old. Use simple words.`

**Example 4: Expand**
- **Hotkey**: `Ctrl+Shift+L`
- **Output**: `Expand this into a detailed explanation with examples.`

---

## 🎨 Hotkey vs Hotstring

### Hotkey (Keyboard Shortcut)
- Triggered by pressing keys together
- Examples: `Ctrl+K`, `Alt+Shift+F1`, `Win+Space`
- Best for: Actions you do frequently

### Hotstring (Text Replacement)
- Triggered by typing an abbreviation
- Examples: Type `btw` → expands to "by the way"
- Best for: Text snippets, email addresses, common phrases
- **Note**: Hotstring support is coming in a future update!

---

## 💡 Pro Tips

### 1. **The "Fix Everything" Hotkey**
This is the most useful shortcut. Set it up first!

```
Type: Hotkey
Action: AI Rewrite
Modifiers: Ctrl
Trigger: space
Description: Fix grammar and spelling
Output: Fix all grammar, spelling, and punctuation errors. Keep the original tone and meaning. Do not add extra words.
```

**Usage**: Select text → Press `Ctrl+Space` → Magic! ✨

---

### 2. **Quick Program Launchers**
```
Ctrl+Alt+C → Chrome
Ctrl+Alt+N → Notepad
Ctrl+Alt+V → VS Code
```

---

### 3. **Email Templates**
```
Ctrl+Shift+1 → "Thanks for reaching out! I'll get back to you soon."
Ctrl+Shift+2 → "Please see attached."
Ctrl+Shift+3 → Your full email signature
```

---

### 4. **AI Writing Modes**
Create multiple AI shortcuts for different styles:

```
Ctrl+1 → "Make this casual and friendly"
Ctrl+2 → "Make this formal and professional"
Ctrl+3 → "Summarize this in 2 sentences"
Ctrl+4 → "Translate this to Spanish"
```

---

## 🔧 How It Works (Technical)

1. **You create shortcuts** in the GUI
2. **Saved to**: `config/shortcuts.json`
3. **Loaded at startup** by `GlobalHotkeys` class
4. **Registered globally** using the `keyboard` library
5. **Works everywhere** - Chrome, Notepad, Slack, Discord, etc.

---

## 🐛 Troubleshooting

### Shortcuts Not Working?
1. **Did you restart AI Hub?** Changes only apply after restart
2. **Check for conflicts**: Make sure the hotkey isn't used by Windows or another app
3. **Run as Administrator**: Some apps need elevated permissions

### AI Rewrite Not Responding?
1. **Check your API key** in `settings.ini`
2. **Make sure text is selected** before pressing the hotkey
3. **Check console** for error messages (use `run_ai_hub.bat`)

### Can't Select Text?
- The AI Rewrite action uses `Ctrl+C` to copy selected text
- Make sure the target app supports text selection

---

## 📝 Example Shortcuts Library

Here are some ready-to-use shortcuts:

### Grammar & Spelling
```json
{
  "type": "Hotkey",
  "action": "AI Rewrite",
  "trigger": "space",
  "modifiers": ["ctrl"],
  "desc": "Fix grammar and spelling",
  "output": "Fix all grammar, spelling, and punctuation. Keep the tone."
}
```

### Professional Tone
```json
{
  "type": "Hotkey",
  "action": "AI Rewrite",
  "trigger": "p",
  "modifiers": ["ctrl", "shift"],
  "desc": "Make it professional",
  "output": "Rewrite this in a professional business tone."
}
```

### Summarize
```json
{
  "type": "Hotkey",
  "action": "AI Rewrite",
  "trigger": "s",
  "modifiers": ["ctrl", "shift"],
  "desc": "Summarize text",
  "output": "Summarize this in 2-3 sentences."
}
```

### Email Signature
```json
{
  "type": "Hotkey",
  "action": "Send Text",
  "trigger": "s",
  "modifiers": ["ctrl", "alt"],
  "desc": "Insert signature",
  "output": "Best regards,\nYour Name\nyour.email@example.com"
}
```

---

## 🎯 Next Steps

1. **Create your "Fix Everything" hotkey** (`Ctrl+Space`)
2. **Add 3-5 common text snippets** you use daily
3. **Experiment with AI instructions** - the possibilities are endless!
4. **Share your best shortcuts** with the community

---

## 🚀 Advanced: Google Dorks Launcher (Coming Soon!)

The next feature will add a menu for quick Google searches:
- Security research queries
- Advanced search operators
- Site-specific searches
- And more!

---

## 📞 Need Help?

- Check the console output: `run_ai_hub.bat`
- Review `settings.ini` for API configuration
- Check `config/shortcuts.json` to see saved shortcuts

---

**Happy automating! 🎉**

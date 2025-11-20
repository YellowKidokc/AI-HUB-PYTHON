# 🎨 AI Hub GUI Testing Guide

## GUI Overview

Your AI Hub has a **beautiful dark-themed GUI** with three main tabs:

### 📱 Three Main Tabs:

1. **Chat Tab** 💬
   - Direct conversation with OpenAI's AI
   - Type your message and send
   - Get intelligent responses
   - Requires valid OpenAI API key

2. **Prompts Tab** 📋
   - Manage and organize AI prompts
   - Create custom system prompts
   - Save frequently used prompts
   - View all available prompts

3. **Spelling Tab** ✏️
   - Check and fix spelling/grammar
   - Works with the current selection
   - Uses AI to improve text quality
   - Auto-correction suggestions

---

## 🚀 How to Launch the GUI

### Option 1: Double-Click (Easiest)
```
run_ai_hub.bat
```

### Option 2: Command Line
```powershell
ai-hub
```

### Option 3: Direct Python
```powershell
python -m ai_hub.app
```

---

## ⚙️ Configuration

### API Key Setup (Required for AI Features)

1. **Get an API Key:**
   - Go to: https://platform.openai.com/api-keys
   - Create a new API key
   - Copy it (starts with `sk-`)

2. **Add to settings.ini:**
   - Open `settings.ini` in the project directory
   - Replace `sk-your-api-key-here` with your actual key:
   ```ini
   [openai]
   api_key = sk-your-actual-key-here
   ```

3. **Or Set Environment Variable:**
   ```powershell
   $env:OPENAI_API_KEY = "sk-your-key-here"
   python -m ai_hub.app
   ```

### Customize Hotkeys

Edit `settings.ini` to change keyboard shortcuts:

```ini
[hotkeys]
spelling = ctrl+shift+j          # Spell check shortcut
prompt_navigator = ctrl+shift+k  # Open prompt dialog
goto_hub = ctrl+alt+shift+k      # Bring window to front
toggle_hotstrings = ctrl+alt+h   # Enable/disable hotstrings
```

### Configure Hotstrings

Auto-text replacements work anywhere on your system:

| Text | Replaces With |
|------|---------------|
| `;sig` | Best regards, Your Name |
| `;date` | Today's date (YYYY-MM-DD) |
| `;time` | Current time (HH:MM) |
| `;fix` | AI Grammar/spelling fix |
| `;clar` | AI Clarify text |
| `;short` | AI Make text shorter |
| `;long` | AI Make text longer |

---

## 🧪 What to Test

### GUI Display
- [ ] Window opens and displays correctly
- [ ] Dark theme is applied
- [ ] All three tabs are visible
- [ ] Window can be resized
- [ ] Text is readable

### Chat Tab
- [ ] Can type text in input field
- [ ] Send button works
- [ ] Gets response from OpenAI (if API key is set)
- [ ] Shows error message if API key is missing
- [ ] Conversation history displays

### Prompts Tab
- [ ] Shows list of available prompts
- [ ] Can view prompt details
- [ ] Interface is responsive

### Spelling Tab
- [ ] Input field works
- [ ] Can paste/type text
- [ ] Shows spelling corrections (with API key)
- [ ] Button clicks work

### Hotkeys (System-Wide)
- [ ] `Ctrl+Shift+J` - Opens spelling check
- [ ] `Ctrl+Shift+K` - Opens prompt navigator
- [ ] `Ctrl+Alt+Shift+K` - Brings window to front
- [ ] `Ctrl+Alt+H` - Toggles hotstrings

### Hotstrings
- [ ] Type `;sig` anywhere and it expands
- [ ] Type `;date` and today's date appears
- [ ] Type `;fix` and AI fixes selected text
- [ ] Hotstrings can be toggled on/off

---

## 🛠️ Troubleshooting

### GUI Won't Open
1. Check batch file output for errors
2. Verify Python is installed: `python --version`
3. Verify PySide6 is installed: `pip show PySide6`
4. Check for missing dependencies: `pip install -e .`

### API Key Warning Appears
- This is normal if API key not set
- You can still explore the UI
- Get a key from OpenAI and add to `settings.ini`

### Hotkeys Not Working
- Make sure the app is running
- Check `settings.ini` for correct key combinations
- Some applications block hotkeys
- Admin privileges may be required

### Text Input Not Responding
- Click in the text field first
- Try keyboard: `Tab` to focus fields
- Ensure app window has focus

---

## 📝 Sample Settings

Here's a `settings.ini` template:

```ini
[openai]
api_key = sk-your-api-key-here
endpoint = https://api.openai.com/v1/chat/completions
model = gpt-4o-mini
timeout = 120

[hotkeys]
spelling = ctrl+shift+j
prompt_navigator = ctrl+shift+k
goto_hub = ctrl+alt+shift+k
toggle_hotstrings = ctrl+alt+h

[hotstrings]
enabled = true
buffer_size = 64
```

---

## 🎯 Next Steps

1. **Get OpenAI API Key** if you want to use AI features
2. **Test the interface** to familiarize yourself with the tabs
3. **Try hotkeys** for quick access to features
4. **Customize prompts** for your use cases

---

## 📚 UI Features

### Dark Theme
- Professional dark interface
- Easy on the eyes
- Automatically adapts to your system theme

### Responsive Design
- 1000x720 default window size
- Resizable and movable
- Clean, modern layout

### Tab-Based Navigation
- Easy switching between features
- Each tab has its own functionality
- Organized interface

### Real-Time Feedback
- Shows loading states
- Error messages are clear
- Success confirmations

---

**Enjoy your AI Hub! 🚀**


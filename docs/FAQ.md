# ❓ Frequently Asked Questions

Common questions and answers about AI Hub.

---

## General Questions

### What is AI Hub?
AI Hub is an AI-powered desktop automation tool that provides:
- Global hotkeys for text correction
- Mouse automation with position recording
- AI chat powered by OpenAI
- Clipboard management
- Voice control and text-to-speech
- Custom shortcuts and workflows

### Is it free?
The software is free and open-source. However, you need an OpenAI API key, which has usage-based costs (typically very affordable for personal use).

### What platforms are supported?
- **Windows**: Fully supported ✅
- **Linux**: Experimental support ⚠️
- **macOS**: Limited support ⚠️

### Do I need an internet connection?
Yes, for AI features (chat, text correction). Mouse automation and clipboard management work offline.

---

## Installation & Setup

### How do I get an API key?
1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Copy and paste it into AI Hub

### How much does the API cost?
OpenAI charges per token (words). For typical use:
- Text correction: ~$0.01-0.05 per day
- Chat: ~$0.10-0.50 per day
- Heavy use: ~$1-5 per day

Check [OpenAI Pricing](https://openai.com/pricing) for current rates.

### Can I use a different AI model?
Currently, AI Hub uses GPT-4o-mini. Support for other models (Claude, Gemini, local models) is planned for future versions.

### How do I update AI Hub?
```bash
cd AI-HUB
git pull origin main
pip install -e ".[voice]" --upgrade
```

---

## Features

### How does mouse automation work?
1. Record the position of a button/element
2. Create a hotkey
3. Press the hotkey to click that position automatically

See [Mouse Automation Guide](MOUSE_AUTOMATION_GUIDE.md) for details.

### Can I create custom hotkeys?
Yes! Go to the **⚡ Shortcuts** tab and create:
- Text expansion (hotstrings)
- Mouse clicks
- AI prompts
- Custom actions

### Does it work when the window is closed?
Yes! Minimize to system tray and all hotkeys continue working globally.

### Can I use it in games?
Mouse automation works in most games, but:
- Some anti-cheat systems may block it
- Use at your own risk
- Not recommended for competitive games

---

## Mouse Automation

### Why isn't my mouse click working?
Common issues:
1. **Wrong coordinates**: Re-record position
2. **Window moved**: Maximize window before recording
3. **pyautogui not installed**: Run `pip install pyautogui`
4. **Admin rights needed**: Try running as Administrator

### Can I click multiple positions in sequence?
Yes! Create multiple shortcuts with different hotkeys:
- Ctrl+1 → Click position A
- Ctrl+2 → Click position B
- Ctrl+3 → Click position C

### Does it work across multiple monitors?
Yes! Position Recorder works across all monitors. Coordinates span the entire desktop.

### Will my mouse move?
Yes, briefly. The mouse:
1. Moves to target position
2. Clicks
3. Returns to original position
All in ~0.2 seconds.

---

## Hotkeys

### Can I change the default hotkeys?
Yes! Go to **⚡ Shortcuts** tab and customize any hotkey.

### My hotkeys conflict with other apps
Change them in the Shortcuts tab. Choose combinations that don't conflict with your other software.

### Hotkeys stopped working
Check:
1. AI Hub is running (check system tray)
2. No conflicting applications
3. Try restarting AI Hub
4. Run as Administrator if needed

### Can I disable hotkeys temporarily?
Yes! Press **Ctrl+Alt+H** to toggle hotstrings on/off.

---

## Clipboard Manager

### Where is clipboard data stored?
Locally in `config/clipboard_data.json`. Never sent anywhere.

### How much history is saved?
Default: Last 100 items. Configurable in settings.

### Can I sync clipboard across devices?
Not currently. Cloud sync is planned for a future version.

### How do I clear clipboard history?
Open Clipboard Manager (Ctrl+Alt+C) and use the clear button.

---

## Voice Features

### Voice features don't work
Install voice dependencies:
```bash
pip install -r requirements-voice.txt
```

### Which languages are supported?
Text-to-speech supports 50+ languages via edge-tts. Voice recognition supports English primarily (via Whisper).

### Can I change the voice?
Yes! Go to **🎙️ Voice** tab and select from available voices.

---

## Privacy & Security

### Is my data safe?
Yes:
- API key stored locally only
- Clipboard data stored locally
- Chat history stored locally
- No telemetry or tracking
- Only API calls go to OpenAI

### What data is sent to OpenAI?
Only:
- Text you explicitly send for correction/chat
- Your API key (for authentication)
- No clipboard history, no keystrokes, no personal data

### Can I use it offline?
Partially:
- ✅ Mouse automation works offline
- ✅ Clipboard manager works offline
- ✅ Hotkeys work offline
- ❌ AI features require internet

---

## Troubleshooting

### "API key is not configured"
Run `set_api_key.bat` or manually edit `settings.ini`

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### Application won't start
1. Check Python version (3.10+)
2. Reinstall dependencies
3. Check console for errors
4. Try running as Administrator

### High CPU usage
- Check for hotkey conflicts
- Disable unused features
- Update to latest version

### Antivirus blocking AI Hub
Add AI Hub folder to antivirus exceptions. The app is safe but may trigger false positives due to hotkey monitoring.

---

## Advanced

### Can I build an executable?
Yes! Use PyInstaller:
```bash
python Windows_and_Linux/pyinstaller-build-script.py
```

### Can I contribute?
Yes! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

### Where are settings stored?
- `settings.ini` - Main configuration
- `config/` - Data files (clipboard, chat history, shortcuts)

### Can I use it commercially?
Yes, under the MIT License. See [LICENSE](../LICENSE).

---

## Getting Help

### Where can I get help?
1. Check this FAQ
2. Read the [documentation](../README.md)
3. Search [GitHub Issues](https://github.com/yourusername/AI-HUB/issues)
4. Open a new issue if needed

### How do I report a bug?
1. Go to GitHub Issues
2. Click "New Issue"
3. Choose "Bug Report"
4. Fill in the template

### How do I request a feature?
1. Go to GitHub Issues
2. Click "New Issue"
3. Choose "Feature Request"
4. Describe your idea

---

## Roadmap

### What's coming next?
See [CHANGELOG.md](../CHANGELOG.md) for planned features:
- Click sequences
- Image recognition
- Macro recording
- Custom themes
- Plugin system
- And more!

---

**Still have questions?** Open an issue on GitHub!

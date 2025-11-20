# 🚀 AI Hub

**AI-powered desktop automation hub with voice control, shortcuts, chat, and mouse automation.**

![Version](https://img.shields.io/badge/version-0.2.0-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

---

## ✨ Features

### 💬 **AI Chat**
- Full AI conversations powered by OpenAI GPT-4o-mini
- Context-aware responses
- Persistent chat history

### ⌨️ **Global Hotkeys**
- **Ctrl+Space** - Fix spelling/grammar on selected text
- **Ctrl+Alt+P** - Open prompt navigator
- **Ctrl+Alt+C** - Clipboard manager
- **Ctrl+Alt+G** - Show/hide main window
- **Ctrl+M** - Mouse automation (customizable)

### 🖱️ **Mouse Automation**
- Click anywhere with a hotkey
- Position recorder with live coordinates
- Perfect for repetitive tasks (mic toggle, camera control, etc.)
- See [Mouse Automation Guide](docs/MOUSE_AUTOMATION_GUIDE.md)

### 🎙️ **Voice Control**
- Text-to-speech with edge-tts
- Voice recognition with Whisper
- Floating audio player

### ⚡ **Custom Shortcuts**
- Create custom hotkeys for any action
- Text expansion (hotstrings)
- AI-powered text transformations
- Mouse click automation

### 📝 **Prompts Manager**
- Create and manage reusable AI prompts
- Full CRUD interface (Create, Read, Update, Delete)
- Reorder prompts with drag-and-drop style controls
- No hardcoding - everything through GUI
- See [Prompts Guide](docs/PROMPTS_GUIDE.md)

### 📋 **Clipboard Manager**
- Auto-save clipboard history
- Pin important items
- Assign hotkeys to clips
- Persistent storage

### 🔍 **Web Scraper**
- Multi-engine search (Google, Bing, Yahoo, DuckDuckGo, etc.)
- Export results to TXT/JSON/CSV
- Proxy support

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10+**
- **Windows** (Linux support available)
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))

### Installation

#### Option 1: Quick Setup (Windows)
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/AI-HUB.git
cd AI-HUB

# 2. Set your API key
set_api_key.bat

# 3. Start AI Hub
startup_ai_hub.bat
```

#### Option 2: Manual Setup
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/AI-HUB.git
cd AI-HUB

# 2. Install dependencies
pip install -e .

# 3. (Optional) Install voice features
pip install -e ".[voice]"

# 4. Configure API key
# Edit settings.ini and add your OpenAI API key

# 5. Run AI Hub
python -m ai_hub.app
```

---

## 📖 Documentation

- **[First Time Setup](README_FIRST_TIME_SETUP.md)** - Complete setup guide
- **[Mouse Automation Guide](docs/MOUSE_AUTOMATION_GUIDE.md)** - Click automation tutorial
- **[Prompts Manager Guide](docs/PROMPTS_GUIDE.md)** - Create and manage AI prompts
- **[API Key Setup](SETUP_API_KEY.md)** - Detailed API configuration
- **[Search Scraper Guide](SEARCH_SCRAPER_GUIDE.md)** - Web scraping instructions

---

## 🎯 Use Cases

### 1. **Mic Toggle Automation**
Record your mic button position and toggle it with Ctrl+M from anywhere!

### 2. **Text Correction**
Select any text, press Ctrl+Space, and get instant grammar/spelling fixes.

### 3. **Clipboard Management**
Save and reuse frequently used text snippets with custom hotkeys.

### 4. **Custom Workflows**
Create multi-step automations combining mouse clicks, text expansion, and AI actions.

### 5. **Voice Control**
Convert text to speech or use voice commands for hands-free operation.

---

## 🔧 Configuration

### API Key Setup
```ini
# settings.ini
[API]
api_key = sk-your-api-key-here
model = gpt-4o-mini
```

### Custom Hotkeys
Configure in the **⚡ Shortcuts** tab:
- Choose modifiers (Ctrl, Alt, Shift)
- Select trigger key
- Define action (text, mouse click, AI prompt)

### Mouse Automation
1. Open **⚡ Shortcuts** tab
2. Select **Action: Mouse Click**
3. Click **🎯 Open Position Recorder**
4. Hover over target and record position
5. Create hotkey with recorded coordinates

---

## 🛠️ Development

### Project Structure
```
AI-HUB/
├── src/
│   └── ai_hub/          # Main application code
├── docs/                # Documentation
├── config/              # Configuration files
├── settings.ini         # User settings
├── pyproject.toml       # Project metadata
└── requirements.txt     # Python dependencies
```

### Running from Source
```bash
# Install in development mode
pip install -e ".[voice]"

# Run the application
python -m ai_hub.app
```

### Building Executable
```bash
# Use PyInstaller
python Windows_and_Linux/pyinstaller-build-script.py
```

---

## 🔒 Privacy & Security

- **API Key**: Stored locally in `settings.ini` (never shared)
- **Clipboard**: Stored locally in `config/clipboard_data.json`
- **Chat History**: Stored locally in `config/chat_history.json`
- **No Telemetry**: No data is sent anywhere except OpenAI API calls

---

## 🐛 Troubleshooting

### App Won't Start
If AI Hub isn't working, try disabling mouse automation:
```bash
disable_mouse_automation.bat
```

Then restart AI Hub. See [Full Troubleshooting Guide](docs/TROUBLESHOOTING.md)

### Hotkeys Don't Work
- Ensure AI Hub is running (check system tray)
- Try running as Administrator
- Check for conflicting hotkeys

### Mouse Automation Fails
```bash
# Install pyautogui
pip install pyautogui

# Or disable it temporarily
disable_mouse_automation.bat
```

### API Key Errors
- Verify key is correct in `settings.ini`
- Check OpenAI account has credits
- Run `set_api_key.bat` to reconfigure

### Voice Features Not Working
```bash
# Install voice dependencies
pip install -e ".[voice]"
```

**For more help**: See [Troubleshooting Guide](docs/TROUBLESHOOTING.md) or [FAQ](docs/FAQ.md)

---

## 📦 Dependencies

### Core
- PySide6 - GUI framework
- requests - HTTP library
- keyboard - Hotkey detection
- pynput - Input control
- pyperclip - Clipboard access
- pyautogui - Mouse automation

### Optional (Voice)
- edge-tts - Text-to-speech
- faster-whisper - Speech recognition
- sounddevice - Audio I/O
- pygame - Audio playback

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📝 License

This project is licensed under the MIT License.

---

## 🌟 Acknowledgments

- Built with [PySide6](https://www.qt.io/qt-for-python)
- AI powered by [OpenAI](https://openai.com)
- Voice by [edge-tts](https://github.com/rany2/edge-tts)
- Speech recognition by [faster-whisper](https://github.com/guillaumekln/faster-whisper)

---

## 📞 Support

- **Documentation**: Check the `docs/` folder
- **Issues**: Open an issue on GitHub
- **Setup Help**: See `README_FIRST_TIME_SETUP.md`

---

**Made with ❤️ for productivity enthusiasts**

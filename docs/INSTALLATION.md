# 📦 Installation Guide

Complete installation instructions for AI Hub.

---

## Prerequisites

- **Python 3.10 or higher**
- **Windows** (primary), Linux (experimental)
- **OpenAI API Key** - [Get one here](https://platform.openai.com/api-keys)

---

## Installation Methods

### Method 1: Quick Install (Recommended for Windows)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/AI-HUB.git
cd AI-HUB

# 2. Run the setup script
set_api_key.bat

# 3. Start AI Hub
startup_ai_hub.bat
```

The startup script will:
- Check Python version
- Install dependencies automatically
- Configure the application
- Start AI Hub

---

### Method 2: Manual Installation

#### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/AI-HUB.git
cd AI-HUB
```

#### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies

**Core Features Only:**
```bash
pip install -r requirements.txt
```

**With Voice Features:**
```bash
pip install -r requirements.txt -r requirements-voice.txt
```

**Or using pyproject.toml:**
```bash
# Core only
pip install -e .

# With voice features
pip install -e ".[voice]"
```

#### Step 4: Configure API Key

**Option A: Use Helper Script**
```bash
set_api_key.bat
```

**Option B: Manual Configuration**
1. Open `settings.ini`
2. Replace `sk-your-api-key-here` with your actual OpenAI API key
3. Save the file

#### Step 5: Run AI Hub
```bash
python -m ai_hub.app
```

---

### Method 3: Development Installation

For contributors and developers:

```bash
# Clone repository
git clone https://github.com/yourusername/AI-HUB.git
cd AI-HUB

# Install in editable mode with all features
pip install -e ".[voice]"

# Run from source
python -m ai_hub.app
```

---

## Verify Installation

### Check Python Version
```bash
python --version
# Should show 3.10 or higher
```

### Check Dependencies
```bash
pip list
# Should show PySide6, pyautogui, requests, etc.
```

### Test Import
```python
python -c "import ai_hub; print('AI Hub installed successfully!')"
```

---

## Auto-Start Setup (Windows)

To start AI Hub automatically when Windows starts:

```bash
# Run the auto-start setup script
setup_autostart.bat
```

This will:
- Create a startup shortcut
- Configure Windows to launch AI Hub on login
- Show confirmation message

To remove auto-start:
```bash
remove_autostart.bat
```

---

## Taskbar Pinning (Windows)

To pin AI Hub to your taskbar:

```bash
# Run the taskbar setup script
setup_taskbar.ps1
```

---

## Voice Features Installation

Voice features require additional dependencies:

```bash
# Install voice dependencies
pip install -r requirements-voice.txt
```

Or:
```bash
pip install edge-tts faster-whisper sounddevice scipy numpy pygame
```

**Note**: Voice features require:
- Microphone (for voice input)
- Speakers/headphones (for text-to-speech)
- ~1GB additional disk space (for Whisper models)

---

## Troubleshooting

### Python Not Found
```bash
# Windows: Install from python.org
# Make sure to check "Add Python to PATH"

# Verify installation
python --version
```

### Permission Errors (Windows)
```bash
# Run as Administrator
# Right-click PowerShell → "Run as Administrator"
```

### Module Not Found Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### pywin32 Installation Issues (Windows)
```bash
# Install separately
pip install pywin32
python Scripts/pywin32_postinstall.py -install
```

### pyautogui Not Working
```bash
# Reinstall with dependencies
pip uninstall pyautogui
pip install pyautogui
```

### Voice Features Not Working
```bash
# Check microphone permissions
# Windows Settings → Privacy → Microphone

# Reinstall voice dependencies
pip install -r requirements-voice.txt --force-reinstall
```

---

## Platform-Specific Notes

### Windows
- Requires **pywin32** for system integration
- Hotkeys work globally across all applications
- System tray integration fully supported
- Auto-start and taskbar pinning available

### Linux
- Some features may require root/sudo
- System tray support varies by desktop environment
- Hotkeys may conflict with desktop shortcuts
- Test thoroughly on your distribution

### macOS
- Experimental support only
- May require additional permissions
- Some hotkeys may not work
- System tray behavior differs

---

## Updating AI Hub

### From Git
```bash
cd AI-HUB
git pull origin main
pip install -e ".[voice]" --upgrade
```

### Manual Update
1. Download latest release
2. Extract to installation directory
3. Run `pip install -e ".[voice]" --upgrade`
4. Restart AI Hub

---

## Uninstallation

### Remove Application
```bash
# If installed with pip
pip uninstall ai-hub

# Remove directory
cd ..
rmdir /s AI-HUB  # Windows
rm -rf AI-HUB    # Linux
```

### Remove Auto-Start
```bash
remove_autostart.bat
```

### Clean Up Data
```bash
# Remove configuration files
del settings.ini
del config\*
```

---

## Next Steps

After installation:
1. ✅ Configure API key
2. ✅ Test basic features
3. ✅ Set up auto-start (optional)
4. ✅ Read the [First Time Setup Guide](../README_FIRST_TIME_SETUP.md)
5. ✅ Explore [Mouse Automation](MOUSE_AUTOMATION_GUIDE.md)

---

**Need help?** Check the [Troubleshooting Guide](../README_FIRST_TIME_SETUP.md#troubleshooting) or open an issue on GitHub.

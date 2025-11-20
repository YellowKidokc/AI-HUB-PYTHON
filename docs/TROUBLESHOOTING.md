# 🔧 Troubleshooting Guide

Common issues and solutions for AI Hub.

---

## 🚨 App Won't Start

### Issue: Application doesn't launch
**Solutions:**
1. Check Python version:
   ```bash
   python --version
   # Must be 3.10 or higher
   ```

2. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

3. Check for errors:
   ```bash
   python -m ai_hub.app
   # Look at console output for specific errors
   ```

4. Try without voice features:
   ```bash
   pip uninstall edge-tts faster-whisper sounddevice scipy numpy pygame
   python -m ai_hub.app
   ```

---

## 🖱️ Mouse Automation Issues

### Issue: Mouse automation not working
**Solutions:**

1. **Install pyautogui:**
   ```bash
   pip install pyautogui
   ```

2. **Disable mouse automation temporarily:**
   
   Edit `src/ai_hub/services/mouse_automation.py` and change line 14:
   ```python
   # Change this:
   HAVE_PYAUTOGUI = True
   
   # To this:
   HAVE_PYAUTOGUI = False
   ```

3. **Remove mouse click shortcuts:**
   - Open AI Hub
   - Go to ⚡ Shortcuts tab
   - Delete any "Mouse Click" shortcuts
   - Restart AI Hub

4. **Check permissions:**
   - Run AI Hub as Administrator
   - Some security software blocks mouse automation

### Issue: Mouse clicks at wrong position
**Solutions:**
1. Re-record position using Position Recorder
2. Ensure target window is maximized
3. Check if UI has moved/resized
4. Use Position Recorder's "Test" button before saving

### Issue: "pyautogui not installed" error
**Solution:**
```bash
pip install pyautogui
```

If that fails:
```bash
pip install pillow
pip install pyautogui
```

---

## ⌨️ Hotkey Issues

### Issue: Hotkeys don't work
**Solutions:**
1. **Check app is running:**
   - Look for AI Hub icon in system tray (bottom-right)
   - Click the ^ arrow to show hidden icons

2. **Restart hotkeys:**
   - Close AI Hub completely (right-click tray icon → Exit)
   - Restart with `startup_ai_hub.bat`

3. **Check for conflicts:**
   - Try different hotkey combinations
   - Some apps block global hotkeys
   - Try running as Administrator

4. **Reinstall keyboard library:**
   ```bash
   pip uninstall keyboard
   pip install keyboard
   ```

### Issue: Specific hotkey doesn't work
**Solutions:**
1. Change the hotkey combination in ⚡ Shortcuts tab
2. Avoid combinations used by Windows (Win+L, Ctrl+Alt+Del, etc.)
3. Test with simple combinations first (Ctrl+Shift+K)

---

## 🔑 API Key Issues

### Issue: "API key is not configured"
**Solutions:**
1. **Use helper script:**
   ```bash
   set_api_key.bat
   ```

2. **Manual fix:**
   - Open `settings.ini`
   - Find `api_key = sk-your-api-key-here`
   - Replace with your actual OpenAI API key
   - Save and restart

3. **Verify key is valid:**
   - Go to https://platform.openai.com/api-keys
   - Check key hasn't expired
   - Check account has credits

### Issue: "Invalid API key" error
**Solutions:**
1. Get a new key from OpenAI
2. Make sure you copied the entire key (starts with `sk-`)
3. No extra spaces before/after the key

---

## 💬 Chat/AI Features Not Working

### Issue: Chat doesn't respond
**Solutions:**
1. Check API key is configured
2. Check internet connection
3. Check OpenAI account has credits
4. Try different model in settings

### Issue: "Rate limit exceeded"
**Solution:**
- Wait a few minutes
- Check OpenAI usage limits
- Upgrade OpenAI plan if needed

### Issue: Slow responses
**Solutions:**
1. Check internet speed
2. Try gpt-4o-mini (faster, cheaper)
3. Reduce message length

---

## 📋 Clipboard Manager Issues

### Issue: Clipboard not saving history
**Solutions:**
1. Check `config/clipboard_data.json` exists
2. Ensure AI Hub is running
3. Try copying text again
4. Check file permissions

### Issue: Clipboard hotkey (Ctrl+Alt+C) doesn't work
**Solutions:**
1. Check hotkey isn't conflicting
2. Try different hotkey combination
3. Restart AI Hub

---

## 🎙️ Voice Features Issues

### Issue: Voice features don't work
**Solutions:**
1. **Install voice dependencies:**
   ```bash
   pip install -r requirements-voice.txt
   ```

2. **Check microphone permissions:**
   - Windows Settings → Privacy → Microphone
   - Allow desktop apps to access microphone

3. **Test microphone:**
   - Windows Sound Settings
   - Test recording device

### Issue: Text-to-speech not working
**Solutions:**
1. Install edge-tts:
   ```bash
   pip install edge-tts
   ```

2. Check speakers/headphones connected
3. Check Windows volume settings

---

## 🔍 Search Scraper Issues

### Issue: Getting banned from search engines
**Solutions:**
1. Use fewer pages (1-2 max)
2. Enable proxy
3. Add delays (5+ seconds)
4. Use less frequently
5. See [Search Scraper Guide](../SEARCH_SCRAPER_GUIDE.md)

### Issue: No results returned
**Solutions:**
1. Check internet connection
2. Try different search engine
3. Simplify search query
4. Check if search engine is accessible

---

## 🪟 System Tray Issues

### Issue: Can't find system tray icon
**Solutions:**
1. Look bottom-right corner near clock
2. Click ^ arrow to show hidden icons
3. Check app is actually running:
   ```bash
   tasklist | findstr python
   ```

### Issue: Clicking X closes app completely
**Expected behavior:**
- X should minimize to tray
- If it closes completely, that's a bug
- Use `startup_ai_hub.bat` to restart

---

## 🔄 Auto-Start Issues

### Issue: App doesn't start with Windows
**Solutions:**
1. **Re-run setup:**
   ```bash
   setup_autostart.bat
   ```

2. **Check startup folder:**
   - Press Win+R
   - Type: `shell:startup`
   - Look for AI Hub shortcut

3. **Remove and re-add:**
   ```bash
   remove_autostart.bat
   setup_autostart.bat
   ```

---

## 💾 Installation Issues

### Issue: "Module not found" errors
**Solutions:**
1. **Reinstall all dependencies:**
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

2. **Check Python version:**
   ```bash
   python --version
   # Must be 3.10+
   ```

3. **Use virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Issue: pywin32 installation fails
**Solutions:**
```bash
pip install pywin32
python venv\Scripts\pywin32_postinstall.py -install
```

### Issue: Permission errors during install
**Solutions:**
1. Run PowerShell as Administrator
2. Or use `--user` flag:
   ```bash
   pip install -r requirements.txt --user
   ```

---

## 🐛 General Debugging

### Get detailed error information:
```bash
# Run with full output
python -m ai_hub.app

# Check what's running
tasklist | findstr python

# Check installed packages
pip list

# Check Python path
python -c "import sys; print(sys.executable)"
```

### Reset to defaults:
```bash
# Backup current settings
copy settings.ini settings.ini.backup

# Delete config files
del config\*.json

# Restart AI Hub
startup_ai_hub.bat
```

### Clean reinstall:
```bash
# Uninstall
pip uninstall ai-hub

# Remove cache
pip cache purge

# Reinstall
pip install -e ".[voice]"
```

---

## 🆘 Still Having Issues?

### Before asking for help:
1. ✅ Check this troubleshooting guide
2. ✅ Read the [FAQ](FAQ.md)
3. ✅ Check [GitHub Issues](https://github.com/yourusername/AI-HUB/issues)
4. ✅ Try clean reinstall

### When reporting issues:
Include:
- **OS version** (Windows 10/11, Linux distro)
- **Python version** (`python --version`)
- **AI Hub version** (check pyproject.toml)
- **Full error message** (copy from console)
- **Steps to reproduce**
- **What you've tried**

### Get help:
1. Search [existing issues](https://github.com/yourusername/AI-HUB/issues)
2. Open a [new issue](https://github.com/yourusername/AI-HUB/issues/new)
3. Use the bug report template

---

## 🔧 Advanced Troubleshooting

### Enable debug logging:
Edit `src/ai_hub/app.py` and add:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check specific modules:
```python
# Test imports
python -c "import PySide6; print('PySide6 OK')"
python -c "import keyboard; print('keyboard OK')"
python -c "import pyautogui; print('pyautogui OK')"
python -c "import requests; print('requests OK')"
```

### Test mouse automation separately:
```python
python -c "from ai_hub.services.mouse_automation import get_mouse_position; print(get_mouse_position())"
```

---

**Most issues can be fixed by reinstalling dependencies or checking the API key!**

# 🤖 AI Hub - Your Personal AI Assistant

**Version 0.2.0** - Now with Voice Capabilities! 🎙️

A powerful, voice-enabled desktop AI assistant that works everywhere. Create custom shortcuts, transcribe audio/video, and interact with AI using your voice - all running locally on your machine.

---

## ✨ Features

### 🎙️ Voice Assistant ("Jarvis Mode")
- **Text-to-Speech**: Human-like neural voices (Microsoft Azure)
- **Speech-to-Text**: Local transcription with faster-whisper
- **Video Transcription**: Drop MP4/MP3 files → Get full text
- **Voice Recording**: Capture and transcribe from microphone
- **5+ Voice Options**: Male/Female, US/UK/Australian accents

### ⚡ Smart Shortcuts
- **Visual Manager**: AHK-style GUI for creating shortcuts
- **Global Hotkeys**: Work in any app (Chrome, Notepad, Slack, etc.)
- **AI Rewriting**: Select text → Press hotkey → AI transforms it
- **Text Snippets**: Quick insertion of common phrases
- **Program Launchers**: Open apps with keyboard shortcuts

### 🤖 AI Integration
- **OpenAI API**: GPT-4o-mini for fast, cheap AI processing
- **Custom Prompts**: Create reusable AI instructions
- **Grammar Fixing**: Instant text correction
- **Tone Changing**: Professional, casual, simplified, etc.
- **Summarization**: Condense long text instantly

### 🔧 Automation
- **Hotstrings**: Type abbreviations → Auto-expand
- **Clipboard History**: Track and reuse copied text
- **Background Operation**: Runs silently in system tray
- **Auto-Start**: Launch on Windows boot

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
# Core features
pip install -e .

# Voice features (optional)
pip install edge-tts faster-whisper sounddevice scipy numpy pygame
# Or run: install_voice.bat
```

### 2. Configure API Key
Edit `settings.ini`:
```ini
[openai]
api_key = sk-proj-YOUR_KEY_HERE
```

### 3. Launch
```bash
# With console (for debugging)
run_ai_hub.bat

# Silent mode (background)
Start_AI_Hub.bat
```

### 4. Create Your First Shortcut
1. Open **⚡ Shortcuts** tab
2. Create a `Ctrl+Space` hotkey
3. Action: **AI Rewrite**
4. Output: `Fix all grammar and spelling errors`
5. Click **💾 Save**
6. Restart AI Hub

### 5. Test It!
1. Open Notepad
2. Type messy text: `this is a test with bad grammer`
3. Select text (Ctrl+A)
4. Press `Ctrl+Space`
5. Watch AI fix it! ✨

---

## 📚 Documentation

### Getting Started:
- **[QUICK_SETUP.md](QUICK_SETUP.md)** - 5-minute setup guide
- **[SHORTCUTS_MANAGER_GUIDE.md](SHORTCUTS_MANAGER_GUIDE.md)** - Complete shortcuts guide
- **[VOICE_SETUP_GUIDE.md](VOICE_SETUP_GUIDE.md)** - Voice features guide

### Reference:
- **[✨_SYSTEM_COMPLETE.md](✨_SYSTEM_COMPLETE.md)** - Complete system overview
- **[🎙️_VOICE_SYSTEM_READY.md](🎙️_VOICE_SYSTEM_READY.md)** - Voice system details
- **[SETUP_AND_STARTUP.md](SETUP_AND_STARTUP.md)** - Detailed setup

---

## 🎯 Use Cases

### Personal Productivity
```
✅ Grammar checker (Ctrl+Space)
✅ Email templates (Ctrl+Alt+1/2/3)
✅ Quick app launchers
✅ Voice memos to text
```

### Writing Assistant
```
✅ Change tone (professional/casual)
✅ Summarize long text
✅ Expand bullet points
✅ Simplify complex text
```

### Content Creation
```
✅ Transcribe videos for subtitles
✅ Convert podcasts to text
✅ Meeting notes from recordings
✅ Voice-to-text drafting
```

### Developer Tools
```
✅ Code snippet insertion
✅ Open IDEs/terminals
✅ Run build scripts
✅ Documentation generation
```

---

## 🎨 Screenshots

### Shortcuts Manager
Visual editor for creating custom hotkeys and text replacements:
- Left panel: Create/edit shortcuts
- Right panel: Library of saved shortcuts
- Three action types: Send Text, Run Program, AI Rewrite

### Voice Assistant
Text-to-speech and speech-to-text interface:
- Type text → Speak with neural voices
- Record audio → Get instant transcription
- Drop video files → Extract full text

### AI Chat
Direct conversation with AI:
- Multi-turn conversations
- Context awareness
- Copy responses instantly

---

## 🔧 System Requirements

- **OS**: Windows 10/11 (tested)
- **Python**: 3.10 or higher
- **RAM**: 200MB (with voice features)
- **Disk**: 100MB (+ 40MB for Whisper model)
- **Internet**: 
  - Required for AI features (OpenAI API)
  - Required for TTS (edge-tts)
  - NOT required for STT (runs locally)

---

## 🎙️ Voice Features

### Text-to-Speech (TTS)
- **Technology**: Microsoft Azure Neural Voices
- **Quality**: Human-like, natural prosody
- **Speed**: Near real-time
- **Cost**: FREE (no API key needed)
- **Voices**: 5+ options (male/female, various accents)

### Speech-to-Text (STT)
- **Technology**: faster-whisper (optimized Whisper)
- **Quality**: State-of-the-art accuracy
- **Speed**: ~5 seconds per minute of audio
- **Privacy**: Runs locally, no internet required
- **Formats**: MP3, WAV, MP4, M4A, OGG, FLAC

---

## 💡 Example Shortcuts

### Grammar Fixer (Essential!)
```
Hotkey: Ctrl+Space
Action: AI Rewrite
Output: Fix all grammar, spelling, and punctuation errors.
```

### Professional Tone
```
Hotkey: Ctrl+Shift+P
Action: AI Rewrite
Output: Rewrite this in a professional business tone.
```

### Summarize
```
Hotkey: Ctrl+Shift+S
Action: AI Rewrite
Output: Summarize this in 2-3 sentences.
```

### Email Signature
```
Hotkey: Ctrl+Alt+S
Action: Send Text
Output: Best regards,
Your Name
your.email@example.com
```

### Open Notepad
```
Hotkey: Ctrl+Alt+N
Action: Run Program
Output: notepad.exe
```

---

## 🏗️ Architecture

```
AI Hub/
├── Core System
│   ├── PySide6 GUI
│   ├── Global hotkey engine
│   ├── Hotstring engine
│   └── Settings management
│
├── AI Services
│   ├── OpenAI client
│   ├── Prompt manager
│   ├── Text selection/replacement
│   └── Multi-API support
│
├── Voice System
│   ├── edge-tts (TTS)
│   ├── faster-whisper (STT)
│   ├── Audio recording
│   └── Audio playback
│
└── UI Tabs
    ├── Chat
    ├── Voice
    ├── Shortcuts Manager
    ├── Prompts
    └── Spelling
```

---

## 🛠️ Development

### Project Structure
```
src/ai_hub/
├── app.py                  # Entry point
├── config.py               # Settings loader
├── ui/
│   ├── main_window.py      # Main window
│   └── tabs/               # UI tabs
├── services/
│   ├── openai_client.py    # AI client
│   ├── audio_engine.py     # Voice engine
│   └── selection.py        # Text handling
└── hotkeys/
    ├── global_hotkeys.py   # Hotkey manager
    └── hotstrings.py       # Text replacement
```

### Adding Features
1. Create service in `services/`
2. Create UI tab in `ui/tabs/`
3. Register in `main_window.py`
4. Update documentation

---

## 🐛 Troubleshooting

### Shortcuts not working?
1. Restart AI Hub after creating shortcuts
2. Check for hotkey conflicts with Windows
3. Run as Administrator if needed

### Voice not working?
```bash
# Install voice dependencies
pip install edge-tts faster-whisper pygame

# Or use the installer
install_voice.bat
```

### API errors?
1. Check `settings.ini` for valid API key
2. Verify internet connection
3. Check OpenAI account has credits

### Import errors?
```bash
# Reinstall dependencies
pip install -e . --upgrade
```

---

## 🚀 Roadmap

### v0.3.0 (Next)
- [ ] Voice commands ("Fix this email")
- [ ] Continuous listening mode
- [ ] Wake word detection ("Hey Jarvis")
- [ ] Voice-triggered shortcuts

### v0.4.0 (Future)
- [ ] Multi-language support
- [ ] Voice cloning
- [ ] Custom AI models (Claude, local LLMs)
- [ ] Shortcut import/export
- [ ] Plugin system

---

## 📝 License

MIT License - Feel free to use, modify, and distribute.

---

## 🙏 Credits

Built with:
- **PySide6** - GUI framework
- **edge-tts** - Neural text-to-speech
- **faster-whisper** - Optimized speech-to-text
- **keyboard** - Global hotkey support
- **OpenAI** - AI language models

---

## 📞 Support

- **Documentation**: See `docs/` folder
- **Issues**: Check console output with `run_ai_hub.bat`
- **Setup Help**: Read `QUICK_SETUP.md`
- **Voice Help**: Read `VOICE_SETUP_GUIDE.md`

---

## 🎉 Get Started Now!

1. **Install**: `pip install -e .`
2. **Configure**: Add API key to `settings.ini`
3. **Launch**: `run_ai_hub.bat`
4. **Create**: Your first shortcut
5. **Enjoy**: Your personal AI assistant!

**Welcome to the future of personal productivity! 🚀**

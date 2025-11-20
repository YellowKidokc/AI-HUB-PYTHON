# 🚀 AI Hub - Complete Setup Guide

**Welcome to AI Hub v0.2.0!** Your personal AI assistant with voice capabilities.

---

## ⚡ Super Quick Start (5 Minutes)

### Step 1: Install Everything
```bash
# Install core features
pip install -e .

# Install voice features
pip install edge-tts faster-whisper sounddevice scipy numpy pygame
```

**Or use the installers:**
- Core: Already installed if you can see this!
- Voice: Double-click `install_voice.bat`

### Step 2: Add Your API Key
1. Get key from: https://platform.openai.com/api-keys
2. Edit `settings.ini`
3. Replace `sk-your-api-key-here` with your key

### Step 3: Launch
Double-click: `run_ai_hub.bat`

### Step 4: Test Voice
1. Click **🎙️ Voice** tab
2. Wait for "Audio Engine Ready"
3. Type: "Hello, AI Hub is online."
4. Click **🔊 Speak Text**
5. Hear the magic! ✨

### Step 5: Create First Shortcut
1. Click **⚡ Shortcuts** tab
2. Fill in:
   - Type: `Hotkey`
   - Action: `AI Rewrite`
   - Modifiers: Check `Ctrl`
   - Trigger: `space`
   - Description: `Fix grammar`
   - Output: `Fix all grammar and spelling errors`
3. Click **💾 Save**
4. Restart AI Hub
5. Test: Select text anywhere → Press Ctrl+Space

---

## 📚 What Can You Do?

### 🎙️ Voice Features
- **Speak Text**: Type → AI speaks with human voice
- **Transcribe Audio**: MP3/WAV → Text
- **Transcribe Video**: MP4 → Full transcript
- **Record Voice**: Microphone → Text
- **5+ Voices**: Choose male/female, accents

### ⚡ Shortcuts
- **Grammar Fix**: Ctrl+Space (essential!)
- **Change Tone**: Professional, casual, simplified
- **Text Snippets**: Email signatures, templates
- **Program Launchers**: Open apps instantly
- **AI Transformations**: Summarize, expand, translate

### 💬 Chat
- **Direct AI Chat**: Ask questions, get answers
- **Context Aware**: Remembers conversation
- **Copy Results**: One-click clipboard

### 📝 Prompts
- **Reusable Instructions**: Save common AI tasks
- **Quick Access**: Run on selected text
- **Customizable**: Create your own prompts

---

## 📖 Documentation Guide

### For Beginners:
1. **[QUICK_SETUP.md](QUICK_SETUP.md)** - Start here!
2. **[SHORTCUTS_MANAGER_GUIDE.md](SHORTCUTS_MANAGER_GUIDE.md)** - Create shortcuts
3. **[VOICE_SETUP_GUIDE.md](VOICE_SETUP_GUIDE.md)** - Voice features

### For Advanced Users:
1. **[✨_SYSTEM_COMPLETE.md](✨_SYSTEM_COMPLETE.md)** - Complete overview
2. **[🎙️_VOICE_SYSTEM_READY.md](🎙️_VOICE_SYSTEM_READY.md)** - Voice details
3. **[README.md](README.md)** - Full documentation

### Quick Reference:
- `settings.ini` - Configuration
- `config/shortcuts.json` - Your shortcuts
- `config/shortcuts_examples.json` - Example shortcuts

---

## 🎯 Essential Shortcuts to Create

### 1. Grammar Fixer (MUST HAVE!)
```
Hotkey: Ctrl+Space
Action: AI Rewrite
Output: Fix all grammar, spelling, and punctuation errors. Keep the tone.
```
**Use**: Select text → Ctrl+Space → Fixed!

### 2. Professional Tone
```
Hotkey: Ctrl+Shift+P
Action: AI Rewrite
Output: Rewrite this in a professional business tone.
```

### 3. Summarize
```
Hotkey: Ctrl+Shift+S
Action: AI Rewrite
Output: Summarize this in 2-3 sentences.
```

### 4. Email Signature
```
Hotkey: Ctrl+Alt+S
Action: Send Text
Output: Best regards,
Your Name
your.email@example.com
```

### 5. Open Notepad
```
Hotkey: Ctrl+Alt+N
Action: Run Program
Output: notepad.exe
```

---

## 🎙️ Voice Examples

### Test Phrases
Try these to test voice quality:

```
"Good morning, sir. All systems operational."
"Processing your request. Please stand by."
"Task completed successfully."
"Welcome to AI Hub, your personal assistant."
```

### Transcription Test
1. Record a voice memo on your phone
2. Transfer to computer
3. Open Voice tab → Select File
4. Get instant transcript!

---

## 🔧 Troubleshooting

### "Python not found"
Install Python 3.10+ from: https://www.python.org/downloads/  
✅ Check "Add Python to PATH" during install

### "Module not found"
```bash
pip install -e .
pip install edge-tts faster-whisper pygame
```

### "API key invalid"
1. Check `settings.ini`
2. Key should start with `sk-proj-` or `sk-`
3. Get new key: https://platform.openai.com/api-keys

### Shortcuts not working
1. **Restart AI Hub** after creating shortcuts
2. Check for conflicts with Windows hotkeys
3. Try running as Administrator

### Voice not working
```bash
# Run the voice installer
install_voice.bat

# Or manually:
pip install edge-tts faster-whisper pygame
```

### "Loading AI Models" forever
- First time downloads Whisper model (~40MB)
- Takes ~10 seconds
- Subsequent launches are instant

---

## 🚀 Auto-Start Setup

Want AI Hub to start automatically when Windows boots?

### Option 1: PowerShell Script (Recommended)
1. Right-click: `install_startup.ps1`
2. Select: "Run with PowerShell"
3. Wait for: ✅ Success
4. Restart computer

### Option 2: Manual
1. Press `Win+R`
2. Type: `shell:startup`
3. Create shortcut to `Start_AI_Hub.bat`
4. Restart computer

---

## 💡 Pro Tips

### 1. Use Ctrl+Space for Everything
Make this your muscle memory:
- Select text
- Press Ctrl+Space
- AI fixes it instantly

### 2. Create Context-Specific Shortcuts
```
Ctrl+1 → "Make casual"
Ctrl+2 → "Make professional"
Ctrl+3 → "Summarize"
Ctrl+4 → "Expand"
```

### 3. Voice Confirmations
Add voice feedback to shortcuts:
```python
from ai_hub.services.audio_engine import quick_speak
quick_speak("Done")
```

### 4. Batch Transcription
Transcribe multiple files:
```python
from ai_hub.services.audio_engine import quick_transcribe
text = quick_transcribe("meeting.mp3")
```

### 5. Email Templates
Create shortcuts for common emails:
```
Ctrl+Alt+1 → "Thanks for reaching out..."
Ctrl+Alt+2 → "Please see attached..."
Ctrl+Alt+3 → Full signature
```

---

## 🎯 Common Workflows

### Workflow 1: Fix Email
```
1. Write draft email (with typos)
2. Select all (Ctrl+A)
3. Press Ctrl+Space
4. AI fixes grammar
5. Send!
```

### Workflow 2: Meeting Notes
```
1. Record meeting on phone
2. Transfer MP3 to computer
3. Open Voice tab
4. Select file
5. Get full transcript
6. Copy to notes app
```

### Workflow 3: Video Subtitles
```
1. Download video (MP4)
2. Open Voice tab
3. Drop video file
4. Get full transcript
5. Use for subtitles
```

### Workflow 4: Voice Memo
```
1. Click "Record (5s)"
2. Speak your note
3. Get instant text
4. Copy to clipboard
```

---

## 📊 What You Get

### Core Features:
✅ AI Chat  
✅ Voice Assistant (TTS + STT)  
✅ Visual Shortcuts Manager  
✅ Global Hotkeys  
✅ AI Text Rewriting  
✅ Hotstrings  
✅ Auto-Start  

### Voice Capabilities:
✅ Human-like TTS (5+ voices)  
✅ Local STT (private)  
✅ Video transcription  
✅ Microphone recording  
✅ Multi-format support  

### Automation:
✅ Custom hotkeys  
✅ Text snippets  
✅ Program launchers  
✅ AI transformations  

---

## 🎓 Learning Path

### Day 1: Setup
- [ ] Install dependencies
- [ ] Add API key
- [ ] Test voice
- [ ] Create first shortcut

### Day 2: Customize
- [ ] Create 5 essential shortcuts
- [ ] Test in different apps
- [ ] Try different voices
- [ ] Transcribe a file

### Week 1: Master
- [ ] Set up auto-start
- [ ] Create email templates
- [ ] Build AI workflows
- [ ] Share with friends

---

## 🌟 Next Steps

1. **Read**: [QUICK_SETUP.md](QUICK_SETUP.md) for detailed setup
2. **Explore**: [SHORTCUTS_MANAGER_GUIDE.md](SHORTCUTS_MANAGER_GUIDE.md) for examples
3. **Voice**: [VOICE_SETUP_GUIDE.md](VOICE_SETUP_GUIDE.md) for voice features
4. **Build**: Your first 5 shortcuts
5. **Enjoy**: Your personal AI assistant!

---

## 🎉 You're Ready!

Your AI Hub includes:

🤖 **AI-powered** text transformation  
🎙️ **Voice-enabled** assistant  
⚡ **Global hotkeys** that work everywhere  
🔒 **Private** - runs on your machine  
🆓 **Free** - except OpenAI API usage  

**Welcome to the future! 🚀**

---

## 📞 Need Help?

- **Setup Issues**: Check `QUICK_SETUP.md`
- **Shortcuts Help**: Check `SHORTCUTS_MANAGER_GUIDE.md`
- **Voice Issues**: Check `VOICE_SETUP_GUIDE.md`
- **Console Errors**: Run `run_ai_hub.bat` to see logs

---

**Built with ❤️ by the AI Hub team**

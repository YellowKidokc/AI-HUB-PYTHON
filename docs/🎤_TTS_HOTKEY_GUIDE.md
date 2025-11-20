# 🎤 Instant Text-to-Speech Hotkey Guide

## 🎉 What's New

Your AI Hub now has **instant TTS from anywhere** with:

1. **🎙️ Brian Voice** - Your favorite multilingual voice (now default!)
2. **⚡ Ctrl+CapsLock+A** - Instant TTS hotkey (select text → speak!)
3. **🎮 Floating Player** - Draggable mini-player with play/pause/stop controls

---

## ⚡ The Magic Hotkey: Ctrl+CapsLock+A

### How It Works:
1. **Select text** anywhere (Chrome, Notepad, Word, Slack, etc.)
2. **Hold Ctrl + CapsLock** and press **A**
3. **Hear it spoken** instantly with Brian's voice!
4. **Floating player appears** with controls

### Example Workflow:
```
1. Reading an article in Chrome
2. Select a paragraph
3. Press Ctrl+CapsLock+A
4. Listen while doing other things
5. Use floating player to pause/resume
```

---

## 🎮 Floating Player Controls

### What It Does:
- **Appears automatically** when TTS starts
- **Stays on top** of all windows
- **Draggable** - Move it anywhere
- **Always accessible** - Never loses focus

### Controls:
- **▶️ Play/Pause** - Toggle playback
- **⏹️ Stop** - Stop and reset
- **× Close** - Hide player (doesn't stop audio)
- **Drag** - Click title bar and drag to move

### Status Indicators:
- 🔊 Playing... - Audio is playing
- ⏸️ Paused - Audio is paused
- ✅ Finished - Playback complete
- Ready - Waiting for input

---

## 🎙️ Brian Voice (Your Favorite!)

### Why Brian?
- **Multilingual** - Handles multiple languages naturally
- **Natural prosody** - Sounds human, not robotic
- **Clear pronunciation** - Easy to understand
- **Consistent quality** - Reliable across all text types

### Now Default:
Brian is now the default voice in AI Hub. You can still change it in the Voice tab if needed.

### Other Voices Available:
1. Brian Multilingual ⭐ (Default)
2. Guy - Professional male
3. Aria - Friendly female
4. Jenny - Warm female
5. Sonia - British female
6. Natasha - Australian female

---

## 🚀 Quick Start

### First Time Setup:
1. **Launch AI Hub**: `run_ai_hub.bat`
2. **Wait for loading**: Voice tab shows "Audio Engine Ready"
3. **Test the hotkey**:
   - Open Notepad
   - Type: "Hello, this is a test of Brian's voice."
   - Select the text
   - Press **Ctrl+CapsLock+A**
   - Hear Brian speak!

### Daily Use:
```
Reading email → Select text → Ctrl+CapsLock+A → Listen
Reading article → Select paragraph → Ctrl+CapsLock+A → Listen
Reviewing document → Select section → Ctrl+CapsLock+A → Listen
```

---

## 💡 Use Cases

### 1. **Reading Long Articles**
```
Problem: Eyes tired from reading
Solution: Select paragraphs → Ctrl+CapsLock+A → Listen while resting
```

### 2. **Proofreading**
```
Problem: Need to catch errors
Solution: Select text → Ctrl+CapsLock+A → Hear mistakes you missed
```

### 3. **Multitasking**
```
Problem: Need to read while doing other things
Solution: Select text → Ctrl+CapsLock+A → Listen while working
```

### 4. **Learning Languages**
```
Problem: Want to hear pronunciation
Solution: Select foreign text → Ctrl+CapsLock+A → Hear native pronunciation
```

### 5. **Accessibility**
```
Problem: Visual impairment or dyslexia
Solution: Select any text → Ctrl+CapsLock+A → Hear it spoken clearly
```

---

## 🎯 Pro Tips

### Tip 1: Use with AI Rewriting
```
1. Write draft email
2. Select text → Ctrl+Space (fix grammar)
3. Select result → Ctrl+CapsLock+A (hear it)
4. Perfect email!
```

### Tip 2: Pause for Notes
```
1. Select long text → Ctrl+CapsLock+A
2. Use floating player to pause
3. Take notes
4. Resume when ready
```

### Tip 3: Position Player Once
```
1. Move floating player to your preferred corner
2. It remembers position
3. Always appears in same spot
```

### Tip 4: Quick Stop
```
- Press ⏹️ Stop button to immediately stop
- Or close floating player (audio continues)
- Or press Ctrl+CapsLock+A again with new text
```

### Tip 5: Multilingual Content
```
Brian handles multiple languages:
- English (all accents)
- Spanish
- French
- German
- And more!
```

---

## 🔧 Technical Details

### Hotkey Combination:
- **Ctrl+CapsLock+A**
- Works globally (all apps)
- Non-intrusive (doesn't interfere with other shortcuts)
- CapsLock acts as modifier when held

### Audio Engine:
- **Voice**: Brian Multilingual Neural
- **Quality**: 24kHz, high-quality neural synthesis
- **Latency**: ~1 second for short text
- **Format**: MP3 (temporary file)

### Floating Player:
- **Framework**: PySide6 (Qt)
- **Position**: Bottom-right by default
- **Size**: 200x120 pixels
- **Features**: Draggable, always-on-top, frameless

---

## 🐛 Troubleshooting

### Hotkey not working?
```bash
# Check if AI Hub is running
# Look for "TTS Hotkey registered" in console

# If not registered:
1. Close AI Hub
2. Run: run_ai_hub.bat
3. Look for: "✅ TTS Hotkey registered: Ctrl+CapsLock+A"
```

### No audio?
```bash
# Check voice dependencies
pip show edge-tts pygame

# Reinstall if needed
pip install edge-tts pygame --upgrade
```

### Floating player not appearing?
```bash
# Check if audio engine is ready
# Open Voice tab → Should say "Audio Engine Ready"

# If not ready:
1. Wait 10 seconds for Whisper to load
2. Or restart AI Hub
```

### Wrong voice?
```bash
# Change in Voice tab:
1. Open Voice tab
2. Select "Brian Multilingual" from dropdown
3. Test with "Speak Text" button
```

### CapsLock key issues?
```bash
# Alternative hotkey (if CapsLock doesn't work):
# Edit main_window.py, line 92:
keyboard.add_hotkey(
    "ctrl+shift+a",  # Use Ctrl+Shift+A instead
    self._trigger_tts_from_selection,
    suppress=False,
    trigger_on_release=True,
)
```

---

## 🎨 Customization

### Change Hotkey:
Edit `src/ai_hub/ui/main_window.py` line 92:
```python
keyboard.add_hotkey(
    "ctrl+capslock+a",  # Change this
    self._trigger_tts_from_selection,
    suppress=False,
    trigger_on_release=True,
)
```

**Options:**
- `"ctrl+shift+a"` - Ctrl+Shift+A
- `"ctrl+alt+s"` - Ctrl+Alt+S
- `"win+s"` - Windows+S
- `"ctrl+space"` - Ctrl+Space (if not used for grammar)

### Change Default Voice:
Edit `src/ai_hub/services/audio_engine.py` line 47:
```python
VOICE = "en-US-BrianMultilingualNeural"  # Change this
```

### Customize Floating Player:
Edit `src/ai_hub/ui/widgets/floating_player.py`:
- Change size (line 163): `self.setFixedSize(200, 120)`
- Change position (line 168): Modify `_position_bottom_right()`
- Change colors: Modify stylesheet (lines 26-63)

---

## 🎯 Keyboard Shortcuts Summary

### AI Hub Hotkeys:
| Hotkey | Action |
|--------|--------|
| **Ctrl+CapsLock+A** | Speak selected text (TTS) |
| **Ctrl+Space** | Fix grammar with AI |
| **Ctrl+Shift+K** | Open prompt navigator |
| **Ctrl+Alt+Shift+K** | Focus AI Hub window |
| **Ctrl+Alt+H** | Toggle hotstrings |

### Floating Player:
| Button | Action |
|--------|--------|
| ▶️/⏸️ | Play/Pause |
| ⏹️ | Stop |
| × | Close player |
| Drag title | Move player |

---

## 🌟 What Makes This Special

### vs Browser Extensions:
✅ **Works everywhere** - Not just in browser  
✅ **Offline capable** - No internet for playback  
✅ **Better voice** - Neural TTS, not robotic  
✅ **Integrated** - Works with AI features  

### vs Built-in TTS:
✅ **Higher quality** - Microsoft Azure neural voices  
✅ **More control** - Floating player with pause/resume  
✅ **Faster** - Optimized for instant playback  
✅ **Customizable** - Choose your favorite voice  

### vs Other Tools:
✅ **One hotkey** - No menu navigation  
✅ **Visual feedback** - Floating player shows status  
✅ **Non-blocking** - Continue working while listening  
✅ **Free** - No subscription required  

---

## 📊 Performance

### Speed:
- **Hotkey response**: Instant
- **Audio generation**: ~1 second
- **Playback start**: Immediate
- **Total latency**: ~1-2 seconds

### Quality:
- **Sample rate**: 24kHz
- **Bitrate**: 128kbps MP3
- **Voice quality**: Neural (human-like)
- **Clarity**: Excellent

---

## 🎉 You're Ready!

Your AI Hub now has:

🎙️ **Brian voice** as default  
⚡ **Ctrl+CapsLock+A** instant TTS  
🎮 **Floating player** with controls  
🌍 **Works everywhere** globally  
🔊 **High quality** neural voices  

**Try it now:**
1. Select this text
2. Press Ctrl+CapsLock+A
3. Hear Brian read it!

---

**Built with ❤️ using edge-tts and PySide6**

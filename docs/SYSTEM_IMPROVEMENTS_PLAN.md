# 🚀 System Improvements Plan

## What You Asked For

You identified several issues and requested major improvements:

### 1. ✅ CHECKBOX VISIBILITY (FIXED)
**Problem:** Checkboxes disappear when checked, no visible checkmark
**Solution:** 
- Larger checkboxes (20x20px)
- Bigger font (12pt bold)
- Styled checkbox indicators
- Clear visual feedback

**File:** `src/ai_hub/ui/improved_manager_window.py`

### 2. ✅ BETTER HOTKEY DISPLAY (FIXED)
**Problem:** Shows "^!L" - cryptic symbols
**Solution:**
- Display as "CTRL + ALT + L" - readable
- Large font (14pt bold, blue)
- Built hotkey display box
- Updates as you select modifiers

**File:** `src/ai_hub/ui/improved_manager_window.py`
**Helper:** `HotkeyDisplayHelper` class converts formats

### 3. ⏳ SYSTEM PROMPT MANAGER (NEXT)
**What:** Side panel to manage system prompts
**Features:**
- Switch between custom system prompts
- Default system prompt about David Lowe
- Save/load different personalities
- Use across entire app (chat, spelling, etc.)

**Implementation:**
- Add side panel to chat tab
- Store prompts in JSON
- Dropdown selector
- Edit/save/delete prompts

### 4. ⏳ MULTI-API SUPPORT (IN PROGRESS)
**What:** Support OpenAI + Claude + others
**Files:**
- `src/ai_hub/services/multi_api_client.py` ✅ Created
- Support for:
  - OpenAI (GPT-4, GPT-4o-mini, etc.)
  - Claude (Anthropic) - newest models
  - Custom endpoints
  
**Configuration:**
- Add API provider selector to settings
- Store both API keys
- Switch providers per-request or globally

### 5. ⏳ WHISPER INTEGRATION (FUTURE)
**What:** Speech-to-text, Text-to-speech, Translation
**Components:**
- **Speech-to-Text:** Convert audio/MP3/video to text
- **Text-to-Speech:** Read text aloud to user
- **Translation:** Translate audio between languages

**Implementation:**
- Use OpenAI Whisper API for STT
- Use gTTS or pyttsx3 for TTS
- Add audio input UI
- Real-time transcription display

---

## Current Status

### ✅ COMPLETED

1. **Improved Hotkeys Manager** ✅
   - File: `src/ai_hub/ui/improved_manager_window.py`
   - Larger checkboxes with visible indicators
   - Readable hotkey display (CTRL+ALT+L format)
   - Better overall UI
   - Can launch with: `python -c "from src.ai_hub.ui.improved_manager_window import ImprovedHotkeysManagerWindow; ..."`

2. **Multi-API Client** ✅
   - File: `src/ai_hub/services/multi_api_client.py`
   - OpenAI support (GPT-4, GPT-4o-mini, etc.)
   - Claude/Anthropic support
   - Custom endpoint support
   - Ready to integrate

### ⏳ IN PROGRESS

1. **System Prompt Manager**
   - Side panel for chat tab
   - Manage multiple system prompts
   - Save/load/delete

2. **Chat History Display**
   - Show conversation history
   - Already has it (QTextEdit)
   - Just need to verify

### 🔮 FUTURE (NOT STARTED)

1. **Whisper Integration**
   - Speech-to-text
   - Text-to-speech
   - Translation

---

## Architecture Overview

### System Prompt Manager (Planned)
```
┌─────────────────────────────────────────────┐
│ Chat Tab                                    │
├─────────────────────┬─────────────────────┤
│ System Prompt Panel │ Chat History        │
├─────────────────────┼─────────────────────┤
│ • Prompt Selector   │ User: "Hello"       │
│   [Dropdown ▼]     │ AI: "Hi, I'm..."   │
│                     │ [scrollable]        │
│ • Edit System       │                     │
│   Prompt            │                     │
│ [________________]  │                     │
│ [________________]  │ Message Input:      │
│ [________________]  │ [_______________]  │
│                     │ [Send]              │
│ • Save Prompt       │                     │
│ • Load Prompt       │                     │
│ • Delete Prompt     │                     │
└─────────────────────┴─────────────────────┘
```

### Multi-API Configuration
```
Settings:
├─ API Provider: [OpenAI ▼] / [Claude ▼]
├─ OpenAI Settings:
│  ├─ API Key: [sk-...]
│  ├─ Model: [gpt-4o-mini ▼]
│  └─ Endpoint: [https://api.openai.com/v1/chat/completions]
├─ Claude Settings:
│  ├─ API Key: [...]
│  ├─ Model: [claude-3-5-sonnet ▼]
│  └─ Endpoint: [https://api.anthropic.com/v1/messages]
└─ Active Provider: [OpenAI ▼] (for requests)
```

### Whisper Integration
```
Chat Tab:
├─ Text Input: [_____________________]
├─ Audio Input: [🎤 Record] [Upload MP3/Audio]
├─ Actions:
│  ├─ Transcribe Audio → Text
│  ├─ Translate Audio
│  └─ Read Response Aloud
└─ History: [Chat/Audio mixed timeline]
```

---

## Next Steps (Priority Order)

### 1. System Prompt Manager (HIGH PRIORITY)
**Why:** Core to your workflow
**Effort:** Medium (2-3 hours)
**Impact:** High - affects all chat operations

**Tasks:**
- [ ] Create PromptManager service
- [ ] Add side panel to chat tab
- [ ] Implement prompt switching
- [ ] Save/load prompts
- [ ] Default prompt setup (David Lowe bio)

### 2. Multi-API Integration (HIGH PRIORITY)  
**Why:** Flexibility and options
**Effort:** Medium (1-2 hours)
**Impact:** High - use best model for each task

**Tasks:**
- [ ] Update settings.ini with API configs
- [ ] Add provider selector to settings UI
- [ ] Replace OpenAIClient with MultiAPIClient
- [ ] Update all services to use new client
- [ ] Test with both OpenAI and Claude

### 3. Whisper Integration (MEDIUM PRIORITY)
**Why:** Audio capabilities expand use cases
**Effort:** High (3-4 hours)
**Impact:** Medium-High - nice to have

**Tasks:**
- [ ] Add audio recording UI
- [ ] Implement OpenAI Whisper integration
- [ ] Add TTS support (pyttsx3 or gTTS)
- [ ] Implement translation
- [ ] Test with various audio formats

---

## Configuration Changes Needed

### settings.ini (Add)
```ini
[api_provider]
# active_provider: openai or claude
active_provider = openai

[openai]
api_key = sk-...
model = gpt-4o-mini
endpoint = https://api.openai.com/v1/chat/completions

[claude]
api_key = sk-ant-...
model = claude-3-5-sonnet-20241022
endpoint = https://api.anthropic.com/v1/messages

[system_prompts]
# Store available system prompts
default = "My name is David Lowe..."
```

---

## File Structure (Planned)

```
src/ai_hub/
├── services/
│   ├── multi_api_client.py        ✅ CREATED
│   ├── system_prompt_manager.py   ⏳ TODO
│   ├── whisper_handler.py         🔮 TODO
│   └── ...
├── ui/
│   ├── improved_manager_window.py ✅ CREATED
│   ├── chat_tab.py               (update)
│   └── ...
└── ...
```

---

## Dependencies to Add

```bash
# For Claude support (already in requests)
# requests >= 2.31

# For Text-to-Speech
pip install pyttsx3

# For Whisper transcription
# pip install openai (already have it)

# For better audio handling
pip install librosa soundfile
```

---

## Testing Checklist

### Hotkeys Manager
- [ ] Checkboxes show visible checked state
- [ ] Hotkey displays as CTRL+ALT+L format
- [ ] Can create hotkeys
- [ ] Can create hotstrings
- [ ] Can delete items

### Multi-API
- [ ] Can switch between OpenAI and Claude
- [ ] Both providers work correctly
- [ ] System prompts work with both
- [ ] No errors on API calls

### System Prompts
- [ ] Can add system prompt
- [ ] Can switch between prompts
- [ ] Prompt persists across chats
- [ ] Prompt affects all responses
- [ ] Can save as template

### Whisper
- [ ] Can record audio
- [ ] Can upload MP3
- [ ] Transcription works
- [ ] Translation works
- [ ] Text-to-speech works

---

## Timeline Estimate

| Component | Effort | Time Est. |
|-----------|--------|-----------|
| Hotkeys Manager UI | Done | ✅ |
| Multi-API Client | Done | ✅ |
| System Prompt Manager | High | 2-3h |
| Settings Integration | Medium | 1h |
| Whisper Integration | High | 3-4h |
| Testing & Polish | Medium | 1-2h |
| **TOTAL** | - | **7-11h** |

---

## Questions for You

Before I proceed, clarify:

1. **System Prompt Scope**
   - Should system prompt be per-tab or global?
   - Can it be different for chat vs spelling?
   - Should it support templates?

2. **API Provider**
   - Should user select provider in UI?
   - Or switch via settings?
   - Both available simultaneously?

3. **Whisper Priority**
   - How soon do you need audio?
   - Text-to-speech or transcription first?
   - Only for chat or for hotkeys too?

4. **Chat History**
   - Keep history in file?
   - Or session-only?
   - Export functionality?

---

## Ready When You Are!

Next action: Would you like me to:
1. **Build System Prompt Manager** (most impactful)
2. **Integrate Multi-API** (flexibility)
3. **Start Whisper** (audio features)
4. **All three** (full implementation)

Let me know what's most important! 🚀


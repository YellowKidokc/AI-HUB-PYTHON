# 🏗️ AI Hub Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERACTION LAYER                      │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  BATCH LAUNCHER: run_ai_hub.bat                           │  │
│  │  • Checks Python installation                             │  │
│  │  • Verifies dependencies                                  │  │
│  │  • Auto-installs missing packages                         │  │
│  │  • Launches application                                   │  │
│  │  • Shows diagnostics & error handling                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                ↓                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  TASKBAR SETUP: add_to_taskbar.bat                        │  │
│  │  • Creates Desktop & Start Menu shortcuts                 │  │
│  │  • Attempts automatic taskbar pinning                     │  │
│  │  • Uses setup_taskbar.ps1 PowerShell script               │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PYTHON APPLICATION                            │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   PySide6 GUI LAYER                       │  │
│  │                                                            │  │
│  │  ┌─────────────────────────────────────────────────────┐ │  │
│  │  │  MAIN WINDOW (main_window.py)                       │ │  │
│  │  │  • Window title: "AI Hub"                           │ │  │
│  │  │  • Size: 1000x720                                   │ │  │
│  │  │  • Dark theme (qdarktheme)                          │ │  │
│  │  │                                                     │ │  │
│  │  │  ┌─────────────────────────────────────────────┐   │ │  │
│  │  │  │ QTabWidget (Three Tabs)                     │   │ │  │
│  │  │  │                                             │   │ │  │
│  │  │  │  [1] CHAT TAB ────→ ChatTab (chat_tab.py) │   │ │  │
│  │  │  │      • Input field for user messages        │   │ │  │
│  │  │  │      • Send button to OpenAI               │   │ │  │
│  │  │  │      • Display AI responses                │   │ │  │
│  │  │  │      • Conversation history                │   │ │  │
│  │  │  │                                             │   │ │  │
│  │  │  │  [2] PROMPTS TAB → PromptsTab (prompts_tab.py) │ │  │
│  │  │  │      • View available prompts               │   │ │  │
│  │  │  │      • Manage prompt library                │   │ │  │
│  │  │  │      • Create custom prompts                │   │ │  │
│  │  │  │                                             │   │ │  │
│  │  │  │  [3] SPELLING TAB → SpellingTab (spelling_tab.py)│ │  │
│  │  │  │      • Input text to check                  │   │ │  │
│  │  │  │      • Grammar/spelling fixes                │   │ │  │
│  │  │  │      • AI-powered corrections               │   │ │  │
│  │  │  └─────────────────────────────────────────────┘   │ │  │
│  │  └─────────────────────────────────────────────────────┘ │  │
│  │                                                            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                ↓                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              SERVICES LAYER (services/)                  │  │
│  │                                                            │  │
│  │  ┌────────────────────────────────────────────────────┐ │  │
│  │  │ OpenAI Client (openai_client.py)                   │ │  │
│  │  │ • Handles API requests to OpenAI                   │ │  │
│  │  │ • Error handling & response parsing                │ │  │
│  │  │ • Graceful fallback if API key missing             │ │  │
│  │  └────────────────────────────────────────────────────┘ │  │
│  │                           ↓                              │  │
│  │          https://api.openai.com/v1/chat/completions     │  │
│  │                                                            │  │
│  │  ┌────────────────────────────────────────────────────┐ │  │
│  │  │ Prompt Manager (prompt_manager.py)                 │ │  │
│  │  │ • Manages prompt templates                         │ │  │
│  │  │ • Default prompts for common tasks                 │ │  │
│  │  │ • Custom prompt creation                           │ │  │
│  │  └────────────────────────────────────────────────────┘ │  │
│  │                                                            │  │
│  │  ┌────────────────────────────────────────────────────┐ │  │
│  │  │ Selection Service (selection.py)                   │ │  │
│  │  │ • Gets current selection from clipboard            │ │  │
│  │  │ • Text processing utilities                        │ │  │
│  │  └────────────────────────────────────────────────────┘ │  │
│  │                                                            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                ↓                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │           HOTKEYS LAYER (hotkeys/)                       │  │
│  │                                                            │  │
│  │  ┌────────────────────────────────────────────────────┐ │  │
│  │  │ Global Hotkeys (global_hotkeys.py)                 │ │  │
│  │  │ • Ctrl+Shift+J = Spell check                       │ │  │
│  │  │ • Ctrl+Shift+K = Prompt navigator                  │ │  │
│  │  │ • Ctrl+Alt+Shift+K = Go to hub                     │ │  │
│  │  │ • Ctrl+Alt+H = Toggle hotstrings                   │ │  │
│  │  │ • Works system-wide (even when app not focused)    │ │  │
│  │  └────────────────────────────────────────────────────┘ │  │
│  │                           ↓                              │  │
│  │              Uses: keyboard library                      │  │
│  │              (https://github.com/boppreh/keyboard)       │  │
│  │                                                            │  │
│  │  ┌────────────────────────────────────────────────────┐ │  │
│  │  │ Hotstrings Engine (hotstrings.py)                  │ │  │
│  │  │ • ;sig → "Best regards, Your Name"                 │ │  │
│  │  │ • ;date → Today's date                             │ │  │
│  │  │ • ;time → Current time                             │ │  │
│  │  │ • ;fix → AI fixes text                             │ │  │
│  │  │ • ;clar → AI clarifies text                        │ │  │
│  │  │ • ;short → AI shortens text                        │ │  │
│  │  │ • ;long → AI expands text                          │ │  │
│  │  │ • Auto-expansion anywhere on system                │ │  │
│  │  └────────────────────────────────────────────────────┘ │  │
│  │                                                            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                ↓                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │          CONFIGURATION LAYER (config.py)                │  │
│  │                                                            │  │
│  │  Reads from:                                             │  │
│  │  • OPENAI_API_KEY environment variable                  │  │
│  │  • settings.ini configuration file                      │  │
│  │                                                            │  │
│  │  Manages:                                                │  │
│  │  • OpenAI settings (key, endpoint, model, timeout)      │  │
│  │  • Hotkey settings (customizable shortcuts)             │  │
│  │  • Hotstring settings (auto-text expansion)             │  │
│  │                                                            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

### User Types in Chat Tab
```
User Input
    ↓
ChatTab (GUI)
    ↓
OpenAIClient.chat()
    ↓
Validate API Key
    ↓
Build Message Payload
    ↓
POST to OpenAI API
    ↓
Parse Response
    ↓
Display in Chat Tab
```

### User Triggers Hotkey (Ctrl+Shift+J)
```
System detects keyboard press
    ↓
GlobalHotkeys listener
    ↓
Execute callback
    ↓
Get selected text from clipboard
    ↓
Show spelling dialog
    ↓
Send to OpenAI for correction
    ↓
Display suggestions
```

### User Types Hotstring (;fix)
```
User types ";fix"
    ↓
HotstringEngine buffer catches text
    ↓
Match detected
    ↓
Get selected text from clipboard
    ↓
Send to OpenAI with "fix" prompt
    ↓
Erase ";fix" and replace with result
    ↓
Auto-replace on screen (system-wide!)
```

## Dependencies

```
PySide6 (GUI Framework)
  ├── Qt 6.x (underlying framework)
  ├── shiboken6 (Python-C++ bindings)
  └── PySide6_Addons (additional widgets)

requests (HTTP Library)
  └── For OpenAI API calls

keyboard (Hotkey Library)
  └── For system-wide hotkey detection

pywin32 (Windows API)
  └── Windows-specific functionality
```

## File Structure

```
AI Hub Root
├── run_ai_hub.bat                    ← Batch launcher
├── add_to_taskbar.bat                ← Taskbar setup
├── settings.ini                      ← Configuration
├── pyproject.toml                    ← Python package config
│
└── src/ai_hub/                       ← Main application
    ├── __init__.py
    ├── app.py                        ← Entry point
    ├── config.py                     ← Settings management
    │
    ├── ui/                           ← GUI components
    │   ├── main_window.py            ← Main window
    │   ├── base.py                   ← Base tab class
    │   ├── tabs/
    │   │   ├── chat_tab.py           ← Chat interface
    │   │   ├── prompts_tab.py        ← Prompts interface
    │   │   └── spelling_tab.py       ← Spelling interface
    │   └── dialogs/
    │       ├── prompt_navigator.py   ← Prompt selection dialog
    │       └── result_popup.py       ← Results popup
    │
    ├── services/                     ← Business logic
    │   ├── openai_client.py          ← OpenAI API wrapper
    │   ├── prompt_manager.py         ← Prompt templates
    │   └── selection.py              ← Text selection utilities
    │
    └── hotkeys/                      ← System integration
        ├── global_hotkeys.py         ← Keyboard shortcuts
        └── hotstrings.py             ← Auto-text expansion
```

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| GUI | PySide6 (Qt) | Desktop application interface |
| Language | Python 3.10+ | Application logic |
| API | OpenAI REST API | AI responses |
| Hotkeys | keyboard library | System-wide keyboard capture |
| HTTP | requests | API communication |
| Windows API | pywin32 | Windows-specific features |
| Theme | qdarktheme | Dark mode styling |

## Security Considerations

- **API Key**: Stored in settings.ini (local) or OPENAI_API_KEY env variable
- **No Network**: All communication encrypted via HTTPS to OpenAI
- **No Data Stored**: Responses not persisted (except in memory during session)
- **Local Execution**: All hotkey processing happens locally
- **No Telemetry**: No tracking or external communication except to OpenAI API

## Performance Notes

- **GUI**: PySide6 provides smooth, responsive interface
- **Hotkeys**: Minimal CPU usage, system-wide listener
- **API Calls**: Asynchronous to prevent UI freezing
- **Memory**: Lightweight, ~200-300MB typical usage
- **Startup**: ~2-3 seconds with all diagnostics

---

This is your complete AI Hub system! 🎉


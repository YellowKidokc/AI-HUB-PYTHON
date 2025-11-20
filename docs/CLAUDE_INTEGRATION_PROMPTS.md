# 🤖 Claude Integration Prompts for AI Hub Development

> These prompts are designed to be copied directly to Claude or GitHub Copilot to extend the AI Hub system. They include full context about the codebase architecture and integration patterns.

---

## 🏗️ MASTER SYSTEM ARCHITECTURE PROMPT

```
You are helping extend the AI Hub desktop application built in Python with PySide6.

## Current Architecture

### Project Structure
```
D:\AI-HUB 2 Claude\
├── run_ai_hub.bat                 # Main launcher
├── settings.ini                    # Configuration
├── config/                         # Runtime config
│   ├── hotkeys.ini                # Hotkey definitions
│   ├── hotstrings.sav             # Hotstring definitions
│   ├── prompts.json               # Saved prompts
│   └── snippets.json              # Code snippets
├── src/ai_hub/
│   ├── app.py                     # Entry point
│   ├── config.py                  # Settings loader
│   ├── ui/
│   │   ├── main_window.py         # Main GUI window
│   │   ├── tabs/
│   │   │   ├── base.py            # Base tab class
│   │   │   ├── chat_tab.py        # Chat with AI
│   │   │   ├── prompts_tab.py     # Prompt management
│   │   │   └── spelling_tab.py    # Text rewriting
│   │   ├── popups/
│   │   │   ├── floating_popup.py  # Result display
│   │   │   ├── prompt_selector_popup.py  # Prompt picker
│   │   │   └── snippets_manager.py       # Snippet storage
│   │   └── improved_manager_window.py    # Hotkey manager
│   ├── services/
│   │   ├── openai_client.py       # OpenAI API wrapper
│   │   ├── multi_api_client.py    # Multi-provider support
│   │   ├── prompt_manager.py      # Prompt templates
│   │   ├── action_manager.py      # Quick actions
│   │   ├── smart_action_handler.py # Smart workflows
│   │   └── text_selector.py       # Text selection utilities
│   └── hotkeys/
│       ├── global_hotkeys.py      # System-wide hotkey detection
│       ├── smart_hotkeys.py       # Alt+Spacebar workflows
│       ├── action_hotkeys.py      # Custom action hotkeys
│       ├── prompt_selector_hotkey.py  # Ctrl+Alt+T
│       └── hotstrings.py          # Text auto-expansion
```

### Key Classes & Patterns

**Tab Pattern (for new features):**
```python
from ..tabs.base import BaseTab
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton

class MyNewTab(BaseTab):
    def __init__(self, client=None):
        super().__init__()
        self._client = client
        self._build_ui()
    
    def _build_ui(self):
        layout = QVBoxLayout(self)
        # Add widgets here
        layout.addWidget(QLabel("My Feature"))
    
    def keyPressEvent(self, event):
        # Handle hotkeys like Ctrl+Alt+X
        if event.key() == Qt.Key.Key_X and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self._on_hotkey()
    
    def _on_hotkey(self):
        # Implement feature logic
        pass
```

**Service Pattern (for business logic):**
```python
class MyNewService:
    def __init__(self, config=None):
        self._config = config
    
    def do_something(self, input_data):
        # Implement feature
        return result
```

**Hotkey Pattern:**
```python
import keyboard

class MyHotkey:
    def __init__(self, on_trigger=None):
        self._on_trigger = on_trigger
    
    def start(self):
        keyboard.add_hotkey("ctrl+alt+x", self._on_hotkey)
    
    def stop(self):
        keyboard.remove_hotkey("ctrl+alt+x")
    
    def _on_hotkey(self):
        if self._on_trigger:
            self._on_trigger()
```

### Dark Theme Styling

All UI elements use this stylesheet:
```python
stylesheet = """
    QWidget {
        background-color: #1e1e1e;
        color: #e0e0e0;
    }
    QLineEdit, QTextEdit, QComboBox {
        background-color: #252525;
        border: 1px solid #3d3d3d;
        color: #e0e0e0;
    }
    QPushButton {
        background-color: #007acc;
        color: white;
    }
    QPushButton:hover {
        background-color: #005a9e;
    }
"""
```

### Data Storage

- **Config files:** JSON in `config/` directory
- **Auto-save:** Use `_save_config()` pattern
- **Auto-load:** Use `_load_config()` in `__init__`
- **Persistence:** Everything saved across sessions

### Threading for Long Operations

```python
import threading

def _on_action(self):
    def run():
        # Long operation
        result = self._api_call()
        # Update UI (use signals or direct update if simple)
        self._update_ui(result)
    
    threading.Thread(target=run, daemon=True).start()
```

## Integration Rules

1. **Don't modify existing tabs** - Create new tabs instead
2. **Don't break hotkey system** - Register new hotkeys separately
3. **Use config directory** - Store data in `config/*.json`
4. **Follow naming patterns** - Use `_on_`, `_build_`, `_load_`, `_save_`
5. **Dark theme only** - Apply stylesheet to all widgets
6. **Thread long operations** - Never block the UI
7. **Add to main_window.py** - Register new tabs in `__init__`

## What You're Adding

[SPECIFY FEATURE HERE]

Please analyze the existing codebase structure and provide:
1. Where the new feature should be added
2. What new files to create
3. How to integrate without breaking existing code
4. Code templates following the patterns above
```

---

## 📋 FEATURE PROMPTS (Copy & Use)

### Feature 1: Clipboard History Manager

```
Based on the AI Hub architecture (see MASTER_SYSTEM_ARCHITECTURE_PROMPT), 
I need to add a Clipboard History Manager as a side panel showing 1000-2000 
clipboard items with 1-2 week storage.

Requirements:
1. Side panel (not a tab) showing clipboard history
2. 1000-2000 items with timestamps
3. 1-2 week storage (configurable retention)
4. Click item to restore to clipboard
5. Search/filter capability
6. Persistent storage in config/clipboard_history.json

Implementation needed:
1. src/ai_hub/services/clipboard_manager.py - Handle history storage
2. src/ai_hub/ui/clipboard_panel.py - UI widget for side panel
3. Integration in src/ai_hub/ui/main_window.py

Follow the patterns:
- Use threading for clipboard monitoring
- JSON storage in config/
- Dark theme styling (see architecture)
- Auto-save every item
- Prune old items (>2 weeks)

Please provide:
1. Complete clipboard_manager.py with persistence
2. Complete clipboard_panel.py with UI
3. Code snippets for integration in main_window.py
4. Storage schema for clipboard_history.json
```

### Feature 2: Web Scraper (Ctrl+Alt+8 & Ctrl+Alt+S)

```
Based on the AI Hub architecture, I need a Web Scraper feature with hotkeys:
- Ctrl+Alt+8: Download to Downloads folder
- Ctrl+Alt+S: Choose folder for download

Requirements:
1. Hotkey handler for both keys
2. Web scraping capability (BeautifulSoup or Selenium)
3. Auto-detect download targets (links, PDFs, images)
4. Save progress to config/scraper_jobs.json
5. Notification when complete

Implementation needed:
1. src/ai_hub/services/web_scraper.py - Scraping logic
2. src/ai_hub/hotkeys/web_scraper_hotkey.py - Hotkey handler
3. Integration in src/ai_hub/hotkeys/global_hotkeys.py

Please provide:
1. Complete web_scraper.py with threading
2. Complete web_scraper_hotkey.py
3. Integration code for global_hotkeys.py
4. Error handling for failed downloads
```

### Feature 3: Specialized Search GUI (50-100 Presets)

```
Based on the AI Hub architecture, create a Specialized Search GUI as a 
new tab showing 50-100 pre-configured search templates.

Requirements:
1. New tab: SpecializedSearchTab
2. List of 50-100 search templates:
   - Google Docs: site:docs.google.com
   - GitHub: site:github.com
   - PDFs: filetype:pdf
   - Datasets: kaggle.com, etc.
3. Click template → opens browser with search applied
4. Search bar to filter templates
5. Ability to add custom searches
6. Store custom searches in config/search_templates.json

Implementation needed:
1. src/ai_hub/ui/tabs/specialized_search_tab.py
2. src/ai_hub/services/search_templates.py - Template management
3. Integration in src/ai_hub/ui/main_window.py

Please provide:
1. Complete SpecializedSearchTab with all UI
2. search_templates.py with built-in templates
3. Integration code
4. List of 50 search template examples
```

### Feature 4: Web Crawler

```
Based on the AI Hub architecture, create a Web Crawler service that 
recursively crawls websites and extracts data.

Requirements:
1. Start URL input
2. Max depth setting
3. Extract: links, images, text, PDFs
4. Store results in config/crawl_results.json
5. Progress display
6. Stop/pause controls

Implementation needed:
1. src/ai_hub/services/web_crawler.py - Crawling logic
2. src/ai_hub/ui/tabs/web_crawler_tab.py - UI for crawler
3. Integration in main_window.py

Please provide:
1. Complete web_crawler.py with threading
2. Complete web_crawler_tab.py with progress UI
3. Threading implementation for non-blocking crawling
4. Storage schema for results
```

---

## 🔧 INTEGRATION CHECKLIST

When adding a new feature, follow this checklist:

- [ ] Create service class in `src/ai_hub/services/`
- [ ] Create UI component (tab or dialog)
- [ ] Add hotkey handler if applicable
- [ ] Create config storage file
- [ ] Add _load_config() and _save_config() methods
- [ ] Apply dark theme stylesheet
- [ ] Use threading for long operations
- [ ] Add to main_window.py initialization
- [ ] Test with run_ai_hub.bat
- [ ] Verify no existing features are broken

---

## 📝 USAGE INSTRUCTIONS

1. **Copy the MASTER_SYSTEM_ARCHITECTURE_PROMPT** to Claude first
2. **Then copy the specific FEATURE PROMPT** for what you want
3. **Claude will generate all needed files**
4. **Review the generated code**
5. **Create files and integrate**
6. **Test with run_ai_hub.bat**

---

## ✅ TESTED PATTERNS

These patterns have been tested and work:

✅ Tab creation and integration
✅ Hotkey detection and handling  
✅ Config file storage (JSON)
✅ Threading for long operations
✅ Dark theme styling
✅ Popup windows and dialogs
✅ Multi-provider API support
✅ Persistent data across sessions

---

## 🚀 GENERATE YOUR FEATURE

To use this system:

1. **For new tab/feature:** Use Feature Prompt 1-4 above
2. **For completely custom:** Use MASTER_SYSTEM_ARCHITECTURE_PROMPT and describe what you want
3. **Claude will generate:** Complete, working, integrated code
4. **You implement:** Copy files and run bat launcher

All features will integrate seamlessly without breaking existing code!
```

---

## Next Steps

Would you like me to:
1. **Create the Clipboard History Manager first?** (I can do this now)
2. **Generate all the prompts above** so you can give them to Claude?
3. **Both?** (I build clipboard now, you get all prompts for other features)

Which appeals to you most? 🚀

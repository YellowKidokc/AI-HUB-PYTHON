# 🎨 Feature Implementation Template for Claude

When asking Claude to build a feature, it should follow this EXACT template structure. This ensures:
- ✅ Consistent code patterns
- ✅ No breaking changes
- ✅ Easy integration
- ✅ Professional quality

---

## 📦 REQUIRED FILE STRUCTURE

Every feature should consist of:

### 1. Service Class (Business Logic)
**File:** `src/ai_hub/services/my_feature_service.py`

```python
"""
my_feature_service.py - [Feature Description]

Handles all business logic for [feature].
Persists data to config/my_feature_config.json
"""

import json
import os
from pathlib import Path
from dataclasses import dataclass, asdict

@dataclass
class MyFeatureConfig:
    """Configuration for my feature"""
    enabled: bool = True
    setting1: str = "default"
    setting2: int = 100
    # Add settings here

class MyFeatureService:
    """Service for [feature description]"""
    
    def __init__(self, config_dir: str = "config"):
        self._config_dir = Path(config_dir)
        self._config_dir.mkdir(exist_ok=True)
        self._config_file = self._config_dir / "my_feature_config.json"
        self._config = self._load_config()
    
    def _load_config(self) -> MyFeatureConfig:
        """Load config from disk or create default"""
        if self._config_file.exists():
            try:
                with open(self._config_file, 'r') as f:
                    data = json.load(f)
                    return MyFeatureConfig(**data)
            except Exception as e:
                print(f"Error loading config: {e}")
        return MyFeatureConfig()
    
    def _save_config(self) -> None:
        """Save config to disk"""
        try:
            with open(self._config_file, 'w') as f:
                json.dump(asdict(self._config), f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def do_something(self, input_data: str) -> str:
        """Main feature logic"""
        # Implement your feature logic here
        result = f"Processed: {input_data}"
        return result
```

### 2. UI Tab Component (if it's a tab feature)
**File:** `src/ai_hub/ui/tabs/my_feature_tab.py`

```python
"""
my_feature_tab.py - [Feature UI]

Visual interface for [feature].
"""

from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QTextEdit, QListWidget, QListWidgetItem
)
from PySide6.QtCore import Qt
from ..tabs.base import BaseTab
from ...services.my_feature_service import MyFeatureService


class MyFeatureTab(BaseTab):
    """Tab for [feature name]"""
    
    def __init__(self, client=None):
        super().__init__()
        self._client = client
        self._service = MyFeatureService()
        self._build_ui()
    
    def _build_ui(self) -> None:
        """Build the UI"""
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("My Feature")
        title.setStyleSheet("color: #e0e0e0; font-size: 14px; font-weight: bold;")
        layout.addWidget(title)
        
        # Input area
        input_label = QLabel("Input:")
        input_label.setStyleSheet("color: #e0e0e0;")
        layout.addWidget(input_label)
        
        self._input_field = QLineEdit()
        self._input_field.setPlaceholderText("Enter input here...")
        self._input_field.setStyleSheet(
            "background-color: #252525; color: #e0e0e0; "
            "border: 1px solid #3d3d3d; padding: 5px; border-radius: 3px;"
        )
        layout.addWidget(self._input_field)
        
        # Button
        btn = QPushButton("Process")
        btn.setStyleSheet(
            "background-color: #007acc; color: white; border: none; "
            "padding: 6px 16px; border-radius: 3px; font-weight: bold;"
        )
        btn.clicked.connect(self._on_process)
        layout.addWidget(btn)
        
        # Output area
        output_label = QLabel("Output:")
        output_label.setStyleSheet("color: #e0e0e0;")
        layout.addWidget(output_label)
        
        self._output = QTextEdit()
        self._output.setReadOnly(True)
        self._output.setStyleSheet(
            "background-color: #252525; color: #e0e0e0; "
            "border: 1px solid #3d3d3d; padding: 5px; border-radius: 3px;"
        )
        layout.addWidget(self._output)
        
        layout.addStretch()
    
    def _on_process(self) -> None:
        """Handle process button click"""
        input_text = self._input_field.text()
        if not input_text.strip():
            self._output.setText("Please enter input.")
            return
        
        result = self._service.do_something(input_text)
        self._output.setText(result)
    
    def keyPressEvent(self, event) -> None:
        """Handle hotkeys"""
        if (event.key() == Qt.Key.Key_Space and 
            event.modifiers() & Qt.KeyboardModifier.ControlModifier and
            event.modifiers() & Qt.KeyboardModifier.AltModifier):
            self._on_process()
            event.accept()
        else:
            super().keyPressEvent(event)
```

### 3. Hotkey Handler (if applicable)
**File:** `src/ai_hub/hotkeys/my_feature_hotkey.py`

```python
"""
my_feature_hotkey.py - Hotkey handler for [feature]

Registers Ctrl+Alt+X hotkey globally.
"""

import keyboard
import threading


class MyFeatureHotkey:
    """Handles Ctrl+Alt+X hotkey for [feature]"""
    
    def __init__(self, on_trigger=None):
        self._on_trigger = on_trigger
        self._registered = False
    
    def start(self) -> None:
        """Register hotkey"""
        try:
            keyboard.add_hotkey("ctrl+alt+x", self._on_hotkey)
            self._registered = True
            print("✅ MyFeature hotkey registered (Ctrl+Alt+X)")
        except Exception as e:
            print(f"❌ Failed to register hotkey: {e}")
    
    def stop(self) -> None:
        """Unregister hotkey"""
        try:
            if self._registered:
                keyboard.remove_hotkey("ctrl+alt+x")
                self._registered = False
        except Exception:
            pass
    
    def _on_hotkey(self) -> None:
        """Called when hotkey is pressed"""
        if self._on_trigger:
            # Run on separate thread to not block input
            threading.Thread(target=self._on_trigger, daemon=True).start()
```

### 4. Integration in Main Window
**File:** `src/ai_hub/ui/main_window.py`

```python
# Add to imports:
from .tabs.my_feature_tab import MyFeatureTab
from ..hotkeys.my_feature_hotkey import MyFeatureHotkey

# In MainWindow.__init__(), add tab:
self._my_feature_tab = MyFeatureTab(self._client)
self._tabs.addTab(self._my_feature_tab, "My Feature")

# Register hotkey:
self._my_feature_hotkey = MyFeatureHotkey(on_trigger=self._on_my_feature_trigger)
self._my_feature_hotkey.start()

# Add to MainWindow class:
def _on_my_feature_trigger(self) -> None:
    """Trigger my feature from hotkey"""
    # Bring tab to foreground
    index = self._tabs.indexOf(self._my_feature_tab)
    self._tabs.setCurrentIndex(index)
    # Or trigger action directly
    self._my_feature_tab._on_process()

# In MainWindow.closeEvent(), clean up:
self._my_feature_hotkey.stop()
```

---

## ✅ QUALITY CHECKLIST

Claude should ensure:

- [ ] **Imports are correct** - All modules exist in project
- [ ] **Follows naming conventions** - `_private_method()`, `MyClass`
- [ ] **Has docstrings** - Every class and method documented
- [ ] **Dark theme applied** - All UI elements styled
- [ ] **Threading used** - No blocking operations
- [ ] **Config persistence** - Data saved/loaded correctly
- [ ] **Error handling** - Try/except where needed
- [ ] **No external deps** - Only uses installed packages
- [ ] **Type hints** - Function parameters and returns
- [ ] **Comments** - Complex logic explained

---

## 🎨 DARK THEME STANDARD

All UI elements must use these colors:

```python
# Background
background: "#1e1e1e"
widget_bg: "#252525"
border: "#3d3d3d"

# Text
text_color: "#e0e0e0"
label_color: "#a0a0a0"

# Buttons
button_bg: "#007acc"
button_hover: "#005a9e"
button_press: "#004578"

# Standard Stylesheet for QLineEdit, QTextEdit, QComboBox:
stylesheet = """
    background-color: #252525;
    color: #e0e0e0;
    border: 1px solid #3d3d3d;
    padding: 5px;
    border-radius: 3px;
"""

# Button Stylesheet:
button_stylesheet = """
    background-color: #007acc;
    color: white;
    border: none;
    padding: 6px 16px;
    border-radius: 3px;
    font-weight: bold;
"""
```

---

## 📚 PYTHON PACKAGE DEPENDENCIES

All features must use ONLY these pre-installed packages:

```
PySide6>=6.6,<7.0      # GUI
requests>=2.31         # HTTP requests
keyboard>=0.13         # Hotkeys
pynput>=1.8           # Input handling
pyperclip>=1.8        # Clipboard
pywin32>=306          # Windows integration (optional)
```

If a feature needs a new dependency:
1. Add to `pyproject.toml`
2. Document why it's needed
3. Test with `pip install -e .`

---

## 🚀 FILE GENERATION INSTRUCTIONS FOR CLAUDE

When Claude generates code, it should output:

```markdown
# Implementation for [Feature Name]

## Files to Create:

### 1. src/ai_hub/services/my_feature_service.py
[FULL FILE CONTENT]

### 2. src/ai_hub/ui/tabs/my_feature_tab.py
[FULL FILE CONTENT]

### 3. src/ai_hub/hotkeys/my_feature_hotkey.py
[FULL FILE CONTENT]

## Integration Code for main_window.py:

[EXACT LINES TO ADD]

## How to Install:

1. Create the three files above
2. Add integration code to main_window.py
3. Run: python -m ai_hub.app
4. Test the new feature

## Config File:
Location: config/my_feature_config.json
Schema: [JSON SCHEMA]
```

---

## 🔄 ITERATIVE IMPROVEMENT

If Claude's code doesn't work:

1. Copy error message
2. Ask Claude to fix it
3. Reference the **exact error and line number**
4. Claude will fix and re-generate

Don't rewrite - let Claude iterate!

---

## 📋 EXAMPLE: Clipboard Manager

For the Clipboard Manager feature, Claude should generate:

1. `src/ai_hub/services/clipboard_manager.py` - 200+ lines
2. `src/ai_hub/ui/clipboard_panel.py` - 150+ lines
3. Integration code for `main_window.py` - 10-15 lines
4. `config/clipboard_history.json` - (created at runtime)

Total time for Claude: ~5 minutes
Total time for you: ~15 minutes to copy files and integrate

---

## 🎯 USAGE EXAMPLE

You to Claude:

```
Use this template to build a [Feature Name] feature for my Python PySide6 desktop app.

Requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

Generate the files following the CLAUDE_FEATURE_TEMPLATE.md structure.
```

Claude will generate complete, working code!

---

**This template ensures consistency, quality, and maintainability across all features.** ✨


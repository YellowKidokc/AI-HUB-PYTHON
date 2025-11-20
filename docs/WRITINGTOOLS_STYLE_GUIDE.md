# 🎯 Converting AI Hub to WritingTools Style

## Current Issue

Your AI Hub is working, but it's missing the **WritingTools pattern** of:
- ✅ System-wide hotkey trigger
- ❌ Floating popup results (instead of multi-tab window)
- ❌ Quick action buttons (Proofread, Rewrite, etc.)
- ❌ Instant text processing from any app

## What We Need to Change

### Current Architecture (Multi-Tab GUI)
```
┌─────────────────────────────┐
│ AI Hub Window               │
├─────────────────────────────┤
│ [Chat] [Prompts] [Spelling] │
├─────────────────────────────┤
│ Main content area           │
└─────────────────────────────┘
```

### WritingTools Style (Floating Popup)
```
User presses Ctrl+Shift+J anywhere
        ↓
AI Hub detects hotkey
        ↓
Gets selected text from clipboard
        ↓
Sends to OpenAI
        ↓
┌─────────────────────────────┐
│ AI Hub - Proofreading...     │
├─────────────────────────────┤
│ Original: "your text here"   │
│                              │
│ Fixed: "Your text here."     │
│                              │
│ [Copy] [Apply] [Dismiss]     │
└─────────────────────────────┘
```

## Required Changes

### 1. **Create Floating Window System**
Instead of static tabs, create popup windows that:
- Appear near cursor position
- Show one action at a time
- Have Copy/Apply/Dismiss buttons
- Close after action or on Escape

### 2. **Add Quick Action Buttons**
Create buttons for:
- Proofread (grammar/spelling)
- Rewrite (improve phrasing)
- Make Friendly (casual tone)
- Make Professional (formal tone)
- Summarize (condense text)
- Custom Instructions (user-defined)

### 3. **Improve System Integration**
- Detect selected text automatically
- Work with any application
- Paste results back with [Apply] button
- Support custom keyboard shortcuts per button

### 4. **Simplify Settings**
Current: Complex tab-based GUI
WritingTools: Simple settings panel with:
- API key setup
- Hotkey configuration
- Button customization
- Provider selection (OpenAI, Ollama, etc.)

## Implementation Plan

### Phase 1: Fix Current Issues
✅ Remove qdarktheme dependency
✅ Implement native dark theme
⏳ Fix hotkey popup triggering

### Phase 2: Add Floating Windows
- Create PopupWindow class
- Implement near-cursor positioning
- Add Copy/Apply/Dismiss buttons
- Create action result display

### Phase 3: Add Quick Actions
- Create action definitions
- Add button to window
- Connect buttons to prompts
- Show results in popup

### Phase 4: WritingTools Parity
- Settings simplified
- All features accessible via hotkeys
- Custom button creation
- Multi-provider support

## File Structure (Proposed)

```
src/ai_hub/
├── ui/
│   ├── main_window.py        ← Keep for settings
│   ├── popups/
│   │   ├── floating_popup.py ← NEW: Floating window
│   │   ├── action_popup.py   ← NEW: Action results
│   │   └── settings_window.py ← NEW: Settings dialog
│   └── tabs/                 ← Can keep or refactor
├── services/
│   ├── action_manager.py     ← NEW: Manage quick actions
│   └── text_processor.py     ← NEW: Process text with AI
└── hotkeys/
    └── action_hotkeys.py     ← NEW: Trigger specific actions
```

## Quick Integration Steps

1. **Install required for WritingTools-like features:**
   ```bash
   pip install pyperclip python-dotenv
   ```

2. **Create action system:**
   - Define built-in actions (Proofread, Rewrite, etc.)
   - Map hotkeys to actions
   - Create popup window manager

3. **Update hotkey handler:**
   - Instead of opening tab, open floating popup
   - Show action result in popup
   - Add Copy/Apply buttons

4. **Simplify main window:**
   - Keep for settings only
   - Remove multi-tab layout
   - Focus on configuration

## Example: Proofread Action Flow

```python
# User presses Ctrl+Shift+J
hotkey_handler()
    ↓
# Get selected text
text = clipboard.get()
    ↓
# Send to AI with "proofread" prompt
result = openai.proofread(text)
    ↓
# Show in floating popup
show_popup(
    title="Proofread",
    original=text,
    result=result,
    buttons=["Copy", "Apply", "Dismiss"]
)
    ↓
# If user clicks Apply:
clipboard.set(result)
# Paste back to original app
paste_text()
```

## Benefits of WritingTools Style

✨ Faster workflow (no window switching)
✨ Works in any application
✨ Less intrusive (temporary popups)
✨ One-click fixes
✨ More intuitive for users
✨ Easier to extend with custom actions

## Next Steps

Would you like me to:

1. **Refactor to WritingTools style** - Convert the current tabs to floating popups
2. **Add floating popup system** - Create the popup infrastructure
3. **Add quick action buttons** - Implement Proofread, Rewrite, etc.
4. **Keep current + add floating** - Have both window and popups available

Which would you prefer? I recommend **Option 1: Full Refactor** to match WritingTools pattern.


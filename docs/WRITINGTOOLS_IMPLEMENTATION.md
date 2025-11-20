# 🚀 WritingTools Implementation Guide

## Status: 🔧 In Progress

I've started converting your AI Hub to follow the [WritingTools](https://github.com/theJayTea/WritingTools) pattern. Here's what I've created and what's next.

## ✅ Completed

### 1. Fixed qdarktheme Error
- ❌ Removed: `qdarktheme` import (package not available)
- ✅ Added: Native PySide6 dark stylesheet
- ✅ Result: App now launches without errors!

### 2. Created Floating Popup System
- **File**: `src/ai_hub/ui/popups/floating_popup.py`
- **Features**:
  - Floating window that stays on top
  - Shows original + result text
  - Copy/Apply/Dismiss buttons
  - Positions near cursor
  - Dark theme styling
  - Frameless design (modern look)

### 3. Created Action Manager
- **File**: `src/ai_hub/services/action_manager.py`
- **Features**:
  - 7 built-in actions (Proofread, Rewrite, Friendly, etc.)
  - Each action has prompt + hotkey
  - Execute actions synchronously
  - Support for custom actions

## ⏳ Next Steps (for you)

### Option A: I Build It (Recommended - 30 min)
Let me fully refactor to WritingTools style:
- [ ] Integrate floating popup into hotkey system
- [ ] Convert hotkeys to trigger specific actions
- [ ] Update main window for settings only
- [ ] Test all actions work
- [ ] Create simplified settings UI

### Option B: You Test Current Features
Try the current app to see what works:
```bash
# Double-click: run_ai_hub.bat
# Or: python -m ai_hub.app
```

Test:
- [ ] GUI opens with dark theme ✓
- [ ] Chat tab works (if API key set)
- [ ] Spelling tab works (if API key set)
- [ ] Hotkeys trigger popups
- [ ] Text selection works

## 🎯 WritingTools Style Features (To Implement)

### Quick Actions (Available Immediately)
```
Ctrl+Shift+J = Proofread text
Ctrl+Shift+R = Rewrite text
Ctrl+Shift+F = Make Friendly
Ctrl+Shift+P = Make Professional
Ctrl+Shift+S = Summarize
```

### How They Work
1. User selects text in any application
2. User presses hotkey (e.g., Ctrl+Shift+J)
3. AI Hub detects hotkey → gets selected text from clipboard
4. Sends to OpenAI with action prompt (e.g., "Proofread this text")
5. Shows result in **floating popup**:
   ```
   ┌─────────────────────────────┐
   │ AI Hub - Proofread          │
   ├─────────────────────────────┤
   │ Your proofread text here    │
   │                             │
   │ Original:                   │
   │ "your orginal text"         │
   │                             │
   │ [Copy] [Apply] [Dismiss]    │
   └─────────────────────────────┘
   ```
6. User can:
   - **Copy**: Copy result to clipboard
   - **Apply**: Copy result AND close popup (then Ctrl+V to paste back)
   - **Dismiss**: Close and discard

## 📁 Files Created

```
src/ai_hub/
├── ui/
│   └── popups/
│       ├── __init__.py                ✅ NEW
│       └── floating_popup.py          ✅ NEW (FloatingPopup class)
├── services/
│   └── action_manager.py              ✅ NEW (ActionManager class)
└── (main files updated)
    ├── main_window.py                 ✅ UPDATED (native dark theme)
    ├── ui/main_window.py              ✅ UPDATED (removed qdarktheme)
```

## 🔄 Architecture Changes

### Before (Current)
```
Hotkey → Open Main Window → Choose Tab → Process Text → Show Result in Tab
```

### After (WritingTools)
```
Hotkey → Get Selected Text → AI Process → Show Floating Popup → User Action
```

## 🛠️ Integration Checklist

To complete the WritingTools conversion:

- [ ] **Update Hotkey Handler**
  - File: `src/ai_hub/hotkeys/global_hotkeys.py`
  - Change: Instead of opening window, trigger action
  - Show: Floating popup with result

- [ ] **Create Custom Hotkey Handler**
  - File: `src/ai_hub/hotkeys/action_hotkeys.py` (NEW)
  - Purpose: Handle action-specific hotkeys
  - Integrate: With ActionManager

- [ ] **Update Main Window**
  - File: `src/ai_hub/ui/main_window.py`
  - Remove: Chat, Prompts, Spelling tabs
  - Keep: Settings panel
  - Add: Action buttons/list

- [ ] **Create Settings UI**
  - File: `src/ai_hub/ui/settings_window.py` (NEW)
  - Features:
    - API key input
    - Hotkey configuration
    - Action enable/disable
    - Provider selection

- [ ] **Test Everything**
  - Launch app
  - Try each hotkey
  - Verify popups show
  - Test Copy/Apply/Dismiss
  - Test with different apps

## 🎨 UI Mockup (After Refactor)

### Main Window (Settings)
```
┌──────────────────────────────────────────┐
│ AI Hub Settings                       [×] │
├──────────────────────────────────────────┤
│                                          │
│ 🔑 API KEY                               │
│ [sk-..............................]      │
│                                          │
│ 🎨 QUICK ACTIONS                         │
│ ☑ Proofread (Ctrl+Shift+J)               │
│ ☑ Rewrite (Ctrl+Shift+R)                 │
│ ☑ Make Friendly (Ctrl+Shift+F)           │
│ ☑ Make Professional (Ctrl+Shift+P)       │
│ ☑ Summarize (Ctrl+Shift+S)               │
│                                          │
│ [Add Custom Action +]                    │
│                                          │
│                               [Save]     │
└──────────────────────────────────────────┘
```

### Floating Popup (After Hotkey)
```
┌─────────────────────────────────┐
│ AI Hub - Proofread          [×] │
├─────────────────────────────────┤
│ Your fixed text goes here.      │
│ It will be formatted nicely.    │
│                                 │
│ Original:                       │
│ "your orginal text goes here"   │
│                                 │
│ [Copy] [Apply] [Dismiss]        │
└─────────────────────────────────┘
```

## 💡 Key Advantages

✨ **Faster workflow** - Hotkey → Result → Done
✨ **Works everywhere** - Any app, any text field
✨ **Less intrusive** - Temporary popups, not persistent window
✨ **More intuitive** - Like WritingTools users expect
✨ **Customizable** - Add own actions/hotkeys
✨ **Minimal UI** - Settings hidden until needed

## 🚀 To Continue

### Option 1: Let Me Build It
Reply: "Build it" and I'll complete the full refactor

### Option 2: Do It Yourself  
Follow this guide step by step:
1. Update `hotkeys/global_hotkeys.py` to use ActionManager
2. Create `hotkeys/action_hotkeys.py` for action-specific keys
3. Update `main_window.py` to show settings
4. Create `ui/settings_window.py` for configuration
5. Test with different hotkeys

### Option 3: Keep Both
- Keep current multi-tab window
- Add floating popups on top
- Users can choose which interface they prefer

## 📊 Comparison: Current vs WritingTools

| Feature | Current | WritingTools |
|---------|---------|--------------|
| Interface | Multi-tab window | Floating popups |
| Hotkey | Opens window | Triggers action |
| Result display | Tab view | Popup near cursor |
| Workflow | Manual + click | Hotkey → Done |
| Text processing | Paste + process | Auto-detect selection |
| Customization | Limited | Highly customizable |
| Integration | Moderate | Seamless |

## 🎯 Recommendation

I recommend **Option 1: Full Build** because:
1. Matches WritingTools pattern (your goal)
2. Better user experience
3. Faster execution
4. Easier to extend
5. More professional feel

Should I go ahead and complete it?

---

**Status**: Ready to implement full WritingTools-style refactor
**Time Estimate**: 30-45 minutes
**Difficulty**: Medium (mostly UI/hotkey updates)

Let me know how you want to proceed! 🚀


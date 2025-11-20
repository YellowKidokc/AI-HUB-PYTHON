# 🎮 Window Manager Guide

## 🎉 Complete Window Control System

Your AI Hub now has **advanced window management** with:

1. **🎮 Ctrl+Alt+G** - Show/hide main window from anywhere
2. **📍 System Tray Icon** - Click to show AI Hub
3. **🎮 Window Manager Panel** - Control all window settings
4. **💾 Position Memory** - Windows remember their location
5. **📏 Size Memory** - Windows remember their size
6. **📌 Always-On-Top** - Keep windows visible or let them hide

---

## ⚡ Quick Access Methods

### 1. **Ctrl+Alt+G Hotkey**
- **Press once**: Show AI Hub
- **Press again**: Hide AI Hub
- **Works globally**: From any app

### 2. **System Tray Icon**
- **Left-click**: Show AI Hub
- **Right-click**: Open menu
  - 🏠 Show AI Hub
  - 🎮 Window Manager
  - ❌ Quit

### 3. **Floating Player Button**
- **🎮 Button**: Opens Window Manager directly
- Located at bottom of floating player

---

## 🎮 Window Manager Panel

### How to Open:
1. **From Tray**: Right-click tray icon → "Window Manager"
2. **From Player**: Click 🎮 button on floating player
3. **From Hotkey**: Ctrl+Alt+G → Right-click tray → "Window Manager"

### Features:

#### **Always On Top Section**
- ☑️ **All Windows On Top** - Makes ALL AI Hub windows stay on top
- ☑️ **Main Window On Top** - Only main window stays on top
- ☑️ **Floating Player On Top** - Only player stays on top

#### **Position & Size Section**
- 💾 **Save Current Position** - Remember where windows are now
- 📏 **Save Current Size** - Remember window sizes
- 💾 **Save Position & Size** - Save everything at once

---

## 💡 Use Cases

### Use Case 1: **Always Accessible**
```
Problem: Need AI Hub available instantly
Solution:
1. Enable "All Windows On Top"
2. Resize main window to corner
3. Click "Save Position & Size"
4. AI Hub always visible, never hidden
```

### Use Case 2: **Normal Workflow**
```
Problem: Don't want windows blocking other apps
Solution:
1. Disable "All Windows On Top"
2. Use Ctrl+Alt+G to show/hide
3. Or click system tray icon
4. Windows appear when needed, hide when not
```

### Use Case 3: **Floating Player Only**
```
Problem: Want player visible, but not main window
Solution:
1. Enable "Floating Player On Top"
2. Disable "Main Window On Top"
3. Player stays visible for quick controls
4. Main window hides behind other apps
```

### Use Case 4: **Custom Layout**
```
Problem: Want specific window arrangement
Solution:
1. Resize main window to preferred size
2. Move floating player to preferred corner
3. Click "Save Position & Size"
4. Windows always open in same spots
```

---

## 🔧 How It Works

### Position Memory:
- **Saves to**: `config/window_settings.json`
- **Remembers**: X, Y coordinates for each window
- **Auto-loads**: On startup
- **Auto-saves**: On close

### Size Memory:
- **Saves to**: `config/window_settings.json`
- **Remembers**: Width, height for main window
- **Auto-loads**: On startup
- **Auto-saves**: On close

### Always-On-Top:
- **Global Mode**: All windows stay on top
- **Individual Mode**: Choose which windows
- **Persists**: Across restarts
- **Toggle anytime**: Via Window Manager panel

---

## 📊 Window Settings File

Location: `config/window_settings.json`

```json
{
  "main_window": {
    "x": 100,
    "y": 100,
    "width": 1000,
    "height": 720,
    "always_on_top": false
  },
  "floating_player": {
    "x": 1700,
    "y": 900,
    "width": 200,
    "height": 140,
    "always_on_top": true
  },
  "global_always_on_top": false
}
```

**You can edit this file manually if needed!**

---

## 🎯 Keyboard Shortcuts Summary

| Hotkey | Action |
|--------|--------|
| **Ctrl+Alt+G** | Show/Hide main window |
| **Ctrl+CapsLock+A** | Speak selected text (TTS) |
| **Ctrl+Space** | Fix grammar with AI |
| **Ctrl+Shift+K** | Open prompt navigator |
| **Ctrl+Alt+Shift+K** | Focus AI Hub window |
| **Ctrl+Alt+H** | Toggle hotstrings |

---

## 🎨 Window Behavior Examples

### Example 1: **Jarvis Mode** (Always Visible)
```
Settings:
- ✅ All Windows On Top
- Main window: Small, top-right corner
- Floating player: Bottom-right corner

Result:
- AI Hub always visible
- Never hidden by other apps
- Quick access to all features
```

### Example 2: **Stealth Mode** (Hidden Until Needed)
```
Settings:
- ❌ All Windows On Top (disabled)
- Use Ctrl+Alt+G to show/hide
- System tray icon for quick access

Result:
- AI Hub hidden by default
- Appears instantly with hotkey
- Doesn't clutter screen
```

### Example 3: **Hybrid Mode** (Player Always, Window On-Demand)
```
Settings:
- ✅ Floating Player On Top
- ❌ Main Window On Top
- Use Ctrl+Alt+G for main window

Result:
- Player always visible for TTS controls
- Main window appears when needed
- Best of both worlds
```

---

## 🐛 Troubleshooting

### Window not remembering position?
```
1. Move window to desired position
2. Open Window Manager (🎮)
3. Click "Save Current Position"
4. Restart AI Hub to test
```

### Window not remembering size?
```
1. Resize window to desired size
2. Open Window Manager (🎮)
3. Click "Save Current Size"
4. Restart AI Hub to test
```

### Always-on-top not working?
```
1. Open Window Manager (🎮)
2. Check if "All Windows On Top" is enabled
3. If enabled, disable and re-enable
4. Windows should update immediately
```

### Ctrl+Alt+G not working?
```
1. Check console for: "✅ Window Toggle Hotkey registered"
2. If not registered, restart AI Hub
3. Check for conflicts with other apps
4. Try running AI Hub as Administrator
```

### System tray icon not showing?
```
1. Check Windows system tray settings
2. Settings → Personalization → Taskbar
3. Enable "Show hidden icons"
4. Look for AI Hub icon
```

### Settings file corrupted?
```
1. Close AI Hub
2. Delete: config/window_settings.json
3. Restart AI Hub
4. Default settings will be created
```

---

## 💡 Pro Tips

### Tip 1: **Quick Reset**
```
Delete config/window_settings.json
Restart AI Hub
Fresh default layout!
```

### Tip 2: **Multi-Monitor Setup**
```
1. Move windows to preferred monitor
2. Save positions
3. Windows remember which monitor
```

### Tip 3: **Backup Your Layout**
```
Copy config/window_settings.json
Save as backup
Restore anytime by copying back
```

### Tip 4: **Share Layouts**
```
Export window_settings.json
Share with friends
They get your exact layout
```

### Tip 5: **Keyboard-Only Workflow**
```
Ctrl+Alt+G → Show window
Do your work
Ctrl+Alt+G → Hide window
Never touch mouse!
```

---

## 🎯 Recommended Setups

### For Productivity:
```
- Main window: 800x600, center screen
- Floating player: Bottom-right
- Always-on-top: Disabled
- Use Ctrl+Alt+G to toggle
```

### For Multitasking:
```
- Main window: 600x800, right side
- Floating player: Top-right
- Always-on-top: Enabled
- Always visible while working
```

### For Minimal Distraction:
```
- Main window: Hidden (Ctrl+Alt+G)
- Floating player: Small, bottom corner
- Player always-on-top: Enabled
- Main window always-on-top: Disabled
```

### For Presentation Mode:
```
- Main window: Full screen
- Floating player: Hidden
- Always-on-top: Enabled
- Demo AI features to audience
```

---

## 🌟 Advanced Features

### Auto-Save on Close:
- Window positions saved automatically
- Window sizes saved automatically
- No need to manually save
- Just close and reopen!

### Per-Window Control:
- Each window has independent settings
- Main window can be on-top
- While floating player is not
- Or vice versa!

### Global Override:
- "All Windows On Top" overrides individual settings
- Quick way to make everything stay visible
- Disable to return to individual settings

---

## 📊 System Status

```
Window Management Features:
├─ Ctrl+Alt+G Hotkey ............... ✅
├─ System Tray Icon ................ ✅
├─ Window Manager Panel ............ ✅
├─ Position Memory ................. ✅
├─ Size Memory ..................... ✅
├─ Always-On-Top (Global) .......... ✅
├─ Always-On-Top (Per-Window) ...... ✅
└─ Auto-Save on Close .............. ✅

Supported Windows:
├─ Main Window ..................... ✅
├─ Floating Player ................. ✅
└─ Window Manager Panel ............ ✅
```

---

## 🎊 You're Ready!

Your AI Hub now has **professional window management**:

🎮 **Ctrl+Alt+G** - Instant show/hide  
📍 **System Tray** - Click to access  
🎮 **Window Manager** - Full control panel  
💾 **Memory** - Remembers positions & sizes  
📌 **Always-On-Top** - Stay visible or hide  

**Try it now:**
1. Press Ctrl+Alt+G
2. See AI Hub appear
3. Press again to hide
4. Right-click tray icon
5. Open Window Manager
6. Customize your layout!

**Welcome to professional window control! 🚀**

---

**Built with ❤️ using PySide6 and Qt**

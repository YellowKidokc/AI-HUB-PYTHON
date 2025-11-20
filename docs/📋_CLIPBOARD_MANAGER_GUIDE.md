# 📋 Clipboard Manager Guide

## 🎉 Never Lose Your Clipboard Again!

The Clipboard Manager automatically saves everything you copy, lets you pin important items, assign hotkeys, and keeps it all synced to a JSON file!

---

## ⚡ Quick Start

### Open Clipboard Manager
Press **Ctrl+Alt+C** anywhere to open the clipboard manager window.

---

## 🎨 Features

### 📋 Automatic History
- **Auto-saves** everything you copy (up to 100 items)
- **Persistent** - survives restarts
- **Searchable** - find anything quickly
- **Organized** - Pinned items at top, recent below

### 📌 Pin Important Items
- Click the **📌 button** to pin an item
- Pinned items **never get deleted**
- Perfect for frequently used text, prompts, code snippets

### ⌨️ Assign Hotkeys
- Click the **⌨️ button** on any item
- Enter a hotkey like `ctrl+shift+1`
- Press that hotkey **anywhere** to copy that item!

### 🔍 Preview & Expand
- **Single click** an item to see it in the preview panel
- **Double-click** to expand and see the full content
- Perfect for long prompts or code

### 🏷️ Label Items
- Add labels to important items
- Makes them easier to find
- Shows at the top of each item

### 📋 Quick Actions
Each item has buttons on the right:
- **📋** - Copy to clipboard
- **📌** - Pin/Unpin
- **⌨️** - Set hotkey
- **🔍** - Preview full content
- **🗑️** - Delete (only if not pinned)

---

## 💾 Storage

### Where is it saved?
`config/clipboard_history.json`

### Can I sync it?
Yes! The JSON file can be:
- ✅ Backed up to cloud (Dropbox, Google Drive, OneDrive)
- ✅ Version controlled (Git)
- ✅ Copied between computers
- ✅ Edited manually (if needed)

### Sync Setup (Optional)
1. Move `config/clipboard_history.json` to your cloud folder
2. Create a symlink:
   ```bash
   mklink "config\clipboard_history.json" "C:\Users\YourName\Dropbox\clipboard_history.json"
   ```
3. Now it syncs across all your devices!

---

## 🎯 Use Cases

### 1. Frequently Used Text
Pin your:
- Email signatures
- Common responses
- Code snippets
- Templates

Assign hotkeys for instant access!

### 2. Long Prompts
- Copy a long AI prompt
- Pin it
- Label it "Marketing Prompt"
- Assign `Ctrl+Shift+M`
- Use it anytime with one keystroke!

### 3. Code Snippets
- Pin common code patterns
- Label them clearly
- Quick copy when coding

### 4. Research & Writing
- Save quotes, references, URLs
- Pin important ones
- Search through history

---

## ⌨️ Hotkeys

### Global Hotkeys
- **Ctrl+Alt+C** - Open Clipboard Manager

### Custom Item Hotkeys
You can assign any hotkey to any clipboard item:
- `ctrl+shift+1` through `ctrl+shift+9` - Quick access slots
- `ctrl+alt+[letter]` - Letter-based shortcuts
- Any valid keyboard combination

**Example Setup:**
- `ctrl+shift+1` → Your email
- `ctrl+shift+2` → Common code snippet
- `ctrl+shift+3` → Favorite prompt
- `ctrl+alt+s` → Signature

---

## 🎨 Layout

```
┌─────────────────────────────────────────────────────────┐
│  📋 Clipboard History    🗑️ Clear   🔍 Search...       │
├──────────────────────────┬──────────────────────────────┤
│                          │                              │
│  📌 PINNED               │   📄 Preview                 │
│  ┌────────────────────┐  │                              │
│  │ Item 1       📋📌⌨️│  │   Full content shows here    │
│  │ Item 2       📋📌⌨️│  │   when you click an item     │
│  └────────────────────┘  │                              │
│                          │                              │
│  🕒 RECENT               │   Actions:                   │
│  ┌────────────────────┐  │   📋 Copy  🏷️ Set Label     │
│  │ Item 3       📋📍🔍│  │                              │
│  │ Item 4       📋📍🔍│  │                              │
│  │ Item 5       📋📍🔍│  │                              │
│  └────────────────────┘  │                              │
│                          │                              │
└──────────────────────────┴──────────────────────────────┘
```

### Left Panel: Item List
- **Top section**: Pinned items (green pin 📌)
- **Bottom section**: Recent items (gray pin 📍)
- **Right side of each item**: Action buttons

### Right Panel: Preview
- Shows full content of selected item
- Copy button for quick access
- Set label button

---

## 🔧 Settings

### Max History
Default: 100 items (unpinned)
- Pinned items don't count toward limit
- Oldest unpinned items are removed first

### Auto-Monitoring
Checks clipboard every 1 second
- Minimal CPU usage
- Runs in background
- Can be disabled if needed

---

## 💡 Tips & Tricks

### 1. Pin Your Essentials
Pin items you use daily - they'll always be at the top and never get deleted.

### 2. Use Labels
Label pinned items so you can find them quickly:
- "Work Email"
- "Personal Email"
- "Code Template"
- "AI Prompt - Marketing"

### 3. Hotkey Strategy
Organize your hotkeys logically:
- `Ctrl+Shift+[1-9]` for your top 9 items
- `Ctrl+Alt+[letter]` for category-based (e.g., `Ctrl+Alt+E` for email)

### 4. Search is Your Friend
Use the search box to find anything in your history instantly.

### 5. Preview Before Copy
Double-check long items in the preview panel before copying.

### 6. Regular Cleanup
Click "🗑️ Clear Unpinned" occasionally to remove old items (keeps pinned ones).

---

## 🚀 Advanced: Cloud Sync

### Dropbox Example
```powershell
# Move file to Dropbox
move config\clipboard_history.json C:\Users\YourName\Dropbox\AI-Hub\

# Create symlink
mklink config\clipboard_history.json C:\Users\YourName\Dropbox\AI-Hub\clipboard_history.json
```

### Google Drive Example
```powershell
# Move file to Google Drive
move config\clipboard_history.json "C:\Users\YourName\Google Drive\AI-Hub\"

# Create symlink
mklink config\clipboard_history.json "C:\Users\YourName\Google Drive\AI-Hub\clipboard_history.json"
```

Now your clipboard history syncs across all your computers! 🎉

---

## 🐛 Troubleshooting

### Clipboard not monitoring?
- Check if `pyperclip` is installed: `pip install pyperclip`
- Restart AI Hub

### Hotkeys not working?
- Make sure hotkey isn't already used by another app
- Try a different combination
- Check console for error messages

### Items not saving?
- Check if `config/` folder exists
- Check file permissions
- Look for errors in console

### Window not showing?
- Press **Ctrl+Alt+C** again
- Check if it's behind other windows
- Try **Alt+Tab** to find it

---

## 📊 File Format

The clipboard history is stored in JSON:

```json
[
  {
    "id": "abc123_2025-01-19T10:30:00",
    "content": "Your clipboard text here",
    "timestamp": "2025-01-19T10:30:00",
    "pinned": true,
    "hotkey": "ctrl+shift+1",
    "label": "My Important Text"
  }
]
```

You can edit this file manually if needed!

---

## 🎯 Summary

✅ **Auto-saves** everything you copy  
✅ **Pin** important items  
✅ **Assign hotkeys** for instant access  
✅ **Search** through history  
✅ **Preview** before copying  
✅ **Label** for organization  
✅ **Persistent** across restarts  
✅ **Cloud-syncable** JSON storage  

**Press Ctrl+Alt+C to get started!** 🚀

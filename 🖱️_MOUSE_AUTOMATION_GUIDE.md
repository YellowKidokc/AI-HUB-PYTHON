And# 🖱️ Mouse Automation Guide

## 🎉 Click Anywhere with a Hotkey!

Perfect for toggling your mic, clicking buttons, or any repetitive mouse actions!

---

## ⚡ Quick Example: Mic Toggle

**Problem**: Your mic button is at the top of a 60" TV screen, hard to reach

**Solution**: Create a hotkey that clicks it for you!

```
1. Hover over your mic button
2. Open Position Recorder (⚡ Shortcuts tab)
3. Click "Record Position"
4. Create shortcut:
   - Hotkey: Ctrl+M
   - Action: Mouse Click
   - Position: (paste recorded position)
5. Press Ctrl+M anytime to toggle mic!
```

**Result**: Instant mic toggle from anywhere! 🎤

---

## 🚀 How to Set Up

### Step 1: Install pyautogui
```bash
pip install pyautogui
```

### Step 2: Find Your Click Position

#### Method A: Use Position Recorder (Recommended)
1. Open **⚡ Shortcuts** tab
2. Select **Action: Mouse Click**
3. Click **🎯 Open Position Recorder**
4. **Hover** over the button you want to click
5. Click **📍 Record This Position**
6. Click **📋 Copy Last Position**
7. Paste into the **Output** field

#### Method B: Manual Method
1. Move mouse to desired position
2. Run this in Python:
```python
import pyautogui
print(pyautogui.position())
```
3. Note the X, Y coordinates

### Step 3: Create the Shortcut
1. **Type**: Hotkey
2. **Action**: Mouse Click
3. **Modifiers**: Check Ctrl (or your preference)
4. **Key**: m (or your preference)
5. **Description**: Toggle mic
6. **Output**: Paste coordinates (e.g., `1850, 50`)
7. **Clicks**: 1 (Single)
8. Click **💾 Add / Save**

### Step 4: Restart & Test
1. Restart AI Hub
2. Press your hotkey (e.g., Ctrl+M)
3. Watch it click automatically! ✨

---

## 💡 Use Cases

### 1. **Mic Toggle** (Your Request!)
```
Position: Top of screen (mic button)
Hotkey: Ctrl+M
Clicks: 1
Result: Instant mic on/off
```

### 2. **Camera Toggle**
```
Position: Camera button
Hotkey: Ctrl+Shift+C
Clicks: 1
Result: Camera on/off
```

### 3. **Screen Share Toggle**
```
Position: Share screen button
Hotkey: Ctrl+Shift+S
Clicks: 1
Result: Start/stop sharing
```

### 4. **Mute All (Discord/Teams)**
```
Position: Mute all button
Hotkey: Ctrl+Shift+M
Clicks: 1
Result: Mute everyone
```

### 5. **Quick Save in Apps**
```
Position: Save button
Hotkey: Ctrl+Shift+S
Clicks: 1
Result: Click save without moving mouse
```

### 6. **Start/Stop Recording**
```
Position: Record button
Hotkey: Ctrl+R
Clicks: 1
Result: Toggle recording
```

---

## 🎯 Position Recorder Features

### Live Position Display
- Shows current mouse X, Y coordinates
- Updates in real-time (50ms refresh)
- Large, easy-to-read display

### Record Multiple Positions
- Record as many positions as you need
- See all recorded positions in list
- Copy any position to clipboard

### Test Before Using
- Click "Test Last Position"
- 2-second countdown
- Sees the click happen
- Confirms it works!

### Quick Actions
- **📍 Record** - Save current position
- **📋 Copy** - Copy to clipboard
- **🖱️ Test** - Test the click
- **🗑️ Clear** - Clear all positions

---

## ⚙️ Advanced Features

### Multiple Clicks
```
Clicks: 1 - Single click
Clicks: 2 - Double click
Clicks: 3 - Triple click
```

**Example**: Double-click to open file
```
Position: File icon coordinates
Clicks: 2 (Double)
Hotkey: Ctrl+O
```

### Click Sequences
Create multiple shortcuts for complex actions:
```
Shortcut 1: Ctrl+1 → Click position A
Shortcut 2: Ctrl+2 → Click position B
Shortcut 3: Ctrl+3 → Click position C

Press Ctrl+1, Ctrl+2, Ctrl+3 in sequence!
```

### Mouse Returns to Original Position
- After clicking, mouse returns to where it was
- You don't lose your place
- Seamless automation!

---

## 🔧 Technical Details

### How It Works:
1. **pyautogui** library controls mouse
2. Saves current mouse position
3. Moves to target coordinates
4. Performs click
5. Returns to original position
6. All in ~0.2 seconds!

### Safety Features:
- **Fail-safe**: Move mouse to corner to abort
- **Small pause**: 0.1s between actions
- **Error handling**: Won't crash if position invalid
- **Background thread**: Doesn't block UI

### Coordinate System:
- **Origin**: Top-left corner (0, 0)
- **X**: Increases to the right
- **Y**: Increases downward
- **Example**: (1920, 1080) = bottom-right on 1080p screen

---

## 💡 Pro Tips

### Tip 1: **Use Position Recorder**
```
Don't guess coordinates!
Use the Position Recorder tool
It's accurate and easy
```

### Tip 2: **Test Before Saving**
```
Use "Test Last Position" button
Make sure it clicks the right spot
Adjust if needed
```

### Tip 3: **Descriptive Names**
```
Good: "Toggle mic in Teams"
Bad: "Click thing"
You'll thank yourself later!
```

### Tip 4: **Multiple Monitors**
```
Position Recorder works across monitors
Coordinates span all screens
Record position on any monitor
```

### Tip 5: **Fixed UI Elements**
```
Works best for buttons that don't move
Mic button, camera button, etc.
Not ideal for dynamic content
```

### Tip 6: **Combine with Other Actions**
```
Create workflow:
1. Ctrl+M → Toggle mic
2. Ctrl+Space → Fix text
3. Ctrl+Enter → Send message
Complete automation!
```

---

## 🐛 Troubleshooting

### "pyautogui not installed"
```bash
pip install pyautogui
```

### Click happens at wrong position
```
1. Re-record position with Position Recorder
2. Make sure UI hasn't moved
3. Check if window is maximized/minimized
4. Test with "Test Last Position"
```

### Click doesn't work
```
1. Check coordinates are correct
2. Make sure target window is visible
3. Try increasing click count to 2
4. Check if button requires hover first
```

### Mouse moves but doesn't click
```
1. Check pyautogui is installed
2. Try running AI Hub as Administrator
3. Check antivirus isn't blocking
```

### Position changes when window moves
```
Solution: Always maximize the target window
Or: Record position when window is in specific location
```

---

## 📊 Example Shortcuts

### Mic Toggle (Teams)
```json
{
  "type": "Hotkey",
  "action": "Mouse Click",
  "modifiers": ["ctrl"],
  "trigger": "m",
  "desc": "Toggle mic in Teams",
  "output": "1850, 50"
}
```

### Camera Toggle (Zoom)
```json
{
  "type": "Hotkey",
  "action": "Mouse Click",
  "modifiers": ["ctrl", "shift"],
  "trigger": "c",
  "desc": "Toggle camera in Zoom",
  "output": "1750, 50"
}
```

### Screen Share (Discord)
```json
{
  "type": "Hotkey",
  "action": "Mouse Click",
  "modifiers": ["ctrl", "shift"],
  "trigger": "s",
  "desc": "Toggle screen share",
  "output": "1650, 50"
}
```

---

## 🎯 Your Mic Toggle Setup

**Based on your request:**

### Setup:
1. **Open Position Recorder**
2. **Hover over mic button** (top of 60" TV)
3. **Record position** (e.g., 1850, 50)
4. **Create shortcut**:
   - Hotkey: **Ctrl+M** (or your preference)
   - Action: **Mouse Click**
   - Position: **1850, 50** (your recorded position)
   - Clicks: **1**
   - Description: **Toggle mic**

### Usage:
```
Press Ctrl+M → Mic toggles instantly!
No more dragging mouse to top of screen
Works from anywhere
Less than 0.2 seconds
```

**Perfect for your 60" TV setup! 🎤**

---

## 🌟 What's Next?

You mentioned this would lead to your next idea...

**Possible next features:**
- **Click sequences** (multiple clicks in order)
- **Conditional clicks** (click if button is visible)
- **Image recognition** (find button by image)
- **Macro recording** (record mouse movements)
- **Scheduled clicks** (click at specific times)

**Let me know what you're thinking! 🚀**

---

## 🎊 You're Ready!

You now have:
- 🖱️ **Mouse automation** - Click anywhere with hotkeys
- 🎯 **Position Recorder** - Find exact coordinates
- 🎤 **Mic toggle** - Perfect for your 60" TV
- ⚡ **Instant clicks** - Less than 0.2 seconds
- 🔄 **Auto-return** - Mouse goes back to original position

**Create your mic toggle shortcut now:**
1. Open ⚡ Shortcuts tab
2. Click 🎯 Position Recorder
3. Record your mic button position
4. Create the shortcut
5. Restart AI Hub
6. Press Ctrl+M to toggle!

**No more dragging to the top of the screen! 🎉**

---

**Built with ❤️ using pyautogui**

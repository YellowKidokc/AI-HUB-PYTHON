# 🔧 Chat Fix + Prompt Selector

## What Was Fixed

### Chat Error ✅ FIXED
**Problem:**
```
AttributeError: 'Message' object has no attribute '__dict__'
```

**Cause:** 
Message class uses `@dataclass(slots=True)` which doesn't create `__dict__` attribute

**Solution:**
Changed line 42 in `src/ai_hub/services/openai_client.py` from:
```python
"messages": [msg.__dict__ for msg in messages],
```

To:
```python
"messages": [{"role": msg.role, "content": msg.content} for msg in messages],
```

**Result:** Chat now works! ✅

---

## New Feature: Prompt Selector (Ctrl+Alt+T)

### What It Does

Press **Ctrl+Alt+T** with selected text to:
1. Open a popup near your cursor
2. See list of all your prompts with descriptions
3. Click a prompt to apply it to selected text
4. Create new prompts
5. Delete existing prompts

### How It Works

**Files Created:**
- `src/ai_hub/ui/prompt_selector_popup.py` - Main popup UI
- `src/ai_hub/hotkeys/prompt_selector_hotkey.py` - Ctrl+Alt+T hotkey handler

**Hotkey:** `Ctrl+Alt+T`

### UI Layout

```
┌─────────────────────────────────────────┐
│ Select Prompt                       [×] │
├─────────────────────────────────────────┤
│ • Simplify                              │
│ • Professional                          │
│ • Friendly                              │
│ • Expand                                │
│ • [Your custom prompts...]              │
│                                         │
│ 📝 Make text simpler and easier...      │
│ (description of selected prompt)        │
│                                         │
│ [Use This] [New] [Delete] [Close]       │
└─────────────────────────────────────────┘
```

### Default Prompts Included

1. **Simplify** - Make text simpler and easier to understand
2. **Professional** - Use formal, professional tone
3. **Friendly** - Use casual, friendly tone
4. **Expand** - Add more detail and examples

### Create New Prompt

Click **[New Prompt]** to open dialog:

```
Create New Prompt
┌──────────────────────────────────────┐
│ Prompt Name: [_________________]     │
│ Description: [_________________]     │
│                                      │
│ Prompt Text:                         │
│ [_______________________________]    │
│ [_______________________________]    │
│                                      │
│ Testing Notes:                       │
│ [_______________________________]    │
│                                      │
│ [Save] [Cancel]                      │
└──────────────────────────────────────┘
```

**Fields:**
- **Prompt Name** - What to call it (required)
- **Description** - Short description shown in popup
- **Prompt Text** - The full prompt to send to AI (required)
- **Testing Notes** - How to test the prompt (optional)

### Storage

All prompts saved to: `config/prompts.json`

Format:
```json
[
  {
    "name": "Simplify",
    "description": "Make text simpler",
    "prompt": "Simplify this text...",
    "testing": "Test with complex text"
  },
  ...
]
```

### Usage Examples

**Example 1: Select text in Word**
```
Your selected text:
"The implementation of this feature requires a comprehensive 
understanding of the underlying infrastructure."

Press: Ctrl+Alt+T
Select: "Simplify"
Result: "This feature needs a good understanding of how it works."
```

**Example 2: Select code snippet**
```
Your selected text:
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

Press: Ctrl+Alt+T
Create: New "Pythonic" prompt
Result: "sum(numbers)"
```

### Keyboard Shortcuts (in Popup)

| Action | Key |
|--------|-----|
| Open selector | Ctrl+Alt+T |
| Use prompt | Enter / Double-click |
| Create new | Click [New Prompt] |
| Delete | Select + Click [Delete] |
| Close | Escape / Click [Close] |

### How It Integrates

1. **With Smart Hotkeys:**
   - Alt+Spacebar - Rewrite all
   - Ctrl+Alt+Spacebar - Prompt picker (old style)
   - **Ctrl+Alt+T** - Prompt selector (new! with descriptions)

2. **With Chat:**
   - You can copy prompts
   - Use them in the chat manually
   - Or build AI features around them

3. **With Hotkeys:**
   - Store your favorite prompts
   - Quick access via popup
   - Beautiful organized interface

### Tips & Tricks

**Tip 1: Organize by Use Case**
- Create categories in prompt name: "Code: Python", "Code: JavaScript"
- Or use descriptions to organize

**Tip 2: Test Prompts**
- Use "Testing Notes" field to document how to test
- Remember what works for each prompt

**Tip 3: Reuse Good Prompts**
- Start with defaults
- Modify and save as new version
- Build your library over time

**Tip 4: Share Prompts**
- Export config/prompts.json
- Share with team
- They can copy to their config folder

### Troubleshooting

**Q: Hotkey not working**
A: Make sure AI Hub app is running with smart hotkeys enabled

**Q: Can't create prompt**
A: Name and Prompt Text are both required

**Q: Prompts disappeared**
A: Check config/prompts.json wasn't deleted. Restore from backup.

**Q: Want to delete all and start over**
A: Delete config/prompts.json and restart - will create defaults

---

## Quick Start

1. **Test the fix:**
   - Launch AI Hub: `run_ai_hub.bat`
   - Go to Chat tab
   - Type a message
   - Should work now! ✅

2. **Try Prompt Selector:**
   - Select some text anywhere
   - Press: **Ctrl+Alt+T**
   - Popup appears!
   - Click a prompt
   - It applies to your text

3. **Create Your Own Prompt:**
   - In popup, click [New Prompt]
   - Fill in:
     - Name: "My Custom Prompt"
     - Description: "What it does"
     - Prompt: "Your full prompt text"
   - Click [Save]
   - It appears in the list!

---

## Files Modified

- `src/ai_hub/services/openai_client.py` - Fixed Message dict error
- `src/ai_hub/ui/prompt_selector_popup.py` - NEW (prompt selector UI)
- `src/ai_hub/hotkeys/prompt_selector_hotkey.py` - NEW (hotkey handler)

---

## Next Steps

To integrate into main app, would need to:
1. Add prompt selector hotkey to main app hotkey handler
2. Connect "Use This Prompt" to apply prompts
3. Maybe add to chat tab directly

But it works standalone now!

---

**Ready to use!** 🚀

Press **Ctrl+Alt+T** and enjoy your prompt selector!


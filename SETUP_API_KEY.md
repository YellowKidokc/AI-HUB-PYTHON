# 🔑 API Key Setup Guide

## ⚠️ IMPORTANT: Your API Key is Not Configured!

The app won't work properly until you add your OpenAI API key.

---

## 🚀 Quick Setup (2 Minutes)

### Step 1: Get Your API Key

1. Go to: https://platform.openai.com/api-keys
2. Log in to your OpenAI account
3. Click **"Create new secret key"**
4. **Copy the key** (starts with `sk-`)
5. **Save it somewhere safe** - you can't see it again!

### Step 2: Add Key to AI Hub

**Option A: Edit settings.ini (Recommended)**

1. Open `settings.ini` in this folder
2. Find this line:
   ```ini
   api_key = sk-your-api-key-here
   ```
3. Replace `sk-your-api-key-here` with your actual key:
   ```ini
   api_key = sk-proj-abc123xyz...
   ```
4. Save the file
5. Restart AI Hub

**Option B: Use Environment Variable**

1. Press `Win + R`
2. Type: `sysdm.cpl` and press Enter
3. Go to **Advanced** → **Environment Variables**
4. Under **User variables**, click **New**
5. Variable name: `OPENAI_API_KEY`
6. Variable value: Your API key (starts with `sk-`)
7. Click OK
8. Restart your computer
9. Restart AI Hub

---

## ✅ Verify It's Working

After adding your key:

1. **Restart AI Hub**
2. Go to **💬 Chat** tab
3. Type a message
4. If it responds → **Success!** ✅
5. If error → Check your key is correct

---

## 🎯 What Works With API Key

Once configured, the API key unlocks:

✅ **💬 Chat** - Full AI conversations  
✅ **✏️ Spelling** - Grammar/spelling fixes (Ctrl+Space)  
✅ **📝 Prompts** - All custom prompts  
✅ **⚡ Shortcuts** - AI-powered shortcuts  
✅ **Hotstrings** - AI text expansion (;fix, ;clar, etc.)  
✅ **Hotkeys** - Ctrl+Space, Ctrl+Alt+P work everywhere  

**The key is UNIVERSAL - it works across ALL features!**

---

## 💰 API Costs

OpenAI charges per token used:

- **gpt-4o-mini** (default): ~$0.15 per 1M input tokens
- Very cheap for normal use
- Example: 100 chat messages ≈ $0.01-0.05

**Monitor usage:** https://platform.openai.com/usage

---

## 🔒 Security Tips

### ✅ DO:
- Keep your API key private
- Add `settings.ini` to `.gitignore` if using Git
- Use environment variable for extra security
- Rotate keys periodically

### ❌ DON'T:
- Share your API key publicly
- Commit it to GitHub
- Give it to others
- Use it in public code

---

## 🐛 Troubleshooting

### "API key is not configured"
- Check `settings.ini` has your real key
- Make sure no extra spaces
- Key should start with `sk-`
- Restart AI Hub after editing

### "Invalid API key"
- Key might be wrong - copy it again
- Check for typos
- Verify key is active at https://platform.openai.com/api-keys

### "Rate limit exceeded"
- You're making too many requests
- Wait a few minutes
- Check your OpenAI account limits

### Features still don't work
- Make sure you **restarted AI Hub** after adding key
- Check console for error messages
- Verify key at: https://platform.openai.com/api-keys

---

## 🎓 Example settings.ini

```ini
[openai]
# Get your API key from https://platform.openai.com/api-keys
api_key = sk-proj-abc123xyz789...YOUR_ACTUAL_KEY_HERE
endpoint = https://api.openai.com/v1/chat/completions
model = gpt-4o-mini
timeout = 120

[hotkeys]
spelling = ctrl+space
prompt_navigator = ctrl+alt+p
goto_hub = ctrl+alt+shift+k
toggle_hotstrings = ctrl+alt+h

[hotstrings]
enabled = true
buffer_size = 64
```

---

## 🌐 Alternative: Use Different Model

You can use other OpenAI-compatible APIs:

### Local Models (Free!)
```ini
api_key = not-needed
endpoint = http://localhost:1234/v1/chat/completions
model = local-model
```

### Other Providers
- **OpenRouter**: https://openrouter.ai/
- **Together AI**: https://together.ai/
- **Groq**: https://groq.com/

Just change the `endpoint` and `api_key` in settings.ini!

---

## 🆘 Still Need Help?

1. Check the console output when starting AI Hub
2. Look for error messages
3. Verify your API key at OpenAI's website
4. Make sure you have credits in your OpenAI account

---

**Once you add your API key, ALL AI features will work universally across the entire app!** 🚀

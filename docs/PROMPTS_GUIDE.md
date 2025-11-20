# 📝 Prompts Manager Guide

Complete guide to creating and managing AI prompts in AI Hub.

---

## 🎯 What Are Prompts?

Prompts are **reusable AI instructions** that transform selected text. Instead of typing the same instructions repeatedly, create a prompt once and use it anywhere!

### Examples:
- **Fix Grammar** - Correct spelling and grammar errors
- **Make Professional** - Rewrite in business tone
- **Summarize** - Create brief summaries
- **Simplify** - Use simpler language
- **Translate** - Convert to another language

---

## 🚀 Quick Start

### 1. Open Prompts Manager
Click the **📝 Prompts** tab in AI Hub

### 2. Create Your First Prompt
1. Click **➕ New Prompt**
2. Fill in the form:
   - **Title**: "Fix Grammar"
   - **Description**: "Correct spelling and grammar"
   - **Prompt**: "Fix the spelling and grammar in the following text:"
   - **Replace**: ✅ Checked
3. Click **Save**

### 3. Use Your Prompt
1. Select text in **any application**
2. Go to AI Hub → Prompts tab
3. Select your prompt
4. Click **▶️ Run on Selected Text**
5. Watch your text transform! ✨

---

## 📋 Creating Prompts

### The Form

#### 📝 Title (Required)
- Short, descriptive name
- Shows in the list
- Examples: "Fix Grammar", "Make Professional", "Summarize"

#### 📄 Description (Optional)
- Brief explanation of what the prompt does
- Helps you remember its purpose
- Shows in the preview panel

#### 🤖 System Message (Optional)
- Sets the AI's role and behavior
- Examples:
  - "You are a professional editor"
  - "You are a helpful translator"
  - "You are a technical writer"
- Leave blank for general-purpose prompts

#### 💬 User Prompt (Required)
- The actual instruction sent to AI
- Selected text is automatically appended
- Be clear and specific!

**Examples:**
```
Fix the spelling and grammar in the following text:

Rewrite the following in a professional tone:

Summarize the following text in 2-3 sentences:

Translate the following to Spanish:
```

#### ⚙️ Options

**Replace Selected Text**
- ✅ **Checked**: Replaces your selected text with AI result
- ❌ **Unchecked**: Shows result in a popup window

**Temperature (0.0 - 2.0)**
- **0.0**: Focused, consistent, deterministic
- **0.2**: Slightly varied (good default)
- **0.7**: Creative, varied
- **2.0**: Very creative, unpredictable

**When to use:**
- **0.0**: Grammar fixes, translations, factual tasks
- **0.2-0.5**: Rewriting, summarizing, general tasks
- **0.7-1.0**: Creative writing, brainstorming
- **1.0+**: Experimental, very creative

---

## 🎨 Prompt Examples

### 1. Fix Spelling & Grammar
```
Title: Fix Spelling & Grammar
Description: Correct spelling and grammar errors
System: You are a professional editor. Reply ONLY with the corrected text—no explanations.
Prompt: Fix the spelling and grammar in the following text:
Replace: ✅ Yes
Temperature: 0.0
```

### 2. Make Professional
```
Title: Make Professional
Description: Rewrite in business-appropriate tone
System: (leave blank)
Prompt: Rewrite the following text in a professional, business-appropriate tone:
Replace: ✅ Yes
Temperature: 0.2
```

### 3. Simplify Language
```
Title: Simplify
Description: Use simpler words and shorter sentences
System: (leave blank)
Prompt: Simplify the following text. Use simple words and short sentences that anyone can understand:
Replace: ✅ Yes
Temperature: 0.2
```

### 4. Summarize
```
Title: Summarize
Description: Create a brief summary
System: (leave blank)
Prompt: Summarize the following text in 2-3 sentences:
Replace: ❌ No (show in popup)
Temperature: 0.2
```

### 5. Expand with Details
```
Title: Expand
Description: Add more detail and examples
System: (leave blank)
Prompt: Expand the following text with more details, examples, and explanations:
Replace: ✅ Yes
Temperature: 0.5
```

### 6. Translate to Spanish
```
Title: Translate to Spanish
Description: Convert English to Spanish
System: You are a professional translator. Translate accurately while preserving tone and meaning.
Prompt: Translate the following English text to Spanish:
Replace: ❌ No (show in popup)
Temperature: 0.1
```

### 7. Find Action Items
```
Title: Find Action Items
Description: Extract tasks and to-dos
System: (leave blank)
Prompt: Identify all action items in the following text and list them as bullet points:
Replace: ❌ No (show in popup)
Temperature: 0.2
```

### 8. Make Friendly
```
Title: Make Friendly
Description: Use casual, warm tone
System: (leave blank)
Prompt: Rewrite the following text in a casual, friendly, and approachable tone:
Replace: ✅ Yes
Temperature: 0.5
```

---

## 🔧 Managing Prompts

### Editing Prompts
1. Select a prompt in the list
2. Click **✏️ Edit**
3. Make your changes
4. Click **Save**

### Deleting Prompts
1. Select a prompt
2. Click **🗑️ Delete**
3. Confirm deletion

### Reordering Prompts
1. Select a prompt
2. Click **⬆️ Move Up** or **⬇️ Move Down**
3. Order is saved automatically

**Why reorder?**
- Put frequently-used prompts at the top
- Group similar prompts together
- Create a logical workflow

---

## 💡 Pro Tips

### Tip 1: Be Specific
```
❌ Bad: "Make this better"
✅ Good: "Rewrite this email in a professional tone, keeping it under 100 words"
```

### Tip 2: Use System Messages for Consistency
```
System: You are a technical writer. Use clear, precise language.
Prompt: Explain the following technical concept:
```

### Tip 3: Test Temperature Settings
- Start with 0.2 for most tasks
- Increase for creative tasks
- Decrease for factual tasks

### Tip 4: Create Specialized Prompts
```
- "Email - Professional"
- "Email - Friendly"
- "Email - Apology"
- "Email - Thank You"
```

### Tip 5: Use Replace Wisely
- **Replace = Yes**: Quick edits, rewrites
- **Replace = No**: Summaries, analysis, translations (keep original)

### Tip 6: Chain Prompts
1. Run "Fix Grammar" first
2. Then run "Make Professional"
3. Finally run "Make Shorter"

---

## 🎯 Common Use Cases

### For Writers
- Fix grammar and spelling
- Improve clarity
- Adjust tone (formal/casual)
- Expand or shorten text

### For Business
- Professional emails
- Meeting summaries
- Action item extraction
- Report writing

### For Students
- Essay improvement
- Simplify complex text
- Summarize readings
- Citation formatting

### For Developers
- Code documentation
- Explain technical concepts
- Bug report writing
- Commit message improvement

### For Content Creators
- Social media posts
- Video descriptions
- Blog post editing
- SEO optimization

---

## 🔥 Advanced Techniques

### Multi-Step Prompts
Create a series of prompts for complex workflows:
```
1. "Extract Key Points"
2. "Organize by Priority"
3. "Format as Bullet Points"
```

### Context-Aware Prompts
Include context in your prompt:
```
Prompt: You are writing a technical blog post for developers. 
Rewrite the following paragraph to be more engaging:
```

### Conditional Instructions
```
Prompt: If the following text is formal, make it casual. 
If it's casual, make it formal:
```

### Format-Specific Prompts
```
- "Format as Markdown"
- "Format as Email"
- "Format as Bullet Points"
- "Format as JSON"
```

---

## 📊 Workflow Examples

### Email Workflow
1. Write rough draft
2. Run "Fix Grammar"
3. Run "Make Professional"
4. Run "Make Shorter" (if needed)
5. Send!

### Content Creation Workflow
1. Write initial content
2. Run "Improve Clarity"
3. Run "Add Examples"
4. Run "SEO Optimize"
5. Publish!

### Study Workflow
1. Copy complex text
2. Run "Simplify"
3. Run "Summarize"
4. Run "Create Study Questions"
5. Study!

---

## 🐛 Troubleshooting

### Prompt doesn't work
- Check API key is configured
- Ensure text is selected
- Try simpler instructions
- Check temperature setting

### Results are inconsistent
- Lower temperature (0.0-0.2)
- Add more specific instructions
- Use system message for consistency

### Results are too creative
- Lower temperature
- Add "Be concise" to prompt
- Use system message: "Reply ONLY with the requested output"

### Results are too boring
- Increase temperature (0.5-1.0)
- Remove restrictive instructions
- Add "Be creative" to prompt

---

## 💾 Data Storage

Prompts are saved in:
```
config/prompts_manager.json
```

**Backup your prompts:**
```bash
copy config\prompts_manager.json config\prompts_backup.json
```

**Share prompts:**
- Copy the JSON file
- Send to others
- They can import by replacing their file

---

## 🎊 You're Ready!

You now have:
- ✅ Complete prompt management
- ✅ No hardcoding needed
- ✅ Full CRUD operations
- ✅ Reordering capability
- ✅ Professional workflow

**Start creating prompts and automate your writing! 🚀**

---

## 📚 Related Guides

- [Quick Start Guide](../QUICKSTART.md)
- [First Time Setup](../README_FIRST_TIME_SETUP.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [FAQ](FAQ.md)

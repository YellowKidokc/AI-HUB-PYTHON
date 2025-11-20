# 🔍 Search Scraper Guide

## ⚠️ IMPORTANT WARNING

**Web scraping may violate search engine Terms of Service and can result in temporary IP bans!**

Use this tool:
- ✅ Responsibly and sparingly
- ✅ With delays between requests
- ✅ Preferably with a proxy
- ❌ NOT for commercial scraping
- ❌ NOT for high-volume automated searches

---

## 🚀 Quick Start

1. **Open AI Hub** and go to the **🔍 Search** tab
2. **Enter your query**
3. **Select search engine** (Google, Bing, Yahoo, DuckDuckGo, AOL, Mojeek)
4. **Set number of pages** (1-5, start with 1!)
5. **Click Search**

---

## 🎯 Features

### 🔍 Multiple Search Engines
- **Google** - Most comprehensive results
- **Bing** - Microsoft's search engine
- **Yahoo** - Powered by Bing
- **DuckDuckGo** - Privacy-focused
- **AOL** - Classic search
- **Mojeek** - Independent crawler

### 📊 Export Options
- **📋 Copy All** - Copy links to clipboard
- **💾 TXT** - Plain text file (one URL per line)
- **💾 JSON** - Structured data with metadata
- **💾 CSV** - Spreadsheet-compatible format

### 🛡️ Safety Features
- **Page limit** - Max 5 pages to reduce ban risk
- **Proxy support** - Route through proxy server
- **Delay settings** - Configurable delays (1-10 seconds)
- **Warning prompts** - Confirms before risky operations

---

## 🛡️ How to Avoid Getting Banned

### 1. **Use Fewer Pages**
- Start with **1 page** (10-15 results)
- Only increase if absolutely necessary
- More pages = higher ban risk

### 2. **Add Delays**
- Default: 3 seconds between requests
- Increase to 5-10 seconds for safety
- Mimics human browsing behavior

### 3. **Use a Proxy (Recommended)**
- Protects your real IP address
- Reduces ban risk significantly
- Format: `http://proxy:port` or `socks5://proxy:port`

**Free Proxy Lists:**
- https://www.proxy-list.download/
- https://free-proxy-list.net/
- https://www.sslproxies.org/

### 4. **Don't Overuse**
- Limit searches to a few per day
- Spread out searches over time
- Use different search engines

### 5. **Rotate Search Engines**
- Don't hammer one engine repeatedly
- Switch between Google, Bing, DuckDuckGo
- Each has separate rate limits

---

## 📖 Usage Examples

### Example 1: Basic Search
```
Query: "python web scraping tutorial"
Engine: Google
Pages: 1
Proxy: None
```
**Result:** ~10-15 URLs

### Example 2: Safe Multi-Page Search
```
Query: "machine learning datasets"
Engine: DuckDuckGo
Pages: 2
Proxy: http://proxy.example.com:8080
Delay: 5 seconds
```
**Result:** ~20-30 URLs (safer with proxy)

### Example 3: Research Project
```
Query: "climate change research papers"
Engine: Bing
Pages: 3
Proxy: socks5://proxy.example.com:1080
Delay: 7 seconds
```
**Result:** ~30-45 URLs (maximum safety)

---

## 💾 Export Formats

### TXT Format
```
https://example.com/page1
https://example.com/page2
https://example.com/page3
```

### JSON Format
```json
{
  "query": "python tutorial",
  "engine": "Google",
  "count": 15,
  "results": [
    "https://example.com/page1",
    "https://example.com/page2"
  ]
}
```

### CSV Format
```csv
URL
https://example.com/page1
https://example.com/page2
```

---

## 🔧 Proxy Setup

### Finding Free Proxies
1. Visit proxy list websites (see above)
2. Look for:
   - **HTTP/HTTPS** proxies (easiest)
   - **SOCKS5** proxies (more secure)
   - High uptime percentage
   - Recent last check time

### Proxy Format
```
HTTP:    http://ip:port
HTTPS:   https://ip:port
SOCKS5:  socks5://ip:port
```

### Example Proxies
```
http://123.45.67.89:8080
https://98.76.54.32:3128
socks5://11.22.33.44:1080
```

### Testing Proxies
- Try a simple 1-page search first
- If it fails, try a different proxy
- Free proxies can be unreliable

---

## 🚨 Troubleshooting

### "Search failed: Connection error"
- **Cause:** Network issue or proxy down
- **Fix:** 
  - Check internet connection
  - Try without proxy
  - Try different proxy

### "Search failed: Timeout"
- **Cause:** Search engine not responding
- **Fix:**
  - Increase timeout (edit code if needed)
  - Try different search engine
  - Check if you're banned (wait 24 hours)

### "No results found"
- **Cause:** Query too specific or engine blocked
- **Fix:**
  - Try broader query
  - Try different search engine
  - Check if you're banned

### "Temporary Ban"
- **Symptoms:** CAPTCHAs, no results, errors
- **Fix:**
  - Wait 24-48 hours
  - Use proxy next time
  - Reduce pages and add delays

---

## 📊 Best Practices

### ✅ DO:
- Start with 1 page
- Use delays (3+ seconds)
- Use proxies when possible
- Rotate search engines
- Export results immediately
- Respect rate limits

### ❌ DON'T:
- Scrape 5+ pages at once
- Run searches in rapid succession
- Use without delays
- Scrape for commercial purposes
- Ignore ban warnings
- Automate high-volume searches

---

## 🎓 Use Cases

### 1. Research
- Gather URLs for academic research
- Find relevant papers/articles
- Collect data sources

### 2. SEO Analysis
- Check search rankings
- Analyze competitor results
- Monitor keyword positions

### 3. Content Discovery
- Find relevant content
- Discover new sources
- Research topics

### 4. Data Collection
- Build URL datasets
- Create link lists
- Compile resources

---

## ⚖️ Legal & Ethical Considerations

### Terms of Service
Most search engines prohibit automated scraping in their TOS:
- **Google:** Prohibits automated queries
- **Bing:** Limits automated access
- **Yahoo:** Restricts bots

### Ethical Use
- Use for personal research only
- Don't overload servers
- Respect robots.txt
- Don't sell scraped data
- Attribute sources properly

### Alternatives
Consider official APIs when available:
- **Google Custom Search API** (100 free queries/day)
- **Bing Web Search API** (1000 free queries/month)
- **DuckDuckGo Instant Answer API** (free, limited)

---

## 🔒 Privacy & Security

### Your Privacy
- Search engines can see your IP
- Queries are logged
- Use proxy to mask IP
- Use VPN for extra privacy

### Data Security
- Results saved locally only
- No data sent to third parties
- Export files stored on your PC
- Delete exports when done

---

## 📈 Rate Limits (Estimated)

| Engine | Safe Limit | Risk Level |
|--------|-----------|------------|
| Google | 1-2 pages | HIGH |
| Bing | 2-3 pages | MEDIUM |
| Yahoo | 2-3 pages | MEDIUM |
| DuckDuckGo | 3-5 pages | LOW |
| AOL | 2-3 pages | MEDIUM |
| Mojeek | 3-5 pages | LOW |

**Note:** These are rough estimates. Actual limits vary.

---

## 🎯 Summary

✅ **Installed** - Search scraper ready to use  
⚠️ **Use carefully** - Risk of temporary bans  
🛡️ **Use proxies** - Reduces ban risk  
⏱️ **Add delays** - Mimics human behavior  
📊 **Export results** - Save to TXT/JSON/CSV  
🔄 **Rotate engines** - Don't overuse one  

**Access via: AI Hub → 🔍 Search tab**

---

## 🆘 Getting Help

If you get banned:
1. **Wait 24-48 hours**
2. **Clear cookies** (if using browser)
3. **Change IP** (restart router or use VPN)
4. **Use proxy** next time
5. **Reduce pages** to 1-2

If you have issues:
1. Check console for error messages
2. Try different search engine
3. Test without proxy first
4. Verify internet connection

---

**Remember: Use responsibly! This is a research tool, not for commercial scraping.** 🔍

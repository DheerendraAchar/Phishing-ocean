# Quick Feature Guide 🚀

## Your Dashboard Now Has:

### 🎛️ Control Panel (Top Right)

```
┌─────────────────────────────────────────┐
│ Last Updated: 2025-10-22 21:45:32      │
│ ┌─────────────────────────────────────┐ │
│ │     🔄 Refresh Data                 │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ ⚡ Auto-Refresh  [OFF]  [5 min ▼]      │
│ 📊 Demo Mode     [ON]                   │
│ 🌙 Dark Mode     [OFF]                  │
└─────────────────────────────────────────┘
```

### 🔍 Filter Bar (Above Charts)

```
┌───────────────────────────────────────────────────────────────┐
│  Time Range: [Last 24 Hours ▼] │ Attack Type: [All ▼]        │
│  Brand: [All Brands ▼]          │ Country: [All Countries ▼]  │
└───────────────────────────────────────────────────────────────┘
```

---

## Feature Quick Start

### ⏱️ Auto-Refresh
**Turn ON:**
1. Click "Auto-Refresh" toggle → ON
2. Select interval: 1 min / 5 min / 15 min
3. Dashboard updates automatically!

**Turn OFF:**
- Click toggle → OFF

---

### 🌙 Dark Mode
**Enable:**
- Click "Dark Mode" toggle → ON
- Entire dashboard switches to dark theme

**Disable:**
- Click toggle → OFF

---

### 📅 Filters

**Time Range:**
- Click dropdown → Select:
  - Last 24 Hours (most recent)
  - Last 7 Days (weekly)
  - Last 30 Days (monthly)
  - All Time (everything)

**Attack Type:**
- Click dropdown → Select attack type
- Examples: Fake Login Page, Malicious Link

**Brand:**
- Click dropdown → Select brand
- Examples: PayPal, Microsoft, Google

**Country:**
- Click dropdown → Select country
- Examples: United States, Russia, China

**Clear Filters:**
- Select "All" in each dropdown

---

## Common Usage Patterns

### Pattern 1: Real-Time Monitoring
```
Auto-Refresh: ON (5 min)
Demo Mode: OFF
Time Range: Last 24 Hours
Dark Mode: ON
```
**Use case:** 24/7 SOC monitoring

### Pattern 2: Brand Analysis
```
Auto-Refresh: OFF
Time Range: Last 7 Days
Brand: PayPal
Dark Mode: OFF
```
**Use case:** Analyzing PayPal targeting

### Pattern 3: Geographic Analysis
```
Time Range: Last 30 Days
Country: Russia
Attack Type: Fake Login Page
Dark Mode: OFF
```
**Use case:** Studying Russian attack patterns

### Pattern 4: Demo/Presentation
```
Demo Mode: ON
Dark Mode: ON
Auto-Refresh: ON (1 min)
Time Range: All Time
```
**Use case:** Live demo with automatic updates

---

## Tips & Tricks

✅ **Combine filters** for detailed analysis  
✅ **Use dark mode** for extended monitoring  
✅ **Auto-refresh** keeps data current  
✅ **Filter first**, then enable auto-refresh  
✅ **Demo mode** for testing/presentations  

---

## Keyboard Shortcuts

(Future enhancement - not yet implemented)
- `D` - Toggle dark mode
- `R` - Manual refresh
- `A` - Toggle auto-refresh
- `Esc` - Clear all filters

---

## Feature Status

| Feature | Status | Performance |
|---------|--------|-------------|
| Auto-Refresh | ✅ Working | Excellent |
| Dark Mode | ✅ Working | Instant |
| Time Filter | ✅ Working | Real-time |
| Attack Filter | ✅ Working | Real-time |
| Brand Filter | ✅ Working | Real-time |
| Country Filter | ✅ Working | Real-time |

---

## What Changes When You Filter?

### Everything Updates:
- ✅ Total Attacks count
- ✅ Most Targeted Brand
- ✅ Primary Source Region
- ✅ Primary Attack Vector
- ✅ Global Threat Map
- ✅ Brand Impersonation Treemap
- ✅ Attack Frequency Timeline

### Example:
**Before filtering:**
- Total Attacks: 100
- Top Brand: Microsoft (14)

**After filtering (Time: Last 7 Days, Brand: PayPal):**
- Total Attacks: 8
- Top Brand: PayPal (8)
- Map shows only PayPal attacks
- Timeline shows only last 7 days

---

## Troubleshooting

**Auto-refresh not working?**
- Check toggle is ON
- Verify interval is selected
- Data updates appear in "Last Updated" timestamp

**Dark mode looks weird?**
- Refresh page after toggling
- Some chart elements may need reload

**Filters show no data?**
- Too restrictive - broaden criteria
- Try "All Time" range
- Check multiple filters aren't conflicting

**Dropdown is empty?**
- Click "Refresh Data" first
- Ensure Demo Mode is ON or live data loaded

---

## Access Dashboard

🌐 http://localhost:8050

**Try it now!**

# 📊 Live Statistics Dashboard - Data Update Explanation

## Current Implementation: **Near Real-Time** ⏱️

### How It Works

The dashboard uses a **hybrid approach** between real-time and cached data:

## 🔄 Data Flow

```
OpenPhish API (Live Feed)
         ↓
    Cache Layer (1 hour TTL)
         ↓
  Manual/Auto Refresh
         ↓
   Dashboard Display
```

## ⚙️ Update Mechanisms

### 1. **Manual Refresh** (Active)
- ✅ **Click "Refresh Data" button** → Fetches fresh data immediately
- ✅ **Toggle Sample/Live Data** → Switches data source instantly
- Updates all visualizations in real-time

### 2. **Auto-Refresh Interval** (Currently Disabled)
- ⏸️ **Status**: Disabled by default
- ⏰ **Interval**: 5 minutes (300,000 ms) when enabled
- 🔧 **Configure in**: `config.py` → `DATA_REFRESH_INTERVAL`

### 3. **Cache System**
- 💾 **Duration**: 1 hour (3600 seconds)
- 📁 **Location**: `cache/phishing_data.json`
- 🎯 **Purpose**: Reduces API load and improves performance
- 🔧 **Configure in**: `config.py` → `CACHE_DURATION`

## 📈 Current Configuration

```python
# config.py
CACHE_DURATION = 3600        # 1 hour cache
DATA_REFRESH_INTERVAL = 300000  # 5 min auto-refresh (disabled)
```

## 🔴 Is It "Real-Time"?

### **Short Answer**: Near real-time with manual control

| Feature | Status | Timing |
|---------|--------|--------|
| **Live Data Source** | ✅ Active | OpenPhish updates multiple times/day |
| **Cache** | ✅ Active | 1 hour TTL |
| **Manual Refresh** | ✅ Active | Instant on button click |
| **Auto-Refresh** | ⏸️ Disabled | Would update every 5 min |
| **Sample Data Mode** | ✅ Active | For demos/testing |

### **Detailed Answer**:

1. **Live Data (When "Use Sample Data" = OFF)**
   - Fetches from OpenPhish (updated multiple times daily)
   - Cached for 1 hour to avoid excessive API calls
   - Click "Refresh Data" to force new fetch
   - **Freshness**: As recent as OpenPhish's latest update

2. **Sample Data (When "Use Sample Data" = ON)**
   - Uses generated demo data
   - Shows 100 sample phishing URLs
   - Instant updates on refresh
   - **Freshness**: Synthetic data for demonstration

## 🚀 Enabling TRUE Real-Time Updates

Want the dashboard to auto-refresh every 5 minutes? Here's how:

### Option 1: Enable Auto-Refresh in Code

**Edit `app.py` line 245:**

```python
# BEFORE (disabled)
dcc.Interval(
    id='interval-component',
    interval=config.DATA_REFRESH_INTERVAL,
    n_intervals=0,
    disabled=True  # ← Change this
)

# AFTER (enabled)
dcc.Interval(
    id='interval-component',
    interval=config.DATA_REFRESH_INTERVAL,
    n_intervals=0,
    disabled=False  # ← Auto-refresh every 5 minutes
)
```

### Option 2: Reduce Cache Time

**Edit `config.py`:**

```python
# More frequent data updates
CACHE_DURATION = 600  # 10 minutes instead of 1 hour
DATA_REFRESH_INTERVAL = 60000  # 1 minute auto-refresh
```

### Option 3: Add Toggle Button to Dashboard

I can add a "Enable Auto-Refresh" switch to the UI that lets users control this dynamically!

## 📊 Statistics Update Flow

```
User Action (Refresh Button)
         ↓
Check Cache Age
         ↓
    Is cache < 1 hour old?
    ├─ YES → Use cached data
    └─ NO  → Fetch from OpenPhish
         ↓
Process URLs (country, brand, attack type)
         ↓
Update all visualizations:
  • Global Threat Map
  • Brand Treemap
  • Attack Timeline
  • Statistics Cards
         ↓
Display updated timestamp
```

## 🎯 What Updates "Live"

### ✅ Updates Immediately on Refresh:
- Total attack count
- Most targeted brand
- Top source country
- Most common attack type
- All 3 visualizations (map, treemap, timeline)
- Last update timestamp

### ⏱️ Updates Based on:
1. **Data freshness**: OpenPhish feed updates
2. **Cache age**: Whether 1 hour has passed
3. **User action**: Manual refresh clicks
4. **Auto-refresh**: If enabled (currently disabled)

## 🔧 Recommendation for Your Use Case

### For **Demonstration/Training**:
✅ Current setup is perfect
- Manual refresh gives control
- Sample data shows features instantly
- No API rate limit concerns

### For **Live Monitoring**:
🔄 Enable auto-refresh:
1. Set `disabled=False` in `app.py` (line 245)
2. Reduce cache to 10-15 minutes
3. Auto-refresh every 5 minutes
4. Monitors phishing trends continuously

### For **Production SOC Dashboard**:
⚡ Full real-time:
1. Use webhooks from phishing feeds
2. Implement database backend
3. WebSocket connections for instant updates
4. Multiple data source aggregation

## 💡 Quick Modifications

Want to make changes? I can help you:

1. **Enable auto-refresh** - Dashboard updates automatically
2. **Add real-time toggle** - User controls auto-refresh from UI
3. **Reduce cache time** - More frequent fresh data
4. **Add refresh rate indicator** - Show countdown to next update
5. **Implement WebSocket** - True real-time streaming data

## 📋 Current Data Freshness

```
🔄 Refresh Mode: Manual (on-demand)
⏰ Cache Duration: 1 hour
📡 Data Source: OpenPhish (live) or Sample (demo)
🔄 Last Update: Shown in dashboard header
✅ Statistics: Update with every refresh
```

---

## Summary

**Your dashboard shows:**
- ✅ **Live phishing data** (from OpenPhish when sample mode OFF)
- ✅ **Real statistics** (calculated from actual phishing URLs)
- ✅ **Manual refresh** (full control over updates)
- ⏸️ **Auto-refresh disabled** (can be enabled for automatic updates)
- 💾 **1-hour cache** (balances freshness with API limits)

**It's "near real-time"** - you get fresh data on demand, and can enable automatic updates if needed!

Would you like me to enable auto-refresh for you? 🚀

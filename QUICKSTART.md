# Quick Start Guide 🎣

## Start the Dashboard

### Method 1: Using the Launcher Script (Recommended)
```bash
./run_dashboard.sh
```

### Method 2: Using Python Directly
```bash
source .venv/bin/activate  # Activate virtual environment
python app.py
```

### Method 3: First Time Setup
```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run dashboard
python app.py
```

## Access the Dashboard

Once running, open your web browser and go to:
```
http://localhost:8050
```

## Using the Dashboard

### 1. **Sample Data Mode** (Default)
   - Toggle "Use Sample Data" to ON
   - Click "Refresh Data" to load demo data
   - Perfect for testing and demonstrations

### 2. **Live Data Mode**
   - Toggle "Use Sample Data" to OFF
   - Click "Refresh Data" to fetch real phishing data
   - Data comes from OpenPhish (no API key needed)

### 3. **Dashboard Features**

#### Control Panel
- **Refresh Data**: Manual data refresh button
- **Auto-Refresh**: Toggle automatic updates (1/5/15 min intervals)
- **Demo Mode**: Switch between sample and live data
- **Dark Mode**: Toggle professional dark theme

#### Advanced Filters
- **Time Range**: Last 24h, 7 days, 30 days, or all time
- **Attack Type**: Filter by specific attack methods
- **Brand**: Filter by targeted brand
- **Country**: Filter by geographic origin
- All filters update all visualizations in real-time

#### Statistics Cards
- **Total Attacks**: See the count of detected phishing attempts
- **Most Targeted Brand**: Which brand is most impersonated
- **Top Source Country**: Where attacks originate from
- **Most Common Attack**: Primary attack method

#### 7 Interactive Visualizations

**Global Threat Map**
- Interactive world map showing attack distribution
- Hover over countries for details
- Color intensity shows frequency

**Brand Impersonation Treemap**
- Visual breakdown of targeted brands
- Larger boxes = more attacks
- Click to explore details

**Attack Timeline**
- See attack trends over time
- Different colors for different attack types
- Hover for specific counts

**Attack Pattern Heatmap** (NEW!)
- Hour-by-hour and day-by-day patterns
- Identify peak attack times
- Color intensity shows frequency

**Top 10 Targeted Domains** (NEW!)
- Most frequently attacked domains
- Horizontal bar chart
- Prioritize defense efforts

**Attack Type Distribution** (NEW!)
- Donut chart with percentages
- Clear breakdown of attack methods
- Interactive legend

**URL Length Distribution** (NEW!)
- Histogram of phishing URL lengths
- Average length indicator
- Pattern analysis for detection

## Quick Tips

1. **Start with Sample Data** to see the dashboard in action immediately
2. **Try Dark Mode** for comfortable extended viewing
3. **Use Filters** to drill down into specific threat patterns
4. **Enable Auto-Refresh** for live monitoring (SOC environments)
5. **Use Live Data** for real threat intelligence
6. **Combine Filters** for detailed analysis (e.g., "PayPal + Last 7 Days + Russia")
7. **Export Charts** using the Plotly toolbar on each visualization
8. **Explore Interactive Charts** - hover, click, zoom!

## Keyboard Shortcuts

- **Refresh Data**: Click the "Refresh Data" button
- **Stop Server**: Press `Ctrl+C` in terminal

## Common Issues

### Port Already in Use?
```bash
# Find and kill the process
lsof -ti:8050 | xargs kill -9

# Or change the port in config.py
DASHBOARD_PORT = 8051
```

### No Data Showing?
- Make sure you clicked "Refresh Data"
- Check "Use Sample Data" is toggled ON for demo
- Check your internet connection for live data

### Import Errors?
```bash
source .venv/bin/activate
pip install -r requirements.txt --upgrade
```

## Need Help?

Check the main [README.md](README.md) for detailed documentation!

---
**Happy Threat Hunting! 🎣**

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

#### Statistics Cards
- **Total Attacks**: See the count of detected phishing attempts
- **Most Targeted Brand**: Which brand is most impersonated
- **Top Source Country**: Where attacks originate from
- **Most Common Attack**: Primary attack method

#### Global Threat Map
- Interactive world map showing attack distribution
- Hover over countries for details
- Color intensity shows attack frequency

#### Brand Impersonation Treemap
- Visual breakdown of targeted brands
- Larger boxes = more attacks
- Click to explore details

#### Attack Timeline
- See attack trends over time
- Different colors for different attack types
- Hover for specific counts

## Keyboard Shortcuts

- **Refresh Data**: Click the "Refresh Data" button
- **Stop Server**: Press `Ctrl+C` in terminal

## Tips

1. **Start with Sample Data** to see the dashboard in action immediately
2. **Use Live Data** for real threat intelligence
3. **Refresh Periodically** to see updated phishing campaigns
4. **Explore Interactive Charts** - hover, click, zoom!

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

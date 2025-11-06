# 🚀 Phishing Ocean - Installation & Setup Guide

## Quick Start for New Users

Follow these steps to get the Phishing Ocean dashboard running on your machine in under 5 minutes!

---

## 📋 Prerequisites

Before you begin, make sure you have:

- **Python 3.8+** installed (Python 3.13 recommended)
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **Web browser** (Chrome, Firefox, Safari, Edge)
- **Terminal/Command Line** access

### Check Your Python Version:
```bash
python3 --version
# Should show Python 3.8 or higher
```

---

## 🔽 Step 1: Clone the Repository

```bash
# Clone from GitHub
git clone https://github.com/DheerendraAchar/Phishing-ocean.git

# Navigate into the project directory
cd Phishing-ocean
```

---

## 🐍 Step 2: Create Virtual Environment

A virtual environment keeps your dependencies isolated.

### On macOS/Linux:
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

### On Windows:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

**You should see `(.venv)` appear in your terminal prompt!**

---

## 📦 Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

This will install:
- dash (2.14.2)
- plotly (5.18.0)
- pandas (2.1.4)
- dash-bootstrap-components (1.5.0)
- requests (2.31.0)
- tldextract (5.1.1)

**Wait for installation to complete** (usually 1-2 minutes)

---

## ▶️ Step 4: Run the Dashboard

### Option A: Using the Run Script (Recommended)

#### On macOS/Linux:
```bash
# Make script executable (first time only)
chmod +x run_dashboard.sh

# Run the dashboard
./run_dashboard.sh
```

#### On Windows:
```bash
# Run directly with Python
python app.py
```

### Option B: Manual Run
```bash
# Make sure virtual environment is activated
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows

# Run the application
python app.py
```

---

## 🌐 Step 5: Open in Browser

Once the dashboard starts, you'll see:
```
======================================================================
  PHISHING THREAT INTELLIGENCE DASHBOARD
======================================================================
  Status: Starting server...
  URL: http://localhost:8050
  Mode: Development
  Press Ctrl+C to stop
======================================================================

Dash is running on http://0.0.0.0:8050/
```

**Open your web browser** and navigate to:
```
http://localhost:8050
```

**🎉 That's it! The dashboard should now be running!**

---

## ✅ What You Should See

Your browser should display:
- 📊 **4 Statistics Cards** at the top
- 🔧 **Filter Controls** (Time Range, Attack Type, Brand, Country)
- 🌍 **Global Threat Map** showing country-level attacks
- 🏢 **Brand Treemap** with targeted brands
- 📈 **Attack Timeline** showing temporal patterns
- 🔥 **Attack Heatmap** with day/hour patterns
- 🏆 **Top Domains Chart** ranking targeted services
- 🎯 **Attack Type Pie Chart** showing distribution
- 📏 **URL Length Histogram** analyzing URL patterns

---

## 🛑 To Stop the Dashboard

Press **`Ctrl + C`** in your terminal

---

## 🔧 Troubleshooting

### Problem: "Port 8050 is already in use"

**Solution:**
```bash
# Kill the process using port 8050
lsof -ti :8050 | xargs kill -9  # macOS/Linux
# OR
netstat -ano | findstr :8050    # Windows (find PID, then kill it)
```

---

### Problem: "ModuleNotFoundError: No module named 'dash'"

**Solution:**
```bash
# Make sure virtual environment is activated
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

---

### Problem: "python3: command not found"

**Solution:**
```bash
# Try using 'python' instead of 'python3'
python --version

# Or install Python 3 from python.org
```

---

### Problem: Virtual environment won't activate

**Solution on macOS/Linux:**
```bash
# Make sure you're in the project directory
cd Phishing-ocean

# Try with bash
bash .venv/bin/activate
```

**Solution on Windows:**
```bash
# Try this alternative
.venv\Scripts\activate.bat
```

---

### Problem: "No data showing on dashboard"

**Solution:**
```bash
# The dashboard uses Demo Mode by default
# Check the "Demo Mode" toggle in the interface
# If you want live data, uncheck "Demo Mode" and click Refresh
```

---

### Problem: Dependencies installation fails

**Solution:**
```bash
# Upgrade pip first
pip install --upgrade pip

# Try installing dependencies again
pip install -r requirements.txt

# If specific package fails, install one by one:
pip install dash==2.14.2
pip install plotly==5.18.0
pip install pandas==2.1.4
# ... etc
```

---

## 🎨 Dashboard Features

Once running, you can:

### 1. **Apply Filters**
- Select **Time Range** (24h, 7d, 30d, All Time)
- Choose **Attack Type** (Fake Login, Verification, etc.)
- Filter by **Brand** (PayPal, Microsoft, Google, etc.)
- Select **Country** (United States, Russia, etc.)

### 2. **Toggle Dark Mode**
- Click the **Dark Mode** switch for a sleek dark theme
- Perfect for presentations or late-night monitoring

### 3. **Enable Auto-Refresh**
- Turn on **Auto-Refresh** toggle
- Select interval: 1, 5, or 15 minutes
- Dashboard updates automatically

### 4. **Refresh Data**
- Click the **🔄 Refresh Data** button
- Fetches latest phishing data
- Updates all visualizations

### 5. **Use Demo Mode**
- Toggle **Demo Mode** on/off
- Demo mode: Uses 100 sample URLs (no internet needed)
- Live mode: Fetches from OpenPhish API (requires internet)

---

## 📁 Project Structure

```
Phishing-ocean/
├── app.py                      # Main dashboard application
├── visualizations.py           # 7 chart creation functions
├── data_fetcher.py            # Fetches phishing URLs
├── data_processor.py          # Processes and analyzes data
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies
├── run_dashboard.sh           # Launch script (macOS/Linux)
├── README.md                  # Project overview
├── QUICKSTART.md              # This file
├── FILE_DESCRIPTIONS.md       # Detailed file documentation
├── VISUALIZATIONS_GUIDE.md    # Chart explanations
├── PRESENTATION_CONTENT.md    # Presentation slides content
└── .venv/                     # Virtual environment (created by you)
```

---

## 🔄 Updating the Project

To get the latest updates:

```bash
# Navigate to project directory
cd Phishing-ocean

# Pull latest changes
git pull origin main

# Update dependencies (if requirements.txt changed)
pip install -r requirements.txt --upgrade

# Run the dashboard
./run_dashboard.sh
```

---

## 🐳 Docker Setup (Alternative - Coming Soon)

For Docker users, we're working on containerization:

```bash
# Build image
docker build -t phishing-ocean .

# Run container
docker run -p 8050:8050 phishing-ocean
```

*Note: Docker support is planned for future release*

---

## 🌐 Deployment Options

### Local Development (Current)
- Run on localhost
- Access from your machine only

### Network Access
- Dashboard binds to `0.0.0.0:8050`
- Accessible from other devices on your network
- Find your IP: `ifconfig` (Mac/Linux) or `ipconfig` (Windows)
- Access from other devices: `http://YOUR_IP:8050`

### Cloud Deployment (Future)
- Heroku
- AWS EC2
- Google Cloud Run
- Azure App Service
- DigitalOcean

*Deployment guides coming soon!*

---

## 📚 Additional Resources

### Documentation
- **README.md** - Project overview and features
- **FILE_DESCRIPTIONS.md** - Detailed code documentation
- **VISUALIZATIONS_GUIDE.md** - How to interpret charts
- **PRESENTATION_CONTENT.md** - Presentation materials

### Learning Resources
- [Dash Documentation](https://dash.plotly.com/)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/)

### Support
- **GitHub Issues**: Report bugs or request features
- **Repository**: https://github.com/DheerendraAchar/Phishing-ocean
- **Email**: [Your email for support]

---

## 🤝 Contributing

Want to contribute? Great!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit (`git commit -m 'Add some AmazingFeature'`)
5. Push to branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

---

## 📝 Common Commands Reference

### Virtual Environment
```bash
# Create
python3 -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Deactivate
deactivate
```

### Running
```bash
# Quick run
./run_dashboard.sh

# Manual run
python app.py

# With virtual env
.venv/bin/python app.py
```

### Dependencies
```bash
# Install all
pip install -r requirements.txt

# Install single package
pip install dash

# Update all
pip install -r requirements.txt --upgrade

# List installed
pip list
```

### Git Commands
```bash
# Clone
git clone https://github.com/DheerendraAchar/Phishing-ocean.git

# Update
git pull origin main

# Check status
git status

# View commits
git log
```

---

## ⚡ Performance Tips

### For Faster Loading:
1. Use **Demo Mode** for offline testing
2. Set **Auto-Refresh** to 15 minutes (not 1 minute)
3. Apply **filters** to reduce data volume
4. Close other browser tabs

### For Production:
1. Set `debug=False` in `app.py`
2. Use production WSGI server (gunicorn)
3. Enable caching
4. Use database for data storage

---

## 🔒 Security Notes

### For Local Use:
- Dashboard runs on localhost by default
- Safe for personal use and development

### For Public Deployment:
- Add authentication (not included)
- Use HTTPS (SSL certificates)
- Implement rate limiting
- Sanitize user inputs
- Use environment variables for secrets

---

## 🎯 Next Steps

Now that you have the dashboard running:

1. **Explore the Features**
   - Try different filters
   - Toggle dark mode
   - Enable auto-refresh

2. **Read the Documentation**
   - VISUALIZATIONS_GUIDE.md - Understand the charts
   - FILE_DESCRIPTIONS.md - Learn the code structure

3. **Customize It**
   - Edit `config.py` to add brands
   - Modify `visualizations.py` for custom charts
   - Update `app.py` for new features

4. **Share Feedback**
   - Star the repository ⭐
   - Report issues 🐛
   - Suggest features 💡

---

## ✨ Success Checklist

- [ ] Python 3.8+ installed
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] Dashboard started successfully
- [ ] Browser shows dashboard at localhost:8050
- [ ] All 7 visualizations are visible
- [ ] Filters are working
- [ ] Dark mode toggles correctly

**If all checked, you're ready to go! 🎉**

---

## 📞 Need Help?

If you run into issues:

1. Check the **Troubleshooting** section above
2. Read the error message carefully
3. Search GitHub Issues
4. Create a new issue with:
   - Your OS (Windows/Mac/Linux)
   - Python version
   - Error message
   - Steps to reproduce

---

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Threat Hunting! 🎣🌊**

Last Updated: November 6, 2025
Version: 1.0

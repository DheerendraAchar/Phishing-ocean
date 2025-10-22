# Phishing Ocean 🎣 - Global Threat Dashboard

A real-time interactive dashboard that visualizes global phishing attacks, tracking origins, targets, and attack types from verified phishing data sources.

![Dashboard Preview](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- **🌍 Global Threat Map**: Interactive choropleth map showing phishing attack origins by country
- **🎯 Brand Impersonation Treemap**: Visual breakdown of most commonly targeted brands
- **📊 Attack Timeline**: Time-series visualization of attack types and frequency
- **📈 Real-time Statistics**: Live stats showing total attacks, top brands, countries, and attack types
- **🔄 Auto-refresh**: Configurable data refresh intervals
- **💾 Smart Caching**: Efficient data caching to minimize API calls

## 🎬 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd /Users/admin/Documents/davproject
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Dashboard

**Quick Start with Sample Data**:
```bash
python app.py
```

The dashboard will start on `http://localhost:8050`. Open this URL in your web browser.

## 📊 Data Sources

### OpenPhish (Default)
- **URL**: https://openphish.com/feed.txt
- **API Key**: Not required for basic feed
- **Update Frequency**: Multiple times per day
- **Data**: List of verified phishing URLs

### PhishTank (Optional)
- **URL**: http://data.phishtank.com/
- **API Key**: Optional (increases rate limits)
- **Sign up**: https://www.phishtank.com/api_info.php
- **Data**: Rich metadata including submission time, verification status, target brands

### Using Live Data

1. **For OpenPhish** (no setup needed):
   - Toggle off "Use Sample Data" in the dashboard
   - Click "Refresh Data"

2. **For PhishTank** (optional):
   - Get an API key from https://www.phishtank.com/api_info.php
   - Set environment variable:
     ```bash
     export PHISHTANK_API_KEY="your_api_key_here"
     ```
   - Uncomment PhishTank fetching code in `data_fetcher.py` (lines 76-77)

## 🏗️ Project Structure

```
davproject/
├── app.py                  # Main dashboard application
├── config.py              # Configuration settings
├── data_fetcher.py        # Data fetching from phishing sources
├── data_processor.py      # Data processing and analysis
├── visualizations.py      # Plotly visualization components
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── cache/                # Data cache directory (auto-created)
```

## 🎨 Dashboard Components

### 1. Header Section
- Dashboard title and description
- Last update timestamp
- Refresh button for manual data updates
- Sample data toggle switch

### 2. Statistics Cards
- **Total Attacks**: Count of all detected phishing attempts
- **Most Targeted Brand**: Brand with highest impersonation count
- **Top Source Country**: Country with most phishing origins
- **Most Common Attack**: Predominant attack type

### 3. Global Threat Map
- Interactive world map showing attack distribution
- Color-coded by attack frequency
- Hover for country-specific details
- Based on domain TLD analysis

### 4. Brand Impersonation Treemap
- Hierarchical visualization of targeted brands
- Size represents attack frequency
- Includes: PayPal, Microsoft, Google, Apple, Amazon, banks, and more
- Interactive hover for detailed counts

### 5. Attack Timeline
- Time-series chart of attacks over time
- Segmented by attack type:
  - Fake Login Pages
  - Malicious Links
  - Survey/Prize Scams
  - Invoice/Payment Fraud
  - Package Delivery Scams
  - Password Reset Phishing

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Cache duration (seconds)
CACHE_DURATION = 3600  # 1 hour

# Dashboard auto-refresh (milliseconds)
DATA_REFRESH_INTERVAL = 300000  # 5 minutes

# Data processing limit
MAX_URLS_TO_PROCESS = 1000

# Dashboard port
DASHBOARD_PORT = 8050
```

## 🔧 Advanced Usage

### Running in Production

Use Gunicorn for production deployment:

```bash
gunicorn app:server -b 0.0.0.0:8050 --workers 4
```

### Custom Brand Detection

Add custom brands to detect in `config.py`:

```python
BRAND_KEYWORDS = {
    'YourBrand': ['yourbrand', 'your-brand'],
    # ... existing brands
}
```

### Custom Attack Type Patterns

Define new attack patterns in `config.py`:

```python
ATTACK_TYPE_PATTERNS = {
    'Your Attack Type': ['keyword1', 'keyword2'],
    # ... existing patterns
}
```

## 🛠️ Development

### Testing Individual Components

**Test Data Fetcher**:
```bash
python data_fetcher.py
```

**Test Data Processor**:
```bash
python data_processor.py
```

**Test Visualizations**:
```bash
python visualizations.py
```

### Clearing Cache

```bash
rm -rf cache/
```

## 📈 Understanding the Data

### Country Detection
- Based on domain TLD (Top-Level Domain)
- Examples: `.ru` → Russia, `.cn` → China, `.uk` → United Kingdom
- Generic TLDs (`.com`, `.net`) marked as "Unknown"

### Brand Detection
- Pattern matching in URL strings
- Checks domain, subdomain, and path
- Case-insensitive matching

### Attack Type Classification
- Keyword-based pattern matching
- Multiple patterns per attack type
- Prioritizes specific matches over generic

## 🐛 Troubleshooting

### Issue: "No Data Available"
**Solution**: 
- Check internet connection
- Verify OpenPhish feed is accessible
- Try using sample data mode
- Check cache directory permissions

### Issue: Import Errors
**Solution**: 
```bash
pip install -r requirements.txt --upgrade
```

### Issue: Port Already in Use
**Solution**: 
Change port in `config.py` or kill existing process:
```bash
lsof -ti:8050 | xargs kill -9
```

### Issue: Slow Performance
**Solution**: 
- Reduce `MAX_URLS_TO_PROCESS` in `config.py`
- Increase `CACHE_DURATION`
- Use sample data mode for testing

## 📚 Dependencies

- **Dash**: Web application framework
- **Plotly**: Interactive visualization library
- **Pandas**: Data manipulation and analysis
- **Requests**: HTTP library for API calls
- **tldextract**: Domain parsing and TLD extraction
- **dash-bootstrap-components**: Bootstrap styling for Dash

## 🔐 Security Notes

- This tool is for educational and awareness purposes
- Do NOT visit phishing URLs directly
- The data is sourced from verified phishing databases
- Always exercise caution with suspicious URLs

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional data sources (URLhaus, AlienVault OTX)
- Machine learning for attack classification
- IP geolocation for more accurate country detection
- Export functionality (PDF reports, CSV data)
- Historical data tracking and trends
- Email alert system for specific brands/countries

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **OpenPhish**: For providing free phishing feed data
- **PhishTank**: For community-driven phishing database
- **Plotly**: For excellent visualization tools
- **Dash**: For the powerful dashboard framework

## 📧 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Review existing documentation
- Check troubleshooting section

---

**Built with ❤️ for Cybersecurity Awareness**

*Remember: Stay vigilant, verify everything, and never click suspicious links!* 🛡️

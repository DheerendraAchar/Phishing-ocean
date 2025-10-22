# Project Files

## Core Application Files
- `app.py` - Main dashboard application (Dash web app)
- `config.py` - Configuration settings
- `data_fetcher.py` - Fetches phishing data from APIs
- `data_processor.py` - Processes and analyzes phishing URLs
- `visualizations.py` - Creates Plotly visualizations

## Documentation
- `README.md` - Complete project documentation
- `QUICKSTART.md` - Quick start guide
- `requirements.txt` - Python dependencies

## Utility Scripts
- `run_dashboard.sh` - Bash launcher script
- `test_data.py` - Test script for data pipeline

## Directory Structure
```
davproject/
├── app.py                      # Main Dash application
├── config.py                   # Configuration settings
├── data_fetcher.py             # Data fetching module
├── data_processor.py           # Data processing module
├── visualizations.py           # Visualization components
├── requirements.txt            # Dependencies
├── README.md                   # Full documentation
├── QUICKSTART.md              # Quick start guide
├── run_dashboard.sh           # Launcher script
├── test_data.py               # Test script
├── .gitignore                 # Git ignore rules
├── .venv/                     # Virtual environment
└── cache/                     # Data cache directory
```

## Key Features by File

### app.py (~800 lines)
- Dashboard layout with 7 visualizations
- 11 callback functions for real-time interactivity
- Advanced filtering system (time, attack type, brand, country)
- Auto-refresh control logic
- Dark mode toggle with client-side callback
- Data refresh logic
- Statistics card updates
- All visualization updates with filter support

### config.py
- API endpoints (OpenPhish, PhishTank)
- Cache settings (1 hour TTL)
- Auto-refresh intervals
- Brand keywords (15+ brands)
- Attack type patterns (6+ types)
- Dashboard configuration (port, host, title)
- Dashboard settings

### data_fetcher.py
- OpenPhish feed fetching
- PhishTank integration
- Caching mechanism
- Sample data generation

### data_processor.py
- URL parsing and analysis
- Brand detection
- Attack type classification
- Country detection from TLD
- Statistics generation

### visualizations.py (~450 lines)
- **7 Visualization Methods:**
  1. `create_global_threat_map()` - Choropleth world map
  2. `create_brand_treemap()` - Brand impersonation treemap
  3. `create_attack_timeline()` - Time-series attack chart
  4. `create_attack_heatmap()` - Hour/day attack pattern heatmap
  5. `create_top_domains_chart()` - Top 10 domains bar chart
  6. `create_attack_pie_chart()` - Attack type donut chart
  7. `create_url_length_distribution()` - URL length histogram
- `create_stats_cards()` - Statistics calculation for dashboard cards

## Running the Project

1. **Quick Start**: `./run_dashboard.sh`
2. **Manual**: `source .venv/bin/activate && python app.py`
3. **Test**: `python test_data.py`

## Data Flow

```
OpenPhish/PhishTank
        ↓
data_fetcher.py (fetch & cache)
        ↓
data_processor.py (analyze & classify)
        ↓
visualizations.py (create charts)
        ↓
app.py (display dashboard)
```

## Customization Points

1. **Add new brands**: Edit `BRAND_KEYWORDS` in `config.py`
2. **Add attack types**: Edit `ATTACK_TYPE_PATTERNS` in `config.py`
3. **Change refresh rate**: Edit `DATA_REFRESH_INTERVAL` in `config.py`
4. **Modify visualizations**: Edit functions in `visualizations.py`
5. **Add data sources**: Extend `data_fetcher.py`

## Technologies Used

- **Dash**: Web application framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation
- **Requests**: HTTP requests
- **tldextract**: Domain parsing
- **Bootstrap**: UI styling

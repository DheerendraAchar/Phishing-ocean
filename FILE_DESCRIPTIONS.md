# Phishing Ocean - File Descriptions

## 📁 Complete Project File Structure

This document provides detailed descriptions of every file in the Phishing Ocean cybersecurity dashboard project.

---

## 🐍 Core Python Files

### **app.py** (Main Application - ~800 lines)
**Purpose**: The main Dash application that orchestrates the entire dashboard.

**Key Components**:
- Initializes Dash app with Bootstrap theme
- Defines the complete UI layout with 7 visualization containers
- Implements 11+ callbacks for interactivity:
  - Data refresh and auto-update
  - Filter synchronization (time range, attack type, brand, country)
  - Chart updates based on filter selections
  - Dark mode toggle
  - Statistics updates
- Handles datetime serialization for JSON storage
- Manages global app state and data caching

**Technologies**: Dash, Flask, Plotly, dash-bootstrap-components

---

### **visualizations.py** (~500 lines)
**Purpose**: Creates all interactive Plotly visualizations.

**7 Visualization Functions**:
1. **create_global_threat_map()** - Choropleth map showing phishing attack distribution by country
2. **create_brand_treemap()** - Hierarchical treemap of brand impersonation patterns
3. **create_attack_timeline()** - Line chart showing attack frequency over time
4. **create_attack_heatmap()** - Heatmap showing attack patterns by day and hour
5. **create_top_domains_chart()** - Bar chart of most targeted domains
6. **create_attack_pie_chart()** - Pie chart of attack type distribution
7. **create_url_length_distribution()** - Histogram of malicious URL lengths

**Features**: 
- Color schemes for light/dark modes
- Responsive layouts
- Interactive hover tooltips
- Professional styling

---

### **data_fetcher.py** (~230 lines)
**Purpose**: Fetches phishing data from OpenPhish API and generates sample data.

**Key Functions**:
- `fetch_openphish()` - Fetches live phishing URLs from OpenPhish.com
- `get_sample_data()` - Generates 100 realistic demo URLs for testing
- Creates timestamps for temporal analysis

**Data Generation**:
- Distributes 100 sample URLs across realistic attack patterns:
  - PayPal (27%), Microsoft (18%), Google (15%), Facebook (12%)
  - Banking (10%), Amazon (8%), Apple (7%), Netflix (5%)
  - Crypto (5%), Other services (varies)
- Generates timestamps spread over 48 hours for time-based filtering
- Includes verification and submission times in ISO format

---

### **data_processor.py** (~227 lines)
**Purpose**: Processes raw phishing URLs and extracts threat intelligence.

**Key Features**:
- **Brand Detection**: Identifies impersonated brands (15+ brands tracked)
- **Attack Type Classification**: Categorizes attacks into 7 types:
  - Fake Login Pages
  - Account Verification Scams
  - Prize/Lottery Scams
  - Invoice/Payment Fraud
  - Package Delivery Scams
  - Security Alert Phishing
  - Other
- **Geolocation**: Maps domains to countries (50+ countries)
- **Domain Analysis**: Extracts domain, subdomain, TLD information
- **Timestamp Parsing**: Handles multiple timestamp formats

**Methods**:
- `process_entry()` - Processes a single phishing URL
- `process_all()` - Batch processes multiple URLs
- `get_statistics()` - Generates summary statistics
- `detect_brand()` - Pattern matching for brand detection
- `detect_attack_type()` - Classifies attack vectors
- `get_country_from_url()` - Country attribution

---

### **config.py** (~100 lines)
**Purpose**: Centralized configuration and constants.

**Contains**:
- **BRAND_KEYWORDS**: Dictionary mapping 15+ brands to detection keywords
  - PayPal, Microsoft, Google, Facebook, Amazon, Apple, Netflix, etc.
- **ATTACK_TYPE_PATTERNS**: Keywords for identifying 7 attack types
- **CACHE_DURATION**: Data refresh interval (3600 seconds)
- **API_ENDPOINTS**: OpenPhish API URL
- **UI_SETTINGS**: Color schemes, font sizes, spacing values

**Purpose**: Makes the application easily configurable without touching core code.

---

## 🚀 Utility Scripts

### **run_dashboard.sh**
**Purpose**: Shell script to start the dashboard safely.

**Features**:
- Checks if port 8050 is already in use
- Stops existing instances automatically
- Activates Python virtual environment
- Starts the Dash server
- Provides user-friendly status messages

**Usage**: `./run_dashboard.sh`

---

### **requirements.txt**
**Purpose**: Python package dependencies for the project.

**Key Packages**:
```
dash==2.14.2              # Web framework
plotly==5.18.0            # Interactive visualizations
pandas==2.1.4             # Data manipulation
dash-bootstrap-components==1.5.0  # UI components
tldextract==5.1.1         # Domain parsing
requests==2.31.0          # HTTP requests
```

**Usage**: `pip install -r requirements.txt`

---

## 📚 Documentation Files

### **README.md** (~150 lines)
**Purpose**: Main project documentation and getting started guide.

**Sections**:
- Project overview and features
- Screenshots preview
- Installation instructions
- Usage guide
- Technology stack
- Project structure overview
- Contributing guidelines
- License information

**Audience**: Developers, users, contributors

---

### **PROJECT_SUMMARY.md** (~100 lines)
**Purpose**: Executive summary of the project.

**Contains**:
- High-level project description
- Key features and capabilities
- Use cases and applications
- Technical highlights
- Success metrics
- Future roadmap

**Audience**: Stakeholders, managers, recruiters

---

### **PROJECT_STRUCTURE.md** (~80 lines)
**Purpose**: Detailed breakdown of the codebase architecture.

**Contains**:
- File organization explanation
- Module responsibilities
- Data flow diagrams
- Component relationships
- Design patterns used

**Audience**: Developers joining the project

---

### **QUICKSTART.md** (~50 lines)
**Purpose**: Fast setup guide for impatient users.

**Contains**:
- 5-step quick setup process
- Common troubleshooting tips
- Quick command reference
- Essential links

**Audience**: New users wanting immediate results

---

### **ENHANCEMENT_IDEAS.md** (~120 lines)
**Purpose**: Future feature ideas and improvement suggestions.

**Categories**:
- Machine learning integrations
- Real-time monitoring features
- API development
- Historical data tracking
- Advanced analytics
- Security enhancements
- Performance optimizations

**Audience**: Contributors, developers planning roadmap

---

### **UI_FIXES.md** (~228 lines)
**Purpose**: Documentation of recent UI/UX improvements.

**Sections**:
- Issues that were fixed
- Technical solutions implemented
- Before/after comparisons
- Code changes made
- Testing checklist

**Audience**: Developers, QA testers

---

### **FILE_DESCRIPTIONS.md** (This file!)
**Purpose**: Complete reference guide for all project files.

---

## 📄 Configuration Files

### **.gitignore**
**Purpose**: Specifies files Git should ignore.

**Excludes**:
```
__pycache__/              # Python cache files
*.pyc                     # Compiled Python files
.venv/                    # Virtual environment
.env                      # Environment variables
*.log                     # Log files
.DS_Store                 # macOS system files
```

**Why**: Keeps repository clean and secure

---

### **LICENSE**
**Purpose**: Legal license for the project.

**Type**: MIT License (typically)
**Grants**: 
- Free use
- Modification rights
- Distribution rights
- Commercial use

---

## 📁 Directory: `.venv/` (Virtual Environment)
**Purpose**: Isolated Python environment for the project.

**Contains**:
- Python interpreter
- Installed packages (dash, plotly, pandas, etc.)
- Package executables
- Library dependencies

**Created By**: `python -m venv .venv`
**Why**: Prevents package conflicts with system Python

---

## 📁 Directory: `__pycache__/`
**Purpose**: Python bytecode cache for faster imports.

**Contains**:
- `.pyc` files (compiled Python bytecode)
- Auto-generated by Python interpreter

**Note**: Automatically created, should be in .gitignore

---

## 📊 Data Flow Summary

```
┌─────────────────┐
│ data_fetcher.py │ ← Fetches phishing URLs
└────────┬────────┘
         ↓
┌─────────────────┐
│data_processor.py│ ← Processes & analyzes URLs
└────────┬────────┘
         ↓
┌─────────────────┐
│    app.py       │ ← Main application logic
└────────┬────────┘
         ↓
┌─────────────────┐
│visualizations.py│ ← Creates charts/graphs
└────────┬────────┘
         ↓
┌─────────────────┐
│  Web Browser    │ ← User interface
└─────────────────┘
```

---

## 🎯 File Count by Type

| Type | Count | Purpose |
|------|-------|---------|
| Python Code | 5 files | Core functionality |
| Documentation | 7 files | User guides & references |
| Configuration | 3 files | Setup & dependencies |
| Scripts | 1 file | Automation |
| **Total** | **16 files** | **Complete project** |

---

## 🔧 How Files Work Together

### **Startup Sequence**:
1. User runs `./run_dashboard.sh` or `python app.py`
2. `app.py` imports `config.py`, `data_fetcher.py`, `data_processor.py`, `visualizations.py`
3. `data_fetcher.py` retrieves phishing URLs
4. `data_processor.py` analyzes URLs and extracts intelligence
5. `app.py` stores processed data and builds UI layout
6. User interacts with filters
7. `app.py` callbacks trigger
8. `visualizations.py` creates updated charts
9. Browser displays new visualizations

### **Filter Flow**:
```
User selects filter → app.py callback → filter_data_by_criteria() 
→ visualizations.py → Updated chart → Browser update
```

### **Dark Mode Flow**:
```
User toggles switch → app.py callback → Updates stored theme 
→ All visualization callbacks re-run → Charts update colors
```

---

## 📝 File Maintenance Guide

### **Files to Edit When**:

**Adding New Features**:
- `app.py` - Add callbacks and UI elements
- `visualizations.py` - Create new chart functions
- `config.py` - Add configuration constants

**Changing Data Sources**:
- `data_fetcher.py` - Modify fetch logic
- `config.py` - Update API endpoints

**Modifying Analytics**:
- `data_processor.py` - Update detection patterns
- `config.py` - Adjust keywords/patterns

**Improving UI**:
- `app.py` - Update layout components
- `visualizations.py` - Adjust chart styling

**Documentation Updates**:
- `README.md` - User-facing changes
- `PROJECT_SUMMARY.md` - Feature additions
- `ENHANCEMENT_IDEAS.md` - Future plans

---

## 🎓 Learning Path for New Developers

1. **Start Here**: `README.md` → Understand the project
2. **Quick Test**: `run_dashboard.sh` → See it in action
3. **Architecture**: `PROJECT_STRUCTURE.md` → Understand design
4. **Data Flow**: `data_fetcher.py` → See how data enters
5. **Processing**: `data_processor.py` → Understand analysis
6. **Visualization**: `visualizations.py` → Learn chart creation
7. **Integration**: `app.py` → See how it all connects
8. **Configuration**: `config.py` → Understand settings

---

## 🔒 Security Considerations

### **Files Containing Sensitive Info** (None currently):
- No API keys stored in code
- No passwords or credentials
- No user data storage

### **Safe to Share**:
- All files in the repository
- All documentation
- All source code (MIT License)

### **Best Practices Followed**:
- ✅ No hardcoded secrets
- ✅ Environment variables supported
- ✅ .gitignore properly configured
- ✅ Dependencies pinned to specific versions
- ✅ Input validation in data processing

---

## 📈 Lines of Code Breakdown

| File | Lines | Percentage |
|------|-------|------------|
| app.py | ~800 | 36% |
| visualizations.py | ~500 | 23% |
| data_processor.py | ~227 | 10% |
| data_fetcher.py | ~230 | 10% |
| config.py | ~100 | 5% |
| Documentation | ~650 | 16% |
| **Total** | **~2,200** | **100%** |

---

## 🎨 Technology Stack Summary

**Frontend**:
- Dash (React-based)
- Plotly.js
- Bootstrap 5
- Font Awesome icons

**Backend**:
- Python 3.13+
- Flask (via Dash)
- Pandas for data manipulation

**External APIs**:
- OpenPhish.com (phishing URL feed)

**Development Tools**:
- Git for version control
- pip for package management
- Virtual environment for isolation

---

## 📞 File-Based Support

**If You See Errors In**:

- `app.py` → Check Flask/Dash installation
- `visualizations.py` → Check Plotly installation
- `data_fetcher.py` → Check internet connection
- `data_processor.py` → Check input data format
- `config.py` → Check syntax for dictionaries

**Common File Issues**:
- ImportError → Missing package in `requirements.txt`
- SyntaxError → Python version < 3.8
- PermissionError → Check file permissions on scripts
- ModuleNotFoundError → Run from correct directory

---

## ✅ File Checklist for Deployment

- [x] All Python files have proper imports
- [x] requirements.txt is up to date
- [x] README.md contains accurate instructions
- [x] .gitignore excludes sensitive files
- [x] run_dashboard.sh has execute permissions
- [x] All documentation is current
- [x] No hardcoded paths or credentials
- [x] Virtual environment is configured

---

## 🎯 Quick File Reference

**Need to**... **Edit this file**:
- Change colors → `visualizations.py`
- Add filter → `app.py` (UI + callback)
- Add brand → `config.py` (BRAND_KEYWORDS)
- Modify data source → `data_fetcher.py`
- Update detection → `data_processor.py`
- Add dependency → `requirements.txt`
- Update docs → `README.md` or relevant .md file

---

**Last Updated**: October 23, 2025  
**Project**: Phishing Ocean Dashboard  
**Repository**: https://github.com/DheerendraAchar/Phishing-ocean

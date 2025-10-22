#!/bin/bash
# Complete setup script for Phishing Ocean Dashboard

echo "🎣 Phishing Ocean Dashboard - Complete Setup"
echo "=============================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✓ Python version: $PYTHON_VERSION"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source .venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Create cache directory
if [ ! -d "cache" ]; then
    mkdir cache
    echo "✓ Cache directory created"
fi

# Make scripts executable
chmod +x run_dashboard.sh
echo "✓ Scripts made executable"
echo ""

# Test installation
echo "🧪 Testing installation..."
python -c "import dash, plotly, pandas, requests, tldextract, dash_bootstrap_components" 2>&1
if [ $? -eq 0 ]; then
    echo "✓ All dependencies verified"
else
    echo "❌ Some dependencies failed to import"
    exit 1
fi
echo ""

echo "=============================================="
echo "✅ Setup complete!"
echo "=============================================="
echo ""
echo "To start the dashboard:"
echo "  ./run_dashboard.sh"
echo ""
echo "Or manually:"
echo "  source .venv/bin/activate"
echo "  python app.py"
echo ""
echo "Then open: http://localhost:8050"
echo ""

#!/bin/bash
# Launcher script for Phishing Threat Intelligence Dashboard

echo "=============================================="
echo "  Phishing Threat Intelligence Dashboard"
echo "=============================================="
echo ""

# Activate virtual environment
if [ -d ".venv" ]; then
    echo "[INFO] Activating virtual environment..."
    source .venv/bin/activate
else
    echo "[WARN] Virtual environment not found. Creating one..."
    python3 -m venv .venv
    source .venv/bin/activate
    echo "[INFO] Installing dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "[INFO] Starting dashboard server..."
echo "[INFO] Dashboard URL: http://localhost:8050"
echo "[INFO] Press Ctrl+C to stop the server"
echo ""

# Run the dashboard
python app.py

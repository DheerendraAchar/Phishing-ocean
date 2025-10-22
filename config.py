"""
Configuration settings for the Phishing Ocean Dashboard
"""
import os

# API Configuration
PHISHTANK_API_KEY = os.environ.get('PHISHTANK_API_KEY', '')  # Optional, get from phishtank.com
OPENPHISH_URL = "https://openphish.com/feed.txt"
PHISHTANK_URL = "http://data.phishtank.com/data/online-valid.json"

# Cache settings
CACHE_DURATION = 3600  # 1 hour in seconds
DATA_REFRESH_INTERVAL = 300000  # 5 minutes in milliseconds for dashboard auto-refresh

# Dashboard settings
DASHBOARD_TITLE = "Phishing Threat Intelligence Dashboard"
DASHBOARD_PORT = 8050
DASHBOARD_HOST = "0.0.0.0"

# Data limits
MAX_URLS_TO_PROCESS = 1000  # Limit for performance

# Brand keywords to detect (can be expanded)
BRAND_KEYWORDS = {
    'PayPal': ['paypal'],
    'Microsoft': ['microsoft', 'office365', 'outlook', 'onedrive', 'azure'],
    'Google': ['google', 'gmail', 'drive', 'docs'],
    'Apple': ['apple', 'icloud', 'itunes', 'appleid'],
    'Amazon': ['amazon', 'aws'],
    'Facebook': ['facebook', 'meta', 'fb'],
    'Instagram': ['instagram', 'insta'],
    'LinkedIn': ['linkedin'],
    'Netflix': ['netflix'],
    'WhatsApp': ['whatsapp', 'whats-app'],
    'DHL': ['dhl'],
    'FedEx': ['fedex'],
    'Bank': ['bank', 'banking', 'chase', 'wellsfargo', 'bofa'],
    'Crypto': ['crypto', 'blockchain', 'bitcoin', 'binance', 'coinbase'],
    'Adobe': ['adobe'],
    'Other': []  # catch-all
}

# Attack type patterns
ATTACK_TYPE_PATTERNS = {
    'Fake Login Page': ['login', 'signin', 'account', 'verify', 'secure'],
    'Malicious Link': ['click', 'download', 'install', 'update'],
    'Survey/Prize Scam': ['prize', 'winner', 'survey', 'gift', 'free'],
    'Invoice/Payment': ['invoice', 'payment', 'billing', 'receipt'],
    'Package Delivery': ['delivery', 'package', 'shipping', 'track'],
    'Password Reset': ['password', 'reset', 'recover'],
    'Other': []
}

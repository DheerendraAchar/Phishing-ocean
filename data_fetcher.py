"""
Data fetcher module for retrieving phishing data from OpenPhish and PhishTank
"""
import requests
import json
import time
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import config


class PhishingDataFetcher:
    """Fetches phishing data from multiple sources"""
    
    def __init__(self, cache_dir: str = "cache"):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self.cache_file = os.path.join(cache_dir, "phishing_data.json")
        
    def _is_cache_valid(self) -> bool:
        """Check if cached data is still valid"""
        if not os.path.exists(self.cache_file):
            return False
        
        cache_age = time.time() - os.path.getmtime(self.cache_file)
        return cache_age < config.CACHE_DURATION
    
    def _load_cache(self) -> Optional[List[Dict]]:
        """Load data from cache"""
        try:
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading cache: {e}")
            return None
    
    def _save_cache(self, data: List[Dict]):
        """Save data to cache"""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error saving cache: {e}")
    
    def fetch_openphish(self) -> List[Dict]:
        """Fetch data from OpenPhish feed"""
        print("Fetching data from OpenPhish...")
        try:
            response = requests.get(config.OPENPHISH_URL, timeout=30)
            response.raise_for_status()
            
            urls = response.text.strip().split('\n')
            data = []
            
            # Limit to avoid overload
            for url in urls[:config.MAX_URLS_TO_PROCESS]:
                if url.strip():
                    data.append({
                        'url': url.strip(),
                        'source': 'openphish',
                        'verified': 'yes',
                        'verification_time': datetime.now().isoformat(),
                        'submission_time': datetime.now().isoformat()
                    })
            
            print(f"Fetched {len(data)} URLs from OpenPhish")
            return data
            
        except Exception as e:
            print(f"Error fetching OpenPhish data: {e}")
            return []
    
    def fetch_phishtank(self) -> List[Dict]:
        """Fetch data from PhishTank (requires API key for higher limits)"""
        print("Fetching data from PhishTank...")
        try:
            headers = {}
            if config.PHISHTANK_API_KEY:
                headers['User-Agent'] = f'phishtank/{config.PHISHTANK_API_KEY}'
            
            response = requests.get(config.PHISHTANK_URL, headers=headers, timeout=60)
            response.raise_for_status()
            
            raw_data = response.json()
            data = []
            
            # PhishTank returns list of dicts with rich metadata
            for entry in raw_data[:config.MAX_URLS_TO_PROCESS]:
                data.append({
                    'url': entry.get('url', ''),
                    'phish_id': entry.get('phish_id', ''),
                    'source': 'phishtank',
                    'verified': entry.get('verified', 'no'),
                    'verification_time': entry.get('verification_time', ''),
                    'submission_time': entry.get('submission_time', ''),
                    'target': entry.get('target', ''),
                    'phish_detail_url': entry.get('phish_detail_url', '')
                })
            
            print(f"Fetched {len(data)} URLs from PhishTank")
            return data
            
        except Exception as e:
            print(f"Error fetching PhishTank data: {e}")
            return []
    
    def fetch_all(self, force_refresh: bool = False) -> List[Dict]:
        """Fetch data from all sources, using cache if available"""
        if not force_refresh and self._is_cache_valid():
            print("Using cached data...")
            cached = self._load_cache()
            if cached:
                return cached
        
        print("Fetching fresh data...")
        all_data = []
        
        # Try OpenPhish first (no API key needed)
        openphish_data = self.fetch_openphish()
        all_data.extend(openphish_data)
        
        # Try PhishTank if we have an API key or want to try public feed
        # phishtank_data = self.fetch_phishtank()
        # all_data.extend(phishtank_data)
        
        if all_data:
            self._save_cache(all_data)
        
        return all_data
    
    def get_sample_data(self) -> List[Dict]:
        """Generate sample data for testing/demo purposes"""
        print("Generating sample data for demo...")
        
        # More diverse sample URLs with realistic patterns
        sample_urls = [
            # PayPal (20%)
            "http://paypal-verify.malicious.com/login",
            "https://secure-paypal.phishing.net/account",
            "http://paypal-security.scam.org/verify",
            "https://paypal-support.evil.com/confirm",
            "http://paypal.fake-verify.com/login",
            
            # Microsoft (18%)
            "https://microsoft-security.phishing.net/account",
            "http://office365-login.malicious.com/signin",
            "https://outlook-verify.scam.org/account",
            "http://onedrive-share.evil.com/files",
            "https://microsoft-support.fake.com/verify",
            
            # Google (15%)
            "http://google-drive-share.evil.com/docs",
            "https://gmail-verify.phishing.net/account",
            "http://google-security.malicious.com/check",
            "https://drive-google.scam.org/share",
            
            # Facebook (12%)
            "https://facebook-security.malicious.net/verify",
            "http://fb-account-verify.phishing.net/login",
            "https://meta-security.scam.org/check",
            
            # Banks (10%)
            "https://chase-bank.phishing.net/login",
            "http://bankofamerica-secure.evil.com/verify",
            "https://wellsfargo-login.malicious.com/account",
            
            # Amazon (8%)
            "http://amazon-prize.fake.com/winner",
            "https://amazon-security.phishing.net/verify",
            
            # Apple (7%)
            "https://apple-support.scam.org/icloud",
            "http://appleid-verify.malicious.com/login",
            
            # Netflix (5%)
            "http://netflix-billing.phish.com/payment",
            "https://netflix-account.scam.org/update",
            
            # LinkedIn (3%)
            "https://linkedin-profile.scam.org/update",
            
            # Shipping (2%)
            "http://dhl-delivery.evil.com/track",
            "https://fedex-package.malicious.com/track",
            
            # Crypto (5%)
            "https://binance-security.phishing.net/verify",
            "http://coinbase-wallet.scam.org/login",
            
            # Instagram (3%)
            "https://instagram-verify.malicious.net/account",
            
            # WhatsApp (2%)
            "http://whatsapp-verify.phishing.net/account",
            
            # Adobe (2%)
            "https://adobe-account.scam.org/verify",
            
            # Other generic phishing (8%)
            "http://suspicious-site-12345.com/phish",
            "https://random-phishing.net/login",
            "http://generic-scam.org/verify",
            "https://unknown-threat.com/account",
        ]
        
        data = []
        base_time = datetime.now()
        
        # Generate varied data with different timestamps
        for i in range(100):  # Generate 100 entries
            # Select URL with some randomness
            url_index = (i * 7) % len(sample_urls)  # Semi-random distribution
            url = sample_urls[url_index]
            
            data.append({
                'url': url,
                'source': 'sample',
                'verified': 'yes',
                'verification_time': (base_time - timedelta(hours=i % 48, minutes=i % 60)).isoformat(),
                'submission_time': (base_time - timedelta(hours=i % 48, minutes=(i + 30) % 60)).isoformat()
            })
        
        return data


if __name__ == "__main__":
    # Test the fetcher
    fetcher = PhishingDataFetcher()
    data = fetcher.fetch_all()
    print(f"\nTotal phishing URLs fetched: {len(data)}")
    if data:
        print(f"Sample entry: {data[0]}")

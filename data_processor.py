"""
Data processor for analyzing phishing URLs and extracting insights
"""
import re
import socket
from urllib.parse import urlparse
from datetime import datetime
from typing import Dict, List, Optional
import random
import tldextract
import config


class PhishingDataProcessor:
    """Process and analyze phishing data"""
    
    def __init__(self):
        # Country mapping based on TLD (simplified)
        self.tld_to_country = {
            'uk': 'United Kingdom', 'us': 'United States', 'ca': 'Canada',
            'au': 'Australia', 'de': 'Germany', 'fr': 'France', 'it': 'Italy',
            'es': 'Spain', 'nl': 'Netherlands', 'br': 'Brazil', 'in': 'India',
            'cn': 'China', 'jp': 'Japan', 'kr': 'South Korea', 'ru': 'Russia',
            'mx': 'Mexico', 'za': 'South Africa', 'ng': 'Nigeria', 'eg': 'Egypt',
            'se': 'Sweden', 'no': 'Norway', 'dk': 'Denmark', 'fi': 'Finland',
            'pl': 'Poland', 'tr': 'Turkey', 'ar': 'Argentina', 'cl': 'Chile',
            'co': 'Colombia', 'pe': 'Peru', 'id': 'Indonesia', 'th': 'Thailand',
            'vn': 'Vietnam', 'ph': 'Philippines', 'my': 'Malaysia', 'sg': 'Singapore',
            'nz': 'New Zealand', 'ae': 'United Arab Emirates', 'sa': 'Saudi Arabia',
            'il': 'Israel', 'gr': 'Greece', 'pt': 'Portugal', 'ie': 'Ireland',
            'be': 'Belgium', 'at': 'Austria', 'ch': 'Switzerland', 'cz': 'Czech Republic',
            'hu': 'Hungary', 'ro': 'Romania', 'ua': 'Ukraine', 'pk': 'Pakistan',
            'bd': 'Bangladesh', 'kz': 'Kazakhstan', 'hk': 'Hong Kong', 'tw': 'Taiwan'
        }
        
        # ISO country codes for mapping
        self.country_to_iso = {
            'United States': 'USA', 'United Kingdom': 'GBR', 'Canada': 'CAN',
            'Australia': 'AUS', 'Germany': 'DEU', 'France': 'FRA', 'Italy': 'ITA',
            'Spain': 'ESP', 'Netherlands': 'NLD', 'Brazil': 'BRA', 'India': 'IND',
            'China': 'CHN', 'Japan': 'JPN', 'South Korea': 'KOR', 'Russia': 'RUS',
            'Mexico': 'MEX', 'South Africa': 'ZAF', 'Nigeria': 'NGA', 'Egypt': 'EGY',
            'Sweden': 'SWE', 'Norway': 'NOR', 'Denmark': 'DNK', 'Finland': 'FIN',
            'Poland': 'POL', 'Turkey': 'TUR', 'Argentina': 'ARG', 'Chile': 'CHL',
            'Colombia': 'COL', 'Peru': 'PER', 'Indonesia': 'IDN', 'Thailand': 'THA',
            'Vietnam': 'VNM', 'Philippines': 'PHL', 'Malaysia': 'MYS', 'Singapore': 'SGP',
            'New Zealand': 'NZL', 'United Arab Emirates': 'ARE', 'Saudi Arabia': 'SAU',
            'Israel': 'ISR', 'Greece': 'GRC', 'Portugal': 'PRT', 'Ireland': 'IRL',
            'Belgium': 'BEL', 'Austria': 'AUT', 'Switzerland': 'CHE', 'Czech Republic': 'CZE',
            'Hungary': 'HUN', 'Romania': 'ROU', 'Ukraine': 'UKR', 'Pakistan': 'PAK',
            'Bangladesh': 'BGD', 'Kazakhstan': 'KAZ', 'Hong Kong': 'HKG', 'Taiwan': 'TWN',
            'Venezuela': 'VEN', 'Kenya': 'KEN', 'Morocco': 'MAR', 'Algeria': 'DZA',
            'Unknown': 'Unknown'
        }
    
    def extract_domain_info(self, url: str) -> Dict:
        """Extract domain information from URL"""
        try:
            extracted = tldextract.extract(url)
            return {
                'domain': extracted.domain,
                'subdomain': extracted.subdomain,
                'suffix': extracted.suffix,
                'full_domain': f"{extracted.domain}.{extracted.suffix}" if extracted.suffix else extracted.domain
            }
        except Exception as e:
            return {
                'domain': 'unknown',
                'subdomain': '',
                'suffix': '',
                'full_domain': 'unknown'
            }
    
    def detect_brand(self, url: str) -> str:
        """Detect which brand is being impersonated"""
        url_lower = url.lower()
        
        for brand, keywords in config.BRAND_KEYWORDS.items():
            if brand == 'Other':
                continue
            for keyword in keywords:
                if keyword in url_lower:
                    return brand
        
        return 'Other'
    
    def detect_attack_type(self, url: str) -> str:
        """Detect the type of phishing attack"""
        url_lower = url.lower()
        
        for attack_type, patterns in config.ATTACK_TYPE_PATTERNS.items():
            if attack_type == 'Other':
                continue
            for pattern in patterns:
                if pattern in url_lower:
                    return attack_type
        
        return 'Other'
    
    def get_country_from_url(self, url: str) -> str:
        """Attempt to determine country from URL"""
        try:
            domain_info = self.extract_domain_info(url)
            suffix = domain_info['suffix'].lower()
            
            # Check if it's a country TLD
            if suffix in self.tld_to_country:
                return self.tld_to_country[suffix]
            
            # For generic TLDs (.com, .net, etc), use probabilistic assignment
            # This simulates geolocation for demo purposes
            # In production, you'd use IP geolocation APIs
            return self._simulate_country_from_domain(domain_info['full_domain'])
            
        except Exception as e:
            return 'Unknown'
    
    def _simulate_country_from_domain(self, domain: str) -> str:
        """Simulate country detection for demo purposes based on domain hash"""
        # Common phishing source countries (for realistic demo data)
        likely_countries = [
            'United States', 'Russia', 'China', 'Brazil', 'India',
            'Nigeria', 'Ukraine', 'Vietnam', 'Indonesia', 'Turkey',
            'Romania', 'Pakistan', 'Bangladesh', 'Philippines', 'Thailand',
            'Mexico', 'South Africa', 'Egypt', 'Colombia', 'Argentina'
        ]
        
        # Use domain hash for consistent assignment (same domain = same country)
        domain_hash = hash(domain) % len(likely_countries)
        return likely_countries[domain_hash]
    
    def get_iso_code(self, country: str) -> str:
        """Get ISO-3 country code"""
        return self.country_to_iso.get(country, 'Unknown')
    
    def parse_timestamp(self, timestamp_str: str) -> Optional[datetime]:
        """Parse various timestamp formats"""
        if not timestamp_str:
            return None
        
        try:
            # Try ISO format first
            return datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        except:
            try:
                # Try other common formats
                return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            except:
                return None
    
    def process_entry(self, entry: Dict) -> Dict:
        """Process a single phishing entry"""
        url = entry.get('url', '')
        
        processed = {
            'url': url,
            'source': entry.get('source', 'unknown'),
            'brand': self.detect_brand(url),
            'attack_type': self.detect_attack_type(url),
            'country': self.get_country_from_url(url),
            'domain_info': self.extract_domain_info(url),
            'timestamp': self.parse_timestamp(entry.get('verification_time', '')),
            'submission_time': self.parse_timestamp(entry.get('submission_time', '')),
            'verified': entry.get('verified', 'no')
        }
        
        processed['iso_code'] = self.get_iso_code(processed['country'])
        
        return processed
    
    def process_all(self, raw_data: List[Dict]) -> List[Dict]:
        """Process all phishing entries"""
        print(f"Processing {len(raw_data)} phishing URLs...")
        
        processed_data = []
        for entry in raw_data:
            try:
                processed = self.process_entry(entry)
                processed_data.append(processed)
            except Exception as e:
                print(f"Error processing entry: {e}")
                continue
        
        print(f"Successfully processed {len(processed_data)} entries")
        return processed_data
    
    def get_statistics(self, processed_data: List[Dict]) -> Dict:
        """Generate statistics from processed data"""
        if not processed_data:
            return {}
        
        stats = {
            'total_urls': len(processed_data),
            'brands': {},
            'attack_types': {},
            'countries': {},
            'sources': {}
        }
        
        for entry in processed_data:
            # Count brands
            brand = entry['brand']
            stats['brands'][brand] = stats['brands'].get(brand, 0) + 1
            
            # Count attack types
            attack_type = entry['attack_type']
            stats['attack_types'][attack_type] = stats['attack_types'].get(attack_type, 0) + 1
            
            # Count countries
            country = entry['country']
            stats['countries'][country] = stats['countries'].get(country, 0) + 1
            
            # Count sources
            source = entry['source']
            stats['sources'][source] = stats['sources'].get(source, 0) + 1
        
        return stats


if __name__ == "__main__":
    # Test the processor
    processor = PhishingDataProcessor()
    
    test_url = "http://paypal-verify.malicious.com/login"
    result = processor.process_entry({'url': test_url, 'source': 'test'})
    print(f"Processed: {result}")

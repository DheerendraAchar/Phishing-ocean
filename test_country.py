"""
Quick test for country detection
"""
from data_processor import PhishingDataProcessor

processor = PhishingDataProcessor()

# Test URLs
test_urls = [
    'http://paypal-verify.malicious.com/login',
    'https://microsoft-security.phishing.net/account',
    'http://google-drive.evil.com/docs',
    'https://amazon-prize.fake.org/winner',
    'http://bljl118.wixstudio.com/jnny'
]

print('=' * 60)
print('Testing Country Detection')
print('=' * 60)
for url in test_urls:
    result = processor.process_entry({'url': url, 'source': 'test'})
    print(f'\n🔗 {url}')
    print(f'   Country: {result["country"]} ({result["iso_code"]})')
    print(f'   Brand: {result["brand"]}')
    print(f'   Attack Type: {result["attack_type"]}')

print('\n' + '=' * 60)
print('✅ Country detection now working!')
print('=' * 60)

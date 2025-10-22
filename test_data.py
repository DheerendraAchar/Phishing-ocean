"""
Example script to test fetching live phishing data
Run this to see how the data fetcher works with real data
"""
from data_fetcher import PhishingDataFetcher
from data_processor import PhishingDataProcessor

def main():
    print("=" * 60)
    print("Phishing Data Test - Fetching Live Data")
    print("=" * 60)
    print()
    
    # Initialize fetcher and processor
    fetcher = PhishingDataFetcher()
    processor = PhishingDataProcessor()
    
    # Fetch data (will use cache if available)
    print("📥 Fetching phishing data...")
    raw_data = fetcher.fetch_all()
    
    if not raw_data:
        print("⚠️  No data fetched. Generating sample data...")
        raw_data = fetcher.get_sample_data()
    
    print(f"✓ Fetched {len(raw_data)} phishing URLs\n")
    
    # Process data
    print("🔄 Processing data...")
    processed_data = processor.process_all(raw_data)
    print(f"✓ Processed {len(processed_data)} entries\n")
    
    # Get statistics
    stats = processor.get_statistics(processed_data)
    
    print("=" * 60)
    print("📊 Statistics Summary")
    print("=" * 60)
    print(f"Total URLs analyzed: {stats['total_urls']}")
    print()
    
    print("🎯 Top 5 Targeted Brands:")
    sorted_brands = sorted(stats['brands'].items(), key=lambda x: x[1], reverse=True)[:5]
    for brand, count in sorted_brands:
        print(f"  - {brand}: {count} attacks")
    print()
    
    print("🌍 Top 5 Source Countries:")
    sorted_countries = sorted(stats['countries'].items(), key=lambda x: x[1], reverse=True)[:5]
    for country, count in sorted_countries:
        if country != 'Unknown':
            print(f"  - {country}: {count} attacks")
    print()
    
    print("⚔️  Attack Types:")
    for attack_type, count in stats['attack_types'].items():
        print(f"  - {attack_type}: {count} attacks")
    print()
    
    print("=" * 60)
    print("Sample entries:")
    print("=" * 60)
    for entry in processed_data[:3]:
        print(f"\n🔗 URL: {entry['url']}")
        print(f"   Brand: {entry['brand']}")
        print(f"   Attack Type: {entry['attack_type']}")
        print(f"   Country: {entry['country']}")
    print()
    
    print("=" * 60)
    print("✅ Test complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

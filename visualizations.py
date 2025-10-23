"""
Visualization module for creating phishing data charts and maps
"""
import plotly.graph_objects as go
import plotly.express as px
from collections import Counter
from datetime import datetime, timedelta
from typing import List, Dict
import pandas as pd


class PhishingVisualizer:
    """Create visualizations for phishing data"""
    
    def __init__(self):
        self.color_scheme = {
            'primary': '#1f77b4',
            'danger': '#d62728',
            'warning': '#ff7f0e',
            'success': '#2ca02c',
            'background': '#f8f9fa'
        }
    
    def create_global_threat_map(self, processed_data: List[Dict]) -> go.Figure:
        """
        Create a choropleth map showing phishing attack origins by country
        """
        if not processed_data:
            # Return empty map
            fig = go.Figure(go.Choropleth())
            fig.update_layout(
                title="Global Threat Map - No Data Available",
                height=600
            )
            return fig
        
        # Count attacks by country
        country_counts = Counter()
        for entry in processed_data:
            country = entry.get('iso_code', 'Unknown')
            if country != 'Unknown':
                country_counts[country] += 1
        
        if not country_counts:
            # Return empty map
            fig = go.Figure(go.Choropleth())
            fig.update_layout(
                title="Global Threat Map - No Location Data",
                height=600
            )
            return fig
        
        # Convert to DataFrame
        df = pd.DataFrame([
            {'country': code, 'attacks': count}
            for code, count in country_counts.items()
        ])
        
        # Create choropleth map
        fig = go.Figure(data=go.Choropleth(
            locations=df['country'],
            z=df['attacks'],
            text=df['country'],
            colorscale='Reds',
            autocolorscale=False,
            reversescale=False,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_title="Number of<br>Attacks",
        ))
        
        fig.update_layout(
            title={
                'text': 'Global Threat Map - Phishing Attack Origins',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20, 'color': '#1a1a1a', 'family': 'Arial, sans-serif'}
            },
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type='natural earth'
            ),
            height=600,
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        return fig
    
    def create_brand_treemap(self, processed_data: List[Dict]) -> go.Figure:
        """
        Create a treemap showing most impersonated brands
        """
        if not processed_data:
            fig = go.Figure()
            fig.update_layout(title="Brand Impersonation - No Data Available")
            return fig
        
        # Count brands
        brand_counts = Counter()
        for entry in processed_data:
            brand = entry.get('brand', 'Other')
            brand_counts[brand] += 1
        
        if not brand_counts:
            fig = go.Figure()
            fig.update_layout(title="Brand Impersonation - No Data Available")
            return fig
        
        # Convert to lists
        brands = list(brand_counts.keys())
        counts = list(brand_counts.values())
        
        # Create treemap
        fig = go.Figure(go.Treemap(
            labels=brands,
            parents=[""] * len(brands),
            values=counts,
            textinfo="label+value+percent parent",
            marker=dict(
                colorscale='RdYlBu',
                line=dict(width=2, color='white')
            ),
            hovertemplate='<b>%{label}</b><br>Attacks: %{value}<br>Percentage: %{percentParent}<extra></extra>'
        ))
        
        fig.update_layout(
            title={
                'text': 'Brand Impersonation Analysis',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 22, 'color': '#1a1a1a', 'family': 'Arial, sans-serif'}
            },
            height=500,
            paper_bgcolor='white'
        )
        
        return fig
    
    def create_attack_timeline(self, processed_data: List[Dict]) -> go.Figure:
        """
        Create a timeline showing attack frequency over time by type
        """
        if not processed_data:
            fig = go.Figure()
            fig.update_layout(title="Attack Timeline - No Data Available")
            return fig
        
        # Filter entries with valid timestamps
        time_data = []
        for entry in processed_data:
            timestamp = entry.get('timestamp') or entry.get('submission_time')
            if timestamp:
                time_data.append({
                    'timestamp': timestamp,
                    'attack_type': entry.get('attack_type', 'Other')
                })
        
        if not time_data:
            # Generate sample timeline data based on relative time
            fig = go.Figure()
            fig.update_layout(title="Attack Timeline - No Timestamp Data")
            return fig
        
        # Convert to DataFrame
        df = pd.DataFrame(time_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.date
        
        # Group by date and attack type
        timeline_data = df.groupby(['date', 'attack_type']).size().reset_index(name='count')
        
        # Create line chart for each attack type
        fig = go.Figure()
        
        attack_types = timeline_data['attack_type'].unique()
        colors = px.colors.qualitative.Set2
        
        for i, attack_type in enumerate(attack_types):
            data = timeline_data[timeline_data['attack_type'] == attack_type]
            fig.add_trace(go.Scatter(
                x=data['date'],
                y=data['count'],
                mode='lines+markers',
                name=attack_type,
                line=dict(width=2, color=colors[i % len(colors)]),
                marker=dict(size=6),
                fill='tonexty' if i > 0 else 'tozeroy',
                hovertemplate='<b>%{fullData.name}</b><br>Date: %{x}<br>Attacks: %{y}<extra></extra>'
            ))
        
        fig.update_layout(
            title={
                'text': 'Attack Frequency Timeline',
                'x': 0.5,
                'xanchor': 'center',
                'y': 0.98,
                'yanchor': 'top',
                'font': {'size': 18, 'color': '#1a1a1a', 'family': 'Arial, sans-serif'}
            },
            xaxis_title='Date',
            yaxis_title='Number of Attacks',
            height=500,
            margin=dict(t=80, b=50, l=50, r=50),
            hovermode='x unified',
            paper_bgcolor='white',
            plot_bgcolor='white',
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='#e0e0e0'),
            yaxis=dict(showgrid=True, gridwidth=1, gridcolor='#e0e0e0'),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
        
        return fig
    
    def create_stats_cards(self, processed_data: List[Dict]) -> Dict:
        """
        Create statistics for dashboard cards
        """
        if not processed_data:
            return {
                'total_attacks': 0,
                'top_brand': 'N/A',
                'top_country': 'N/A',
                'top_attack_type': 'N/A'
            }
        
        brand_counts = Counter(entry.get('brand', 'Other') for entry in processed_data)
        country_counts = Counter(entry.get('country', 'Unknown') for entry in processed_data)
        attack_counts = Counter(entry.get('attack_type', 'Other') for entry in processed_data)
        
        stats = {
            'total_attacks': len(processed_data),
            'top_brand': brand_counts.most_common(1)[0][0] if brand_counts else 'N/A',
            'top_brand_count': brand_counts.most_common(1)[0][1] if brand_counts else 0,
            'top_country': country_counts.most_common(1)[0][0] if country_counts else 'N/A',
            'top_country_count': country_counts.most_common(1)[0][1] if country_counts else 0,
            'top_attack_type': attack_counts.most_common(1)[0][0] if attack_counts else 'N/A',
            'top_attack_count': attack_counts.most_common(1)[0][1] if attack_counts else 0,
            'unique_brands': len(brand_counts),
            'unique_countries': len([c for c in country_counts.keys() if c != 'Unknown']),
        }
        
        return stats
    
    def create_attack_heatmap(self, processed_data: List[Dict]) -> go.Figure:
        """
        Create a heatmap showing attack patterns by hour and day of week
        """
        if not processed_data:
            fig = go.Figure()
            fig.update_layout(title="Attack Pattern Heatmap - No Data Available")
            return fig
        
        # Filter entries with valid timestamps
        time_data = []
        for entry in processed_data:
            timestamp = entry.get('timestamp') or entry.get('submission_time')
            if timestamp:
                time_data.append(timestamp)
        
        if not time_data:
            fig = go.Figure()
            fig.update_layout(title="Attack Pattern Heatmap - No Timestamp Data")
            return fig
        
        # Convert to pandas for easier manipulation
        df = pd.DataFrame({'timestamp': pd.to_datetime(time_data)})
        df['hour'] = df['timestamp'].dt.hour
        df['day_of_week'] = df['timestamp'].dt.day_name()
        
        # Create pivot table for heatmap
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        heatmap_data = df.groupby(['day_of_week', 'hour']).size().unstack(fill_value=0)
        heatmap_data = heatmap_data.reindex(day_order)
        
        # Create heatmap
        fig = go.Figure(data=go.Heatmap(
            z=heatmap_data.values,
            x=[f"{h:02d}:00" for h in range(24)],
            y=day_order,
            colorscale='Reds',
            hovertemplate='<b>%{y}</b><br>Hour: %{x}<br>Attacks: %{z}<extra></extra>',
            colorbar=dict(title="Attacks")
        ))
        
        fig.update_layout(
            title={
                'text': 'Attack Pattern Heatmap (Hour of Day)',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 22, 'color': '#1a1a1a', 'family': 'Arial, sans-serif'}
            },
            xaxis_title='Hour of Day',
            yaxis_title='Day of Week',
            height=400,
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        return fig
    
    def create_top_domains_chart(self, processed_data: List[Dict]) -> go.Figure:
        """
        Create a horizontal bar chart showing top 10 most attacked domains
        """
        if not processed_data:
            fig = go.Figure()
            fig.update_layout(title="Top Targeted Domains - No Data Available")
            return fig
        
        # Extract domains
        domain_counts = Counter()
        for entry in processed_data:
            domain = entry.get('domain_info', {}).get('full_domain', 'unknown')
            if domain != 'unknown':
                domain_counts[domain] += 1
        
        if not domain_counts:
            fig = go.Figure()
            fig.update_layout(title="Top Targeted Domains - No Data Available")
            return fig
        
        # Get top 10
        top_domains = domain_counts.most_common(10)
        domains = [d[0] for d in top_domains]
        counts = [d[1] for d in top_domains]
        
        # Create horizontal bar chart
        fig = go.Figure(data=[
            go.Bar(
                y=domains[::-1],  # Reverse for better display
                x=counts[::-1],
                orientation='h',
                marker=dict(
                    color=counts[::-1],
                    colorscale='Reds',
                    showscale=False
                ),
                text=counts[::-1],
                textposition='outside',
                hovertemplate='<b>%{y}</b><br>Attacks: %{x}<extra></extra>'
            )
        ])
        
        fig.update_layout(
            title={
                'text': 'Top 10 Targeted Domains',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 22, 'color': '#1a1a1a', 'family': 'Arial, sans-serif'}
            },
            xaxis_title='Number of Attacks',
            yaxis_title='Domain',
            height=400,
            paper_bgcolor='white',
            plot_bgcolor='white',
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='#e0e0e0'),
            margin=dict(l=200)  # More space for long domain names
        )
        
        return fig
    
    def create_attack_pie_chart(self, processed_data: List[Dict]) -> go.Figure:
        """
        Create a donut chart showing attack type distribution
        """
        if not processed_data:
            fig = go.Figure()
            fig.update_layout(title="Attack Type Distribution - No Data Available")
            return fig
        
        # Count attack types
        attack_counts = Counter()
        for entry in processed_data:
            attack_type = entry.get('attack_type', 'Other')
            attack_counts[attack_type] += 1
        
        if not attack_counts:
            fig = go.Figure()
            fig.update_layout(title="Attack Type Distribution - No Data Available")
            return fig
        
        # Create pie chart
        labels = list(attack_counts.keys())
        values = list(attack_counts.values())
        
        colors = px.colors.qualitative.Set3
        
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.4,  # Makes it a donut chart
            marker=dict(colors=colors[:len(labels)]),
            textinfo='label+percent',
            textposition='auto',
            hovertemplate='<b>%{label}</b><br>Attacks: %{value}<br>Percentage: %{percent}<extra></extra>'
        )])
        
        fig.update_layout(
            title={
                'text': 'Attack Type Distribution',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 22, 'color': '#1a1a1a', 'family': 'Arial, sans-serif'}
            },
            height=400,
            paper_bgcolor='white',
            showlegend=True,
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.05
            )
        )
        
        return fig
    
    def create_url_length_distribution(self, processed_data: List[Dict]) -> go.Figure:
        """
        Create a histogram showing distribution of phishing URL lengths
        """
        if not processed_data:
            fig = go.Figure()
            fig.update_layout(title="URL Length Distribution - No Data Available")
            return fig
        
        # Extract URL lengths
        url_lengths = []
        for entry in processed_data:
            url = entry.get('url', '')
            if url:
                url_lengths.append(len(url))
        
        if not url_lengths:
            fig = go.Figure()
            fig.update_layout(title="URL Length Distribution - No Data Available")
            return fig
        
        # Create histogram
        fig = go.Figure(data=[
            go.Histogram(
                x=url_lengths,
                nbinsx=30,
                marker=dict(
                    color='#ff7f0e',
                    line=dict(color='white', width=1)
                ),
                hovertemplate='Length: %{x}<br>Count: %{y}<extra></extra>'
            )
        ])
        
        # Add average line
        avg_length = sum(url_lengths) / len(url_lengths)
        fig.add_vline(
            x=avg_length,
            line_dash="dash",
            line_color="red",
            annotation_text=f"Avg: {avg_length:.0f}",
            annotation_position="top"
        )
        
        fig.update_layout(
            title={
                'text': 'Phishing URL Length Distribution',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 22, 'color': '#1a1a1a', 'family': 'Arial, sans-serif'}
            },
            xaxis_title='URL Length (characters)',
            yaxis_title='Frequency',
            height=400,
            paper_bgcolor='white',
            plot_bgcolor='white',
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='#e0e0e0'),
            yaxis=dict(showgrid=True, gridwidth=1, gridcolor='#e0e0e0'),
            bargap=0.1
        )
        
        return fig


if __name__ == "__main__":
    # Test visualizations
    visualizer = PhishingVisualizer()
    
    # Create sample data
    sample_data = [
        {'brand': 'PayPal', 'country': 'United States', 'iso_code': 'USA', 
         'attack_type': 'Fake Login Page', 'timestamp': datetime.now()},
        {'brand': 'Microsoft', 'country': 'Russia', 'iso_code': 'RUS', 
         'attack_type': 'Malicious Link', 'timestamp': datetime.now()},
        {'brand': 'Google', 'country': 'China', 'iso_code': 'CHN', 
         'attack_type': 'Fake Login Page', 'timestamp': datetime.now()},
    ]
    
    stats = visualizer.create_stats_cards(sample_data)
    print(f"Stats: {stats}")

"""
Phishing Ocean Dashboard 🎣
Main dashboard application using Dash and Plotly
"""
import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from datetime import datetime
import config
from data_fetcher import PhishingDataFetcher
from data_processor import PhishingDataProcessor
from visualizations import PhishingVisualizer


# Initialize components
fetcher = PhishingDataFetcher()
processor = PhishingDataProcessor()
visualizer = PhishingVisualizer()

# Initialize Dash app with Bootstrap theme
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True
)

app.title = config.DASHBOARD_TITLE

# Global data storage (in production, use proper caching)
app_data = {
    'raw_data': [],
    'processed_data': [],
    'last_update': None
}


def fetch_and_process_data(use_sample=False):
    """Fetch and process phishing data"""
    global app_data
    
    try:
        # Fetch data
        if use_sample:
            raw_data = fetcher.get_sample_data()
        else:
            raw_data = fetcher.fetch_all()
        
        # Process data
        processed_data = processor.process_all(raw_data)
        
        # Convert datetime objects to ISO strings for JSON serialization
        for entry in processed_data:
            if entry.get('timestamp') and isinstance(entry['timestamp'], datetime):
                entry['timestamp'] = entry['timestamp'].isoformat()
            if entry.get('submission_time') and isinstance(entry['submission_time'], datetime):
                entry['submission_time'] = entry['submission_time'].isoformat()
        
        # Update global storage
        app_data['raw_data'] = raw_data
        app_data['processed_data'] = processed_data
        app_data['last_update'] = datetime.now()
        
        return processed_data
    except Exception as e:
        print(f"Error fetching/processing data: {e}")
        return []


# Initial data load (use sample for demo)
fetch_and_process_data(use_sample=True)


# Layout Components
def create_header():
    """Create dashboard header"""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1([
                    html.I(className="fas fa-shield-alt me-3", style={'color': '#0066cc'}),
                    "Phishing Threat Intelligence Dashboard"
                ], className="mb-2", style={'color': '#1a1a1a', 'fontWeight': '600'}),
                html.P(
                    "Real-time Global Phishing Attack Analysis & Visualization",
                    className="text-muted mb-0",
                    style={'fontSize': '1.1rem'}
                )
            ], width=7),
            dbc.Col([
                html.Div([
                    # Last update time
                    html.P([
                        html.I(className="fas fa-clock me-2"),
                        "Last Updated: ",
                        html.Span(id="last-update-time", className="fw-bold text-primary")
                    ], className="mb-2 small"),
                    
                    # Refresh button
                    dbc.Button([
                        html.I(className="fas fa-sync-alt me-2"),
                        "Refresh Data"
                    ], id="refresh-button", color="primary", size="sm", className="w-100 mb-2"),
                    
                    # Auto-refresh controls
                    html.Div([
                        html.Div([
                            html.Label("Auto-Refresh", className="me-2 mb-0 small"),
                            dbc.Switch(
                                id="auto-refresh-toggle",
                                value=False,
                                className="d-inline-block"
                            )
                        ], className="d-flex align-items-center mb-2"),
                        dbc.Select(
                            id="refresh-interval-select",
                            options=[
                                {"label": "1 min", "value": "60000"},
                                {"label": "5 min", "value": "300000"},
                                {"label": "15 min", "value": "900000"},
                            ],
                            value="300000",
                            size="sm",
                            disabled=True,
                            className="mb-2"
                        )
                    ]),
                    
                    # Sample data toggle
                    html.Div([
                        html.Label("Demo Mode", className="me-2 mb-0 small"),
                        dbc.Switch(
                            id="use-sample-data",
                            value=True,
                            className="d-inline-block"
                        )
                    ], className="d-flex align-items-center mb-2"),
                    
                    # Dark mode toggle
                    html.Div([
                        html.Label("Dark Mode", className="me-2 mb-0 small"),
                        dbc.Switch(
                            id="dark-mode-toggle",
                            value=False,
                            className="d-inline-block"
                        )
                    ], className="d-flex align-items-center")
                ], className="text-end")
            ], width=5)
        ], className="mb-4 align-items-center")
    ], fluid=True, id="header-container", className="bg-white border-bottom py-4 mb-4", style={'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})


def create_stats_cards():
    """Create statistics cards"""
    return dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.I(className="fas fa-exclamation-triangle fa-2x mb-3", style={'color': '#dc3545'}),
                        html.H3(id="stat-total-attacks", className="mb-1", style={'fontWeight': '700', 'color': '#1a1a1a'}),
                        html.P("Total Threats Detected", className="text-muted mb-0 small text-uppercase", style={'letterSpacing': '0.5px'})
                    ], className="text-center")
                ])
            ], className="shadow-sm border-0", style={'borderLeft': '4px solid #dc3545'})
        ], md=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.I(className="fas fa-building fa-2x mb-3", style={'color': '#ffc107'}),
                        html.H3(id="stat-top-brand", className="mb-1", style={'fontWeight': '700', 'color': '#1a1a1a', 'fontSize': '1.3rem'}),
                        html.P("Most Targeted Brand", className="text-muted mb-0 small text-uppercase", style={'letterSpacing': '0.5px'})
                    ], className="text-center")
                ])
            ], className="shadow-sm border-0", style={'borderLeft': '4px solid #ffc107'})
        ], md=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.I(className="fas fa-globe-americas fa-2x mb-3", style={'color': '#17a2b8'}),
                        html.H3(id="stat-top-country", className="mb-1", style={'fontWeight': '700', 'color': '#1a1a1a', 'fontSize': '1.3rem'}),
                        html.P("Primary Source Region", className="text-muted mb-0 small text-uppercase", style={'letterSpacing': '0.5px'})
                    ], className="text-center")
                ])
            ], className="shadow-sm border-0", style={'borderLeft': '4px solid #17a2b8'})
        ], md=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.I(className="fas fa-crosshairs fa-2x mb-3", style={'color': '#28a745'}),
                        html.H3(id="stat-top-attack", className="mb-1", style={'fontWeight': '700', 'color': '#1a1a1a', 'fontSize': '1.3rem'}),
                        html.P("Primary Attack Vector", className="text-muted mb-0 small text-uppercase", style={'letterSpacing': '0.5px'})
                    ], className="text-center")
                ])
            ], className="shadow-sm border-0", style={'borderLeft': '4px solid #28a745'})
        ], md=3)
    ], className="mb-4")


def create_visualizations():
    """Create visualization components"""
    return html.Div([
        # Filters row
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.Label("Time Range:", className="fw-bold small mb-1"),
                                dbc.Select(
                                    id="date-range-filter",
                                    options=[
                                        {"label": "Last 24 Hours", "value": "24h"},
                                        {"label": "Last 7 Days", "value": "7d"},
                                        {"label": "Last 30 Days", "value": "30d"},
                                        {"label": "All Time", "value": "all"},
                                    ],
                                    value="all",
                                    size="sm"
                                )
                            ], md=3),
                            dbc.Col([
                                html.Label("Attack Type:", className="fw-bold small mb-1"),
                                dcc.Dropdown(
                                    id="attack-type-filter",
                                    options=[],
                                    value="all",
                                    placeholder="All Attack Types",
                                    className="small",
                                    clearable=False
                                )
                            ], md=3),
                            dbc.Col([
                                html.Label("Brand:", className="fw-bold small mb-1"),
                                dcc.Dropdown(
                                    id="brand-filter",
                                    options=[],
                                    value="all",
                                    placeholder="All Brands",
                                    className="small",
                                    clearable=False
                                )
                            ], md=3),
                            dbc.Col([
                                html.Label("Country:", className="fw-bold small mb-1"),
                                dcc.Dropdown(
                                    id="country-filter",
                                    options=[],
                                    value="all",
                                    placeholder="All Countries",
                                    className="small",
                                    clearable=False
                                )
                            ], md=3)
                        ])
                    ])
                ], className="shadow-sm mb-3", style={'backgroundColor': '#f8f9fa'})
            ])
        ]),
        
        # Global Threat Map
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-map",
                            type="circle",
                            children=[
                                dcc.Graph(
                                    id="global-threat-map",
                                    config={'displayModeBar': True, 'displaylogo': False}
                                )
                            ]
                        )
                    ])
                ], className="shadow-sm mb-4")
            ])
        ]),
        
        # Brand Treemap and Timeline
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-treemap",
                            type="circle",
                            children=[
                                dcc.Graph(
                                    id="brand-treemap",
                                    config={'displayModeBar': True, 'displaylogo': False}
                                )
                            ]
                        )
                    ])
                ], className="shadow-sm")
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-timeline",
                            type="circle",
                            children=[
                                dcc.Graph(
                                    id="attack-timeline",
                                    config={'displayModeBar': True, 'displaylogo': False}
                                )
                            ]
                        )
                    ])
                ], className="shadow-sm")
            ], md=6)
        ]),
        
        # New visualizations row 1: Heatmap and Top Domains
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-heatmap",
                            type="circle",
                            children=[
                                dcc.Graph(
                                    id="attack-heatmap",
                                    config={'displayModeBar': True, 'displaylogo': False}
                                )
                            ]
                        )
                    ])
                ], className="shadow-sm mt-4")
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-domains",
                            type="circle",
                            children=[
                                dcc.Graph(
                                    id="top-domains-chart",
                                    config={'displayModeBar': True, 'displaylogo': False}
                                )
                            ]
                        )
                    ])
                ], className="shadow-sm mt-4")
            ], md=6)
        ]),
        
        # New visualizations row 2: Pie Chart and URL Length
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-pie",
                            type="circle",
                            children=[
                                dcc.Graph(
                                    id="attack-pie-chart",
                                    config={'displayModeBar': True, 'displaylogo': False}
                                )
                            ]
                        )
                    ])
                ], className="shadow-sm mt-4")
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-histogram",
                            type="circle",
                            children=[
                                dcc.Graph(
                                    id="url-length-histogram",
                                    config={'displayModeBar': True, 'displaylogo': False}
                                )
                            ]
                        )
                    ])
                ], className="shadow-sm mt-4")
            ], md=6)
        ])
    ])


def create_footer():
    """Create dashboard footer"""
    return dbc.Container([
        html.Hr(className="my-4"),
        dbc.Row([
            dbc.Col([
                html.P([
                    html.I(className="fas fa-database me-2"),
                    "Data Sources: OpenPhish, PhishTank",
                    html.Span(" | ", className="mx-2"),
                    html.I(className="fas fa-code me-2"),
                    "Powered by Dash & Plotly"
                ], className="text-muted mb-0 small")
            ], md=8),
            dbc.Col([
                html.P([
                    html.I(className="fas fa-shield-alt me-2"),
                    "Cybersecurity Intelligence Platform | 2025"
                ], className="text-muted text-end mb-0 small")
            ], md=4)
        ])
    ], fluid=True, className="py-3 bg-white border-top")


# Main Layout
app.layout = html.Div([
    # Store components for data
    dcc.Store(id='data-store'),
    dcc.Store(id='dark-mode-store', data=False),  # Store dark mode state
    
    # Auto-refresh interval
    dcc.Interval(
        id='interval-component',
        interval=config.DATA_REFRESH_INTERVAL,
        n_intervals=0,
        disabled=True  # Controlled by toggle
    ),
    
    # Header
    create_header(),
    
    # Main content
    dbc.Container([
        # Stats cards
        create_stats_cards(),
        
        # Visualizations
        create_visualizations(),
    ], fluid=True),
    
    # Footer
    create_footer()
], style={'backgroundColor': '#f8f9fa', 'minHeight': '100vh'})


# Callbacks
@app.callback(
    [Output('interval-component', 'disabled'),
     Output('interval-component', 'interval'),
     Output('refresh-interval-select', 'disabled')],
    [Input('auto-refresh-toggle', 'value'),
     Input('refresh-interval-select', 'value')]
)
def control_auto_refresh(auto_refresh_enabled, interval_value):
    """Enable/disable auto-refresh and set interval"""
    disabled = not auto_refresh_enabled
    interval = int(interval_value) if interval_value else config.DATA_REFRESH_INTERVAL
    select_disabled = not auto_refresh_enabled
    return disabled, interval, select_disabled


@app.callback(
    [Output('attack-type-filter', 'options'),
     Output('brand-filter', 'options'),
     Output('country-filter', 'options')],
    [Input('data-store', 'data')],
    prevent_initial_call=False
)
def update_filter_options(processed_data):
    """Update filter dropdown options based on available data"""
    if not processed_data:
        return [], [], []
    
    # Get unique values
    attack_types = sorted(set(entry.get('attack_type', 'Other') for entry in processed_data))
    brands = sorted(set(entry.get('brand', 'Other') for entry in processed_data))
    countries = sorted(set(entry.get('country', 'Unknown') for entry in processed_data if entry.get('country') != 'Unknown'))
    
    # Create options with "All" as first option
    attack_options = [{'label': 'All Attack Types', 'value': 'all'}] + [{'label': at, 'value': at} for at in attack_types]
    brand_options = [{'label': 'All Brands', 'value': 'all'}] + [{'label': b, 'value': b} for b in brands]
    country_options = [{'label': 'All Countries', 'value': 'all'}] + [{'label': c, 'value': c} for c in countries]
    
    return attack_options, brand_options, country_options


def filter_data_by_criteria(data, date_range, attack_type, brand, country):
    """Filter data based on selected criteria"""
    try:
        if not data:
            return []
        
        filtered = list(data)
        initial_count = len(filtered)
        
        print(f"\n=== FILTERING DEBUG ===")
        print(f"Initial data count: {initial_count}")
        print(f"Filters - Date: {date_range}, Attack: {attack_type}, Brand: {brand}, Country: {country}")
        
        # Date range filter
        if date_range and date_range != 'all':
            from datetime import datetime, timedelta
            now = datetime.now()
            
            if date_range == '24h':
                cutoff = now - timedelta(hours=24)
            elif date_range == '7d':
                cutoff = now - timedelta(days=7)
            elif date_range == '30d':
                cutoff = now - timedelta(days=30)
            else:
                cutoff = None
            
            if cutoff:
                before_count = len(filtered)
                print(f"  Cutoff time: {cutoff}")
                # Filter entries with valid timestamps within the date range
                filtered_with_details = []
                for entry in filtered:
                    ts = entry.get('timestamp')
                    # Parse ISO string back to datetime if needed
                    if ts and isinstance(ts, str):
                        try:
                            ts = datetime.fromisoformat(ts)
                        except:
                            ts = None
                    
                    if ts is not None and isinstance(ts, datetime) and ts >= cutoff:
                        filtered_with_details.append(entry)
                
                filtered = filtered_with_details
                print(f"  Sample timestamps: {[entry.get('timestamp')[:19] if isinstance(entry.get('timestamp'), str) else str(entry.get('timestamp'))[:19] for entry in filtered[:3]]}")
                print(f"After date filter ({date_range}): {len(filtered)} (removed {before_count - len(filtered)})")
        
        # Attack type filter
        if attack_type and attack_type != 'all':
            before_count = len(filtered)
            filtered = [entry for entry in filtered if entry.get('attack_type') == attack_type]
            print(f"After attack type filter ({attack_type}): {len(filtered)} (removed {before_count - len(filtered)})")
        
        # Brand filter
        if brand and brand != 'all':
            before_count = len(filtered)
            filtered = [entry for entry in filtered if entry.get('brand') == brand]
            print(f"After brand filter ({brand}): {len(filtered)} (removed {before_count - len(filtered)})")
        
        # Country filter
        if country and country != 'all':
            before_count = len(filtered)
            filtered = [entry for entry in filtered if entry.get('country') == country]
            print(f"After country filter ({country}): {len(filtered)} (removed {before_count - len(filtered)})")
        
        print(f"Final filtered count: {len(filtered)}")
        print(f"=== END FILTERING ===\n")
        
        return filtered
    except Exception as e:
        print(f"Error filtering data: {e}")
        import traceback
        traceback.print_exc()
        return data if data else []


@app.callback(
    [Output('data-store', 'data'),
     Output('last-update-time', 'children')],
    [Input('refresh-button', 'n_clicks'),
     Input('interval-component', 'n_intervals')],
    [State('use-sample-data', 'value')]
)
def update_data(n_clicks, n_intervals, use_sample):
    """Update data when refresh button is clicked or interval triggers"""
    processed_data = fetch_and_process_data(use_sample=use_sample)
    
    last_update = app_data['last_update']
    if last_update:
        time_str = last_update.strftime("%Y-%m-%d %H:%M:%S")
    else:
        time_str = "Never"
    
    return processed_data, time_str


@app.callback(
    [Output('stat-total-attacks', 'children'),
     Output('stat-top-brand', 'children'),
     Output('stat-top-country', 'children'),
     Output('stat-top-attack', 'children')],
    [Input('data-store', 'data'),
     Input('date-range-filter', 'value'),
     Input('attack-type-filter', 'value'),
     Input('brand-filter', 'value'),
     Input('country-filter', 'value')],
    prevent_initial_call=False
)
def update_stats(processed_data, date_range, attack_type, brand, country):
    """Update statistics cards with filtered data"""
    if not processed_data:
        return "0", "N/A", "N/A", "N/A"
    
    # Apply filters
    filtered_data = filter_data_by_criteria(processed_data, date_range, attack_type, brand, country)
    
    if not filtered_data:
        return "0", "N/A (filtered)", "N/A (filtered)", "N/A (filtered)"
    
    stats = visualizer.create_stats_cards(filtered_data)
    
    return (
        f"{stats['total_attacks']:,}",
        f"{stats['top_brand']} ({stats['top_brand_count']})",
        f"{stats['top_country']} ({stats['top_country_count']})",
        f"{stats['top_attack_type'][:20]}"
    )


@app.callback(
    Output('global-threat-map', 'figure'),
    [Input('data-store', 'data'),
     Input('date-range-filter', 'value'),
     Input('attack-type-filter', 'value'),
     Input('brand-filter', 'value'),
     Input('country-filter', 'value')],
    prevent_initial_call=False
)
def update_map(processed_data, date_range, attack_type, brand, country):
    """Update global threat map with filtered data"""
    if not processed_data:
        return visualizer.create_global_threat_map([])
    
    filtered_data = filter_data_by_criteria(processed_data, date_range, attack_type, brand, country)
    return visualizer.create_global_threat_map(filtered_data)


@app.callback(
    Output('brand-treemap', 'figure'),
    [Input('data-store', 'data'),
     Input('date-range-filter', 'value'),
     Input('attack-type-filter', 'value'),
     Input('brand-filter', 'value'),
     Input('country-filter', 'value')],
    prevent_initial_call=False
)
def update_treemap(processed_data, date_range, attack_type, brand, country):
    """Update brand impersonation treemap with filtered data"""
    if not processed_data:
        return visualizer.create_brand_treemap([])
    
    filtered_data = filter_data_by_criteria(processed_data, date_range, attack_type, brand, country)
    return visualizer.create_brand_treemap(filtered_data)


@app.callback(
    Output('attack-timeline', 'figure'),
    [Input('data-store', 'data'),
     Input('date-range-filter', 'value'),
     Input('attack-type-filter', 'value'),
     Input('brand-filter', 'value'),
     Input('country-filter', 'value')],
    prevent_initial_call=False
)
def update_timeline(processed_data, date_range, attack_type, brand, country):
    """Update attack timeline with filtered data"""
    if not processed_data:
        return visualizer.create_attack_timeline([])
    
    filtered_data = filter_data_by_criteria(processed_data, date_range, attack_type, brand, country)
    return visualizer.create_attack_timeline(filtered_data)


@app.callback(
    Output('attack-heatmap', 'figure'),
    [Input('data-store', 'data'),
     Input('date-range-filter', 'value'),
     Input('attack-type-filter', 'value'),
     Input('brand-filter', 'value'),
     Input('country-filter', 'value')],
    prevent_initial_call=False
)
def update_heatmap(processed_data, date_range, attack_type, brand, country):
    """Update attack pattern heatmap with filtered data"""
    if not processed_data:
        return visualizer.create_attack_heatmap([])
    
    filtered_data = filter_data_by_criteria(processed_data, date_range, attack_type, brand, country)
    return visualizer.create_attack_heatmap(filtered_data)


@app.callback(
    Output('top-domains-chart', 'figure'),
    [Input('data-store', 'data'),
     Input('date-range-filter', 'value'),
     Input('attack-type-filter', 'value'),
     Input('brand-filter', 'value'),
     Input('country-filter', 'value')],
    prevent_initial_call=False
)
def update_domains(processed_data, date_range, attack_type, brand, country):
    """Update top domains chart with filtered data"""
    if not processed_data:
        return visualizer.create_top_domains_chart([])
    
    filtered_data = filter_data_by_criteria(processed_data, date_range, attack_type, brand, country)
    return visualizer.create_top_domains_chart(filtered_data)


@app.callback(
    Output('attack-pie-chart', 'figure'),
    [Input('data-store', 'data'),
     Input('date-range-filter', 'value'),
     Input('attack-type-filter', 'value'),
     Input('brand-filter', 'value'),
     Input('country-filter', 'value')],
    prevent_initial_call=False
)
def update_pie(processed_data, date_range, attack_type, brand, country):
    """Update attack type pie chart with filtered data"""
    if not processed_data:
        return visualizer.create_attack_pie_chart([])
    
    filtered_data = filter_data_by_criteria(processed_data, date_range, attack_type, brand, country)
    return visualizer.create_attack_pie_chart(filtered_data)


@app.callback(
    Output('url-length-histogram', 'figure'),
    [Input('data-store', 'data'),
     Input('date-range-filter', 'value'),
     Input('attack-type-filter', 'value'),
     Input('brand-filter', 'value'),
     Input('country-filter', 'value')],
    prevent_initial_call=False
)
def update_histogram(processed_data, date_range, attack_type, brand, country):
    """Update URL length histogram with filtered data"""
    if not processed_data:
        return visualizer.create_url_length_distribution([])
    
    filtered_data = filter_data_by_criteria(processed_data, date_range, attack_type, brand, country)
    return visualizer.create_url_length_distribution(filtered_data)


@app.callback(
    [Output('dark-mode-store', 'data'),
     Output('header-container', 'style'),
     Output('header-container', 'className')],
    [Input('dark-mode-toggle', 'value')]
)
def toggle_dark_mode(dark_mode):
    """Toggle between dark and light mode"""
    if dark_mode:
        # Dark mode styles
        header_style = {'boxShadow': '0 2px 4px rgba(0,0,0,0.3)', 'backgroundColor': '#1a1a1a', 'borderBottom': '1px solid #333'}
        header_class = "border-bottom py-4 mb-4"
        return True, header_style, header_class
    else:
        # Light mode styles  
        header_style = {'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}
        header_class = "bg-white border-bottom py-4 mb-4"
        return False, header_style, header_class


# Client-side callback for dark mode styling
app.clientside_callback(
    """
    function(darkMode) {
        if (darkMode) {
            // Dark mode
            document.body.style.backgroundColor = '#121212';
            document.body.style.color = '#e0e0e0';
            
            // Update all cards
            var cards = document.querySelectorAll('.card');
            cards.forEach(function(card) {
                card.style.backgroundColor = '#1e1e1e';
                card.style.color = '#e0e0e0';
                card.style.borderColor = '#333';
            });
            
            // Update text elements
            var textMuted = document.querySelectorAll('.text-muted');
            textMuted.forEach(function(el) {
                el.style.color = '#999 !important';
            });
            
            // Update h1
            var headers = document.querySelectorAll('h1, h2, h3');
            headers.forEach(function(h) {
                h.style.color = '#e0e0e0';
            });
            
        } else {
            // Light mode
            document.body.style.backgroundColor = '#f8f9fa';
            document.body.style.color = '#1a1a1a';
            
            // Reset cards
            var cards = document.querySelectorAll('.card');
            cards.forEach(function(card) {
                card.style.backgroundColor = '#fff';
                card.style.color = '#1a1a1a';
                card.style.borderColor = '#dee2e6';
            });
            
            // Reset text
            var textMuted = document.querySelectorAll('.text-muted');
            textMuted.forEach(function(el) {
                el.style.color = '';
            });
            
            // Reset headers
            var headers = document.querySelectorAll('h1, h2, h3');
            headers.forEach(function(h) {
                h.style.color = '#1a1a1a';
            });
        }
        return '';
    }
    """,
    Output('data-store', 'id'),  # Dummy output
    [Input('dark-mode-store', 'data')]
)


# Run the app
if __name__ == '__main__':
    print(f"\n{'='*70}")
    print(f"  PHISHING THREAT INTELLIGENCE DASHBOARD")
    print(f"{'='*70}")
    print(f"  Status: Starting server...")
    print(f"  URL: http://localhost:{config.DASHBOARD_PORT}")
    print(f"  Mode: Development")
    print(f"  Press Ctrl+C to stop")
    print(f"{'='*70}\n")
    
    app.run_server(
        debug=True,
        host=config.DASHBOARD_HOST,
        port=config.DASHBOARD_PORT
    )

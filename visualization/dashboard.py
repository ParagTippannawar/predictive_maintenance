import dash
from dash import dcc, html 
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine
import time

# Connect to the SQLite database
engine = create_engine('sqlite:///C:/Users/parag/predictive_maintenance/maintenance_db.db')

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout of the dashboard
app.layout = html.Div([
    html.H1("Real-Time Machine Data Dashboard"),
    
    dcc.Interval(
        id = 'interval-component',
        interval = 10 * 1000, # Update every 10 seconds
        n_intervals = 0
    ),
    
    dcc.Graph(id = 'temperature-chart'),
    dcc.Graph(id = 'cycle-count-chart'),
    dcc.Graph(id = 'machine-status-chart')
])

# Define callbacks for updating charts
@app.callback(
    [Output('temperature-chart', 'figure'),
    Output('cycle-count-chart', 'figure'),
    Output('machine-status-chart', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_chart(n):
    # Load data from the database
    query = 'SELECT * FROM machine_data ORDER BY timestamp DESC LIMIT 100'
    df = pd.read_sql(query, engine)
    
    # Temprature chart
    fig_temp = px.line(
        df, x = 'timestamp', y = 'temperature',
        title = 'Temperature Over Time',
        labels = { 'temperature': 'Temperature (°C)', 'timestamp': 'Time'}
    )
    
    # Cycle count chart
    fig_cycle = px.line(
        df, x = 'timestamp', y = 'cycle_count',
        title = 'Cycle Count Over Time',
        labels = {'cycle_count': 'Cycl Count', 'timestamp': 'Time'}
    )
    
    # Machine status chart
    fig_status = px.histogram(
        df, x = 'status',
        title = 'Machine Status Distribution',
        labels = {'status' : 'Machine Status'}
    )
    
    return fig_temp, fig_cycle, fig_status
if __name__ == '__main__':
    app.run_server(debug = True)
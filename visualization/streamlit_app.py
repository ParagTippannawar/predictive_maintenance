import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from streamlit_autorefresh import st_autorefresh

# Connect to the SQLite database
engine = create_engine('sqlite:///C:/Users/parag/predictive_maintenance/maintenance_db.db')

# Set up the Streamlit app
st.set_page_config(page_title="Real-Time Machine Dashboard", layout="wide")

# Title
st.title("Real-Time Machine Data Dashboard")

# Sidebar for configuration
st.sidebar.header("Settings")
update_interval = st.sidebar.slider("Update Interval (seconds)", 5, 30, 10)

# Auto-refresh mechanism
st_autorefresh(interval=update_interval * 1000, key="auto_refresh")

# Function to load data from the database
@st.cache_data(ttl=60)
def load_data():
    query = 'SELECT * FROM machine_data ORDER BY timestamp DESC LIMIT 100'
    df = pd.read_sql(query, engine)
    return df

# Load data from the database
df = load_data()

# Layout of the dashboard
col1, col2 = st.columns(2)

# Temperature chart
with col1:
    st.subheader("Temperature Over Time")
    fig_temp = px.line(df, x='timestamp', y='temperature', labels={'temperature': 'Temperature (°C)', 'timestamp': 'Time'}, color_discrete_sequence=['#FF6961'])
    st.plotly_chart(fig_temp, use_container_width=True, key='temp_chart')

# Cycle count chart
with col2:
    st.subheader("Cycle Count Over Time")
    fig_cycle = px.line(df, x='timestamp', y='cycle_count', labels={'cycle_count': 'Cycle Count', 'timestamp': 'Time'}, color_discrete_sequence=['#FF6961'])
    st.plotly_chart(fig_cycle, use_container_width=True, key='cycle_chart')

# Machine status chart
st.subheader("Machine Status Distribution")
fig_status = px.histogram(df, x='status', labels={'status': 'Machine Status'}, color_discrete_sequence=['#1E90FF'])
st.plotly_chart(fig_status, use_container_width=True, key='status_chart')
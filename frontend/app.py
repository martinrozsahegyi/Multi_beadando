import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Weather Monitor",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

API = "http://localhost:8000/weather"

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: white;
        text-align: center;
    }
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3B82F6;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-title">🌤️ Weather Monitoring System</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Real-time meteorological data and analysis</p>', unsafe_allow_html=True)

# Add some spacing
st.markdown("---")

# Fetch data
try:
    latest = requests.get(f"{API}/latest").json()
    stats = requests.get(f"{API}/stats").json()
    history = requests.get(f"{API}/history").json()
    
    # Top Section: Key Statistics
    st.subheader("📊 Statistical Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    # Get stats values
    avg_temp = stats.get('avg', 0)
    max_temp = stats.get('max', 0)
    min_temp = stats.get('min', 0)
    count = len(history)
    
    with col1:
        st.metric(
            label="🌡️ Average Temperature",
            value=f"{avg_temp:.1f} °C",
            delta=None
        )
    
    with col2:
        st.metric(
            label="🔥 Maximum Temperature",
            value=f"{max_temp:.1f} °C",
            delta=f"+{max_temp - avg_temp:.1f} °C"
        )
    
    with col3:
        st.metric(
            label="❄️ Minimum Temperature",
            value=f"{min_temp:.1f} °C",
            delta=f"{min_temp - avg_temp:.1f} °C"
        )
    
    with col4:
        st.metric(
            label="📈 Number of Measurements",
            value=f"{count}",
            delta=None
        )
    
    st.markdown("---")
    
    # Latest Weather Section
    st.subheader("🌍 Current Weather")
    
    col1, col2, col3 = st.columns(3)
    
    # Determine weather emoji based on description
    weather_desc = latest.get('description', '').lower()
    if 'clear' in weather_desc or 'sunny' in weather_desc:
        weather_icon = "☀️"
    elif 'cloud' in weather_desc:
        weather_icon = "☁️"
    elif 'rain' in weather_desc:
        weather_icon = "🌧️"
    elif 'snow' in weather_desc:
        weather_icon = "❄️"
    elif 'storm' in weather_desc or 'thunder' in weather_desc:
        weather_icon = "⛈️"
    else:
        weather_icon = "🌤️"
    
    with col1:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%); 
                        padding: 2rem; border-radius: 15px; text-align: center; color: white;">
                <h1 style="font-size: 4rem; margin: 0;">{latest.get('temperature', 0):.1f}°C</h1>
                <p style="font-size: 1.2rem; margin: 0.5rem 0;">Temperature</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%); 
                        padding: 2rem; border-radius: 15px; text-align: center; color: white;">
                <h1 style="font-size: 4rem; margin: 0;">{weather_icon}</h1>
                <p style="font-size: 1.2rem; margin: 0.5rem 0;">{latest.get('description', 'N/A')}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #10B981 0%, #059669 100%); 
                        padding: 2rem; border-radius: 15px; text-align: center; color: white;">
                <h1 style="font-size: 3rem; margin: 0;">📍</h1>
                <p style="font-size: 1.5rem; margin: 0.5rem 0; font-weight: 600;">{latest.get('city', 'N/A')}</p>
                <p style="font-size: 0.9rem; margin: 0; opacity: 0.9;">{latest.get('timestamp', 'N/A')}</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Temperature History Section
    st.subheader("📈 Temperature Trend")
    
    df = pd.DataFrame(history)
    
    if not df.empty and 'temperature' in df.columns:
        # Temperature line chart
        st.markdown("##### 🔹 Temperature Chart")
        st.line_chart(df['temperature'], use_container_width=True, height=400)
        
        # Expandable detailed data section
        with st.expander("🔍 View Detailed Data"):
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=False,
                column_config={
                    "temperature": st.column_config.NumberColumn(
                        "Temperature (°C)",
                        format="%.2f °C"
                    ),
                    "city": st.column_config.TextColumn("City"),
                    "description": st.column_config.TextColumn("Description"),
                    "timestamp": st.column_config.TextColumn("Timestamp")
                }
            )
    else:
        st.info("No temperature data available in history.")
    
    # Footer with last update time
    st.markdown("---")
    st.markdown(f"""
        <div style="text-align: center; color: #64748B; font-size: 0.9rem;">
            Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | 
            Data source: Weather Microservice API
        </div>
    """, unsafe_allow_html=True)

except requests.exceptions.RequestException as e:
    st.error(f"❌ Error fetching data: {str(e)}")
    st.info("Please ensure the backend API is running at http://localhost:8000.")
except Exception as e:
    st.error(f"❌ Unexpected error occurred: {str(e)}")


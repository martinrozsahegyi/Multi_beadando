import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000/weather"

st.title("🌦 Weather Microservice Dashboard")

# ----------- Latest Weather -----------
st.header("Latest Weather Data")

latest = requests.get(f"{API}/latest").json()
st.write(latest)


# ----------- Full History -----------
st.header("Weather History")

history = requests.get(f"{API}/history").json()

if history:
    df = pd.DataFrame(history)
    st.dataframe(df)

    st.subheader("Temperature Over Time")
    st.line_chart(df["temperature"])
else:
    st.info("No weather data available yet. Try refreshing the backend.")
    

# ----------- Stats -----------
st.header("Statistics")

stats = requests.get(f"{API}/stats").json()
st.write(stats)

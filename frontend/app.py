import streamlit as st
import requests
import pandas as pd

API = "http://localhost:8000/weather"

st.title("Időjárás mikroszerviz")

st.header("Legfrissebb adat")
latest = requests.get(f"{API}/latest").json()
st.write(latest)

st.header("Adattörténet")
history = requests.get(f"{API}/history").json()
df = pd.DataFrame(history)
st.line_chart(df["temperature"])
st.dataframe(df)

st.header("Statisztikák")
stats = requests.get(f"{API}/stats").json()
st.write(stats)

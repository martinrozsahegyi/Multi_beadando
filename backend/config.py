from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY", "Budapest")
DB_URL = os.getenv("DB_URL", "sqlite:///./weather.db")

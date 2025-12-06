from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
DB_URL = os.getenv("DB_URL")
CITY = os.getenv("CITY", "Budapest")

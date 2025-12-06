import requests
from ..config import API_KEY, CITY
from ..database import SessionLocal
from ..models.weather_model import Weather

def fetch_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    print("API RESPONSE:", response)  # <-- NAGYON FONTOS: LÁTJUK A VALÓDI HIBÁT

    # Ha az API hibát ad (401, 404, stb.)
    if "main" not in response:
        return {"error": response}

    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]

    db = SessionLocal()
    record = Weather(city=CITY, temperature=temp, description=desc)
    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()

    return {
        "id": record.id,
        "city": record.city,
        "temperature": record.temperature,
        "description": record.description,
        "timestamp": record.timestamp
    }

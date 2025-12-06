from fastapi import APIRouter
from ..database import SessionLocal
from ..models.weather_model import Weather
from ..services.weather_service import fetch_weather

router = APIRouter()

@router.get("/latest")
def get_latest():
    db = SessionLocal()
    data = db.query(Weather).order_by(Weather.id.desc()).first()
    db.close()
    return data

@router.get("/history")
def get_history():
    db = SessionLocal()
    data = db.query(Weather).all()
    db.close()
    return data

@router.get("/stats")
def get_stats():
    db = SessionLocal()
    temps = [w.temperature for w in db.query(Weather).all()]
    db.close()
    return {
        "min": min(temps),
        "max": max(temps),
        "avg": sum(temps) / len(temps)
    }

@router.get("/refresh")
def refresh():
    return fetch_weather()

from fastapi import FastAPI
from .database import Base, engine
from .api.weather_api import router as weather_router
from .services.scheduler import start_scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(weather_router, prefix="/weather")

start_scheduler()  # automatikus frissítés indul

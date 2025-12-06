from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from ..database import Base

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    temperature = Column(Float)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

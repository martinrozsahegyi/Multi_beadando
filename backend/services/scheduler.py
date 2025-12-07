import schedule
import time
from .weather_service import fetch_weather
import threading

def start_scheduler():
    # Azonnal lekérjük az első adatot az alkalmazás indításakor
    fetch_weather()
    
    # Beállítjuk az óránkénti automatikus frissítést
    schedule.every(1).hours.do(fetch_weather)

    def loop():
        while True:
            schedule.run_pending()
            time.sleep(1)

    t = threading.Thread(target=loop, daemon=True)
    t.start()

import schedule
import time
from .weather_service import fetch_weather
import threading

def start_scheduler():
    schedule.every(1).hours.do(fetch_weather)

    def loop():
        while True:
            schedule.run_pending()
            time.sleep(1)

    t = threading.Thread(target=loop, daemon=True)
    t.start()

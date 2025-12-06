import schedule
import time
from .weather_service import fetch_weather
import threading

def start_scheduler():
    schedule.every(1).hours.do(fetch_weather)

    def run():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()

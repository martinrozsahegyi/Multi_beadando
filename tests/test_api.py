import requests

BASE = "http://127.0.0.1:8000/weather"

def test_latest_status_code():
    r = requests.get(f"{BASE}/latest")
    assert r.status_code == 200

def test_history_status_code():
    r = requests.get(f"{BASE}/history")
    assert r.status_code == 200

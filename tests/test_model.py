from backend.models.weather_model import Weather

def test_weather_model_fields():
    w = Weather(city="TestCity", temperature=25.5, description="clear sky")
    assert w.city == "TestCity"
    assert w.temperature == 25.5
    assert w.description == "clear sky"

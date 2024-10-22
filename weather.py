import requests
import config

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.OPENWEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

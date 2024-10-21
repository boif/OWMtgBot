import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("API_TOKEN")
OPENWEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

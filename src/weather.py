import os
import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

def get_temperature(city="Stuttgart", cache_file="weather_cache.json"):
    """
    Retrieves the current temperature in Celsius for the specified city.
    Caches the result for 24 hours to avoid exceeding API usage limits.
    """
    # Check for cached result
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            cache = json.load(f)
            timestamp = datetime.fromisoformat(cache["timestamp"])
            if datetime.now() - timestamp < timedelta(hours=24):
                return cache["temp"]
    
    # Make API request if no valid cache
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()
    temp = data["main"]["temp"]

    # Save response to cache
    with open(cache_file, "w") as f:
        json.dump({"temp": temp, "timestamp": datetime.now().isoformat()}, f)
    
    return temp

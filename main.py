# Entry point for the Stuttgart weather outfit predictor

from src.weather import get_temperature
from src.logic import outfit_recommendation

if __name__ == "__main__":
    temp = get_temperature("Stuttgart")
    result = outfit_recommendation(temp)
    print(f"{temp}°C in Stuttgart → Recommendation: {result}")

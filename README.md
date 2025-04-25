Stuttgart Weather Outfit Predictor
This Python project predicts what to wear based on the current weather in Stuttgart, Germany.
It uses the OpenWeatherMap API to fetch live temperature data and classifies the result into three outfit categories.

## 🔍 Example Output
18.5°C in Stuttgart → Recommendation: T-Shirt + Pullover

## 🚀 Features
Live weather data from OpenWeatherMap API

API call caching to stay under free-tier limits (max 100/day)

Simple, modular architecture with clean separation of logic

Easy to extend (more cities, weather features, web interface, etc.)

## 🛠️ How to Run
Clone the repository:
```bash
git clone https://github.com/JenzenBenzen/stuttgart-weather-outfit-predictor.git
cd stuttgart-weather-outfit-predictor
```
Create and activate a virtual environment:
```bash
python -m venv env
```
Then, in Git Bash:
```bash
source env/Scripts/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```
Create a .env file and insert your API key:
```bash
OPENWEATHER_API_KEY=your_api_key_here
```
Make sure this file is listed in .gitignore to avoid leaking your key.

Run the application:
```bash
python main.py
```
## 📁 Project Structure
stuttgart-weather-outfit-predictor/
├── data/ (optional: for storing historical data)
├── notebooks/ (optional: for experiments, visualizations)
├── src/
│ ├── logic.py (outfit logic)
│ └── weather.py (API + caching)
├── main.py (entry point)
├── .env 
├── .gitignore
├── requirements.txt
└── README.md

## 📌 License

MIT License — use it, modify it, ship it. 
Just don’t blame me if it tells you to wear a T-shirt in troublesome weather.

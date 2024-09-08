import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, abort
import datetime
from pathlib import Path

app = Flask(__name__)

# Load environment variables
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

# Retrieve the API key from .env
OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

# Route the index.html file to the root URL
@app.route('/', methods=['POST', 'GET'])
def weather():
    city_name = None
    if request.method == 'POST':
        city_name = request.form.get('city_name')

    # API URL
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=imperial&appid={OPEN_WEATHER_API_KEY}'

    # Make the request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # 5-day forecast data
        forecast_data = []
        current_date = datetime.datetime.now()

        # forecast for each day
        for i in range(0, 40, 8):
            weather_data = data["list"][i]

            # iterate through the next 5 days
            weather_forecast = {
                "date": current_date.strftime('%A, %B %d'),
                "temp": "{0:,.2f}".format(weather_data["main"]["temp"]),
                "feels_like": "{0:,.2f}".format(weather_data["main"]["feels_like"]),
                "temp_low": "{0:,.2f}".format(weather_data["main"]["temp_min"]),
                "temp_high": "{0:,.2f}".format(weather_data["main"]["temp_max"]),
                "humidity": weather_data["main"]["humidity"],
                "description": weather_data["weather"][0]["description"],
                "icon": weather_data["weather"][0]["icon"]
            }

            forecast_data.append(weather_forecast)
            current_date += datetime.timedelta(days=1)

        return render_template(
            'index.html', forecast_data=forecast_data, city_name=city_name)
    else:
        # city not found or error with API
        return abort(404, description="City not found or error fetching weather data.")


if __name__ == '__main__':
    app.run()

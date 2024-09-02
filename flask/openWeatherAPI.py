import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

# Define the location
city_name = input("Enter the city name: ")
country = "US"

# API URL
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=imperial&appid={OPEN_WEATHER_API_KEY}'

# Make the request to the API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("5-day Forecast:")
    for i in range(0, 40, 8):  
        day_data = data["list"][i]

        temp = day_data["main"]["temp"]
        feels_like = day_data["main"]["feels_like"]
        temp_min = day_data["main"]["temp_min"]
        temp_max = day_data["main"]["temp_max"]
        humidity = day_data["main"]["humidity"]

        formatted_temp = "{0:,.2f}".format(temp)
        formatted_feels_like = "{0:,.2f}".format(feels_like)
        formatted_temp_min = "{0:,.2f}".format(temp_min)
        formatted_temp_max = "{0:,.2f}".format(temp_max)

        print(f"Day {i//8 + 1}:")
        print(f"  Temp: {formatted_temp}°F")
        print(f"  Feels Like: {formatted_feels_like}°F")
        print(f"  Low: {formatted_temp_min}°F")
        print(f"  High: {formatted_temp_max}°F")
        print(f"  Humidity: {humidity}%")
        print()
else:
    # If the response was unsuccessful, print the status code
    print('Failed to retrieve data:', response.status_code)

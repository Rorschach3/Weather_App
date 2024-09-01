import requests
import os

city_name = 'Los Angeles'
API_Key = os.getenv(OPEN_WEATHER_API_KEY)

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&&units=imperial&appid={API_Key}'


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('temp:', data["main"]["temp"],'degrees Farenheit')

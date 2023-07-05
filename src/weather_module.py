import requests


def get_city_weather(city: str):
    city = 'Moscow'

    url = 'https://api.openweathermap.org/data/2.5/weather?\
    q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

    weather_data = requests.get(url).json()

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])

    print(f'Current temperature in {city} is {temperature} degrees Celcius')
    print(f'Feels like {temperature_feels}')
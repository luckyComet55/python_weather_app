import requests

__api_key__: str = '9964deeb468addac49d151062b0929e2'

def get_city_weather(city: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?\
        q={city}&units=metric&lang=ru&appid={__api_key__}'
    weather_data = requests.get(url).json()
    if weather_data['cod'] == 401:
        print(weather_data)
        return {
            'response_code': 500,
            'data': {
                'message': 'Internal error'
            }
        }
    elif weather_data['cod'] >= 400 and weather_data['cod'] < 500:
        print(weather_data)
        return {
            'response_code': 400,
            'data': {
                'message': f'Incorrect city name: city={city}'
            }
        }
    else:
        return {
        'response_code': 200,
        'data': weather_data
    }

def get_weather_hours(city: str, hours: int):
    url = f'https://api.openweathermap.org/data/2.5/forecast?\
        q={city}&units=metrics&lang=ru&appid={__api_key__}'
    weather_data = requests.get(url).json()
    if weather_data['cod'] == 401:
        return {
            'response_code': 500,
            'data': {
                'message': 'Internal error'
            }
        }
    elif weather_data['cod'] >= 400 and weather_data['cod'] < 500:
        return {
            'response_code': 400,
            'data': {
                'message': f'Incorrect city name: city={city}'
            }
        }
    else:
        return {
        'response_code': 200,
        'data': weather_data['list'][hours : hours + 1]
    }
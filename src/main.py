from fastapi import FastAPI, status, Response
from . import weather_module

app = FastAPI()

@app.get('/')
async def root():
    return 'OK'

@app.get('/weather_current')
async def get_weather(response: Response, city: str):
    res = weather_module.get_city_weather(city)
    response.status_code = res['response_code']
    return res['data']

@app.get('/weather_forecast')
async def get_weather_at(response: Response, city: str, time_to_hours: str):
    hours_accurate = time_to_hours // 3
    res = weather_module.get_weather_hours(city, hours_accurate)
    response.status_code = res['response_code']
    return res['data']
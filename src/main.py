from fastapi import FastAPI
from . import weather_module

app = FastAPI()

@app.get('/')
async def root():
    return {
        'message': 'To use out app, provide the name os the city in query'
    }
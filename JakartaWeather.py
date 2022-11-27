import numpy as np
from datetime import datetime
import requests
import matplotlib.pyplot as plt


BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
API_KEY = "ccfd5f316dbb5b43d3b9587a43aa7d74"
CITY = "1642911"


def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    str(celcius)
    return celcius


url = BASE_URL + "appid=" + API_KEY + "&id=" + CITY

response = requests.get(url).json()
listWeather = response['list']
jakartaWeather = []

for i in listWeather:
    date = datetime.utcfromtimestamp(i['dt']).strftime("%a, %d %b %Y: ")
    celcius = kelvin_to_celcius(i['main']['temp'])
    jakartaWeather.append(date+str(celcius)[:5]+" "+chr(176)+"C")

for x in jakartaWeather:
    print(x)

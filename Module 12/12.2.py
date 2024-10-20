import requests
import json

city = input(f'Pleae input a city name to get the weather condition:')
API_key = 'bd5e378503939ddaee76f12ad7a97608'
request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
response = requests.get(request).json()
print("Weather Description:", response["weather"][0]["description"])
print("Tempreture in Fahrenheit:",response["main"]["temp"] )
celsius_degrees = round(response["main"]["temp"] - 273.15)
print("Temperature in celsius:", celsius_degrees)

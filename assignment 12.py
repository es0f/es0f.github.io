#1
import requests
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print("random chuck norris joke:")
print(response["value"])
#2
import requests
api_key = "9e96ecc04915e1f92e4fd50ee0e0057b"
municipality = input("Enter Municipality: ")
request2 = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"
response = requests.get(request2).json()
temp_kelvin = response["main"]["temp"]
temp_celsius = temp_kelvin - 273.15
description = response["weather"][0]["description"]
print(f"\nWeather in {municipality}:")
print(f"Condition: {description}")
print(f"Temperature: {temp_celsius:.2f} °C")
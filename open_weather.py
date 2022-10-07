import requests
import json
from decouple import config

# calls in an api key that is generated from open weather platfrom
secret_key = config('api')

# the open weather url
open_weather_url = "https://api.openweathermap.org/data/2.5/weather?"

print("Welcome to this platform \nPlease Note that you can Enter your City Name to get information about the weather")
city_name = input("Enter Your City Name: ")

# build the url pointing to that city in the open weather platform
city_url = open_weather_url + "q=" + city_name + "&appid=" + secret_key

print(city_url)
# call the api url and get a respone
response = requests.get(city_url)

# format the data into a python json object
res = response.json()

# Check to see if the City exits
if res["cod"] != "404":
    tem_kv = res['main']['temp']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    tem_c = int(tem_kv) - 273.15

    print(
        f"Name of City: {res['name']}, In the Country : {res['sys']['country']}")
    print(
        f"Wind speed is {res['wind']['speed']} moving in the Degrees of {res['wind']['deg']}")
    print(
        f"Temperature in C : {tem_c} \n Humidity in %: {humidity} \n  Atmospheric pressure (in hPa unit): {pressure}\n")

    print(
        f"In short the Weather is {res['weather'][0]['main']} \n basically {res['weather'][0]['description']}")


else:
    print("Sorry we cant find your city")

import requests

api_key = "c8728ceb75d6d63673ef6306ae4d66e3"
city_name = input("Enter City: ")
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

r = requests.get(url)

print(r)
print(r.json())


temprature = r.json()['main']['temp']
pressure = r.json()['main']['pressure']
humidity = r.json()['main']['humidity']
description = r.json()['main']['weather'][0]["description"]

print("Temprature in Kelvin: ", temprature)
print("Pressure in hPa: ", pressure)
print("Humidity :", humidity)
print("Current Description : ", description)








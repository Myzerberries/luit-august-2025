import requests

city = "London"

url = 'http://api.weatherapi.com/v1/current.json?key=1f77cc8db2774ef5a3713432251408&q=' + city + '&aqi=no'

response = requests.get(url)

weather_json = response.json()

temp = weather_json.get('current').get('temp_f')

description = weather_json.get('current').get('condition').get('text')

#description2 = weather_json(['current'])

print ("Today's weather in" , city, "London is", description, "and", temp, "degrees")


#==================================================================
#
# GetWx.py:  Get the latest Weather Forcasst from OpenWeather
#             and format the output.
#             NB: This requires you to register with Open Weather Map
#              https://openweathermap.org and get an API Key
#
###################################################################
#
# Author: Andy Holmes (2E0IJC)
# Date:   17th November 2023
#
###################################################################


import requests

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

LOC = 'Killingworth Village'
LAT = '55.02974'
LON = '-1.54938'

url = f'http://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric'    #Forecast

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    #location = data['city']['name']
    #location = data['name']
    location = LOC
    
    weather = data['list'][0]['weather'][0]['description']
    temp = data['list'][0]['main']['temp']

    wind = data['list'][0]['wind']['speed']
    gust = data['list'][0]['wind']['gust']
    direction = data['list'][0]['wind']['deg']

    min_t = data['list'][0]['main']['temp_min']
    max_t = data['list'][0]['main']['temp_max']
    pressure = data['list'][0]['main']['pressure']
    humidity = data['list'][0]['main']['humidity']

    output1 = f'The weather in {location} is {weather} with a temperature of {temp} C.\n\n'
    output2 = f'\tMin Temperature: {min_t} C\t Max Temperature: {max_t} C\n'
    output3 = f'\tPressure: {pressure}mb\tHumidity: {humidity}%\n'
    output4 = f'\tWind: {wind}m/s\tGusting to {gust}m/s\tDirection: {direction}\n\n'
    
    print(output1 + output2 + output3 + output4)
else:
    print("Sorry but we're unable to retrieve the weather right now. Please try again later.")


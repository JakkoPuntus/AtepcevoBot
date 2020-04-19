import requests
import ast

url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

querystring = {"lang" : "ru", "cnt": "2", "units":"metric", "id":"523426"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "62acce0ea1mshf007f9b817ad5fcp190835jsndb975b7e65b0"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


result = ast.literal_eval(response.text)
#Погода на завтра
r1 = result['list'] 
r2 = r1[1]
r3 = r2['temp']
r4 = r3['day']
r5 = str(r4)
r31 = r2['weather']
r41 = r31[0]
r51 = r41['description']

#Погода на сегодня
w1 = result['list']
w2 = w1[0]
w3 = w2['temp']
w4 = w3['day']
w5 = str(w4)
w31 = w2['weather']
w41 = w31[0]
w51 = w41['description']


Weather = "Завтра " + r5 + " градусов, " + r51
WeatherToday = "Сегодня " + w5 + " градусов, " + w51
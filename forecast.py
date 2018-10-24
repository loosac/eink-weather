import requests
from pprint import pprint

ICON_URL='http://openweathermap.org/img/w/'

# city = input('Podaj miasto ')
city='Warszawa'
# URL='http://api.openweathermap.org/data/2.5/forecast?q={},pl&mode=json&units=metric&APPID=ef5ceef31ad2d20a5281715b3d1b6b88'.format(city)
URL = 'http://api.openweathermap.org/data/2.5/weather?q={},pl&mode=json&units=metric&APPID=ef5ceef31ad2d20a5281715b3d1b6b88'.format(
    city)

print(URL)

res = requests.get(URL)

data=res.json()

temperatura = data['main']['temp']
wiatr_pred = data['wind']['speed']
wiatr_kier = data['wind']['deg']

ikona = data['weather'][0]['icon']
icon_url='http://openweathermap.org/img/w/{}.png'.format(ikona)

print('Aktualna temperatura: {}'.format(temperatura))
print(icon_url)

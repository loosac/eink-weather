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

progn_data=res.json()

progn_temp = progn_data['main']['temp']
progn_wiatr_pred = progn_data['wind']['speed']
progn_wiatr_kier = progn_data['wind']['deg']

progn_ikona = progn_data['weather'][0]['icon']
icon_url='http://openweathermap.org/img/w/{}.png'.format(progn_ikona)

print('Aktualna temperatura: {}'.format(progn_temp))
print(icon_url)

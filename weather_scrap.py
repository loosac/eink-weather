import requests
from bs4 import BeautifulSoup
#import csv


urlcam='https://www.traxelektronik.pl/pogoda/kamery/kamera.php?pkamnum='
urlmeteo='https://www.traxelektronik.pl/pogoda/stacja/stacja.php?stid='

kopytow_id = 141
pulawska_id = 138

url_kopytow = urlcam + str(kopytow_id)

proxies = {
  'http': 'http://xproxy.i:8090',
  'https': 'http://xproxy.i:8090',

}

r=requests.get(url_kopytow)

soup = BeautifulSoup(r.content,'html.parser')

table = soup.find('table')
rows = table.findAll('tr')
# print(rows)

dane = {}
for tr in rows:
    cells=tr.findAll('td')
    if len(cells)>1:
        parametr = cells[0]
        wartosc = cells[1]
        print("Wiersz:  {0} {1} ".format(parametr, wartosc))
    # print(cells)

# inmates_list = []
#
# for table_row in soup.select("table.inmatesList tr"):
#     cells = table_row.findAll('td')
#     if len(cells) > 0:
#         parametr = cells[0].text.strip()
#         wartosc =  cells[1].text.strip()
#         inmate = {'parametr': parametr, 'wartosc': wartosc}
#         inmates_list.append(inmate)
#         print ("Added {0} {1} to the list".format(parametr, wartosc))

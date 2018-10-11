import datetime
import requests
from bs4 import BeautifulSoup

URL='http://www.pogodynka.pl/polska/prognoza_synoptyczna/warszawa_warszawa'

# tab = soup.find("table",{"class":"wikitable sortable"})

def pobierzProg():
    r=requests.get(URL)
    tresc=r.content
    soup = BeautifulSoup(tresc, 'html.parser')
    # tab = soup.find("table", {"class": "synopy"})[1]
    tab = soup.findAll("table", {"class": "synopy"})[1]
    # dzis
    row1 = tab.findAll('tr', {"class": "k1"})
    # jutro
    row2 = tab.findAll('tr', {"class": "k2"})
    # po jutrze
    row3 = tab.findAll('tr', {"class": "k3"})

    return row1
    # wynik = []
    # for tr in rows:
    #     cells = tr.findAll('td')
    #     if len(cells) > 1:
    #         wynik.append(cells[0])
    #         wynik.append(cells[1])
    #
    #         # wynik.append(cells[3].get_text().strip())
    # return (wynik)


print(pobierzProg())
# r = requests.get(URL)
# soup = BeautifulSoup(r, 'html.parser')



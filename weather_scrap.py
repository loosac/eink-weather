import datetime
import requests
import PIL

from bs4 import BeautifulSoup


urlcam='https://www.traxelektronik.pl/pogoda/kamery/kamera.php?pkamnum='
urlmeteo='https://www.traxelektronik.pl/pogoda/stacja/stacja.php?stid='

kopytow_id = 141
pulawska_id = 138

url_kopytow = urlcam + str(kopytow_id)

x = datetime.datetime.now()

# pobieramy dane o lokalizacji, zwracamy liste
def pobierzCam(url_id,label):

    print(x)
    wynik=[x , label]

    # print('Pobieram {0}'.format(label))
    r=requests.get(urlcam+str(url_id))
    soup = BeautifulSoup(r.content.decode('iso8859-2').encode('utf-8'), 'html.parser')
    table = soup.find('table')
    rows = table.findAll('tr')
    # print(rows)

    dane = {}
    for tr in rows:
        cells=tr.findAll('td')
        if len(cells)>1:
            parametr = cells[0].get_text()
            # stripujemy z whitespaceow na poczatku linii
            wynik.append(cells[1].get_text().strip())
            # print("Wiersz:  {0} {1} ".format(parametr, wartosc))
            #print(":{1}".format(parametr, wartosc))
    return (wynik)

def rysujobraz():
    EPD_WIDTH = 640
    EPD_HEIGHT = 384
    obraz = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)  # 1: clear the frame
    draw = ImageDraw.Draw(obraz)
    # czcionki
    f_ = ImageFont.truetype('fontit/ClearSans-Regular.ttf', 18)
    f_iso = ImageFont.truetype('fontit/unispace.ttf', 44)
    f_symbol_p = ImageFont.truetype('fontit/WeatherIcons.ttf', 40)


print(pobierzCam(141,'Kopytow'))
print(pobierzCam(138,'Pulawska'))
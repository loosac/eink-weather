import datetime
import requests
import socket

# import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from bs4 import BeautifulSoup



#Margines na informacje biezace: date, godzine
MARG_X = 5
MARG_Y = 84
EPD_WIDTH = 640
EPD_HEIGHT = 384

urlcam='https://www.traxelektronik.pl/pogoda/kamery/kamera.php?pkamnum='
urlmeteo='https://www.traxelektronik.pl/pogoda/stacja/stacja.php?stid='

kopytow_id = 141
pulawska_id = 138

obraz_name ='output.jpg'
obr_powietrze='_ikony/powietrze.jpg'
obr_asfalt='_ikony/droga.jpg'
obr_sucha='_ikony/sucha.jpg'
obr_mokra='_ikony/mokra.jpg'
obr_szklanka='_ikony/ryzyko_lodu.jpg'
ikona_sieci='_ikony/net-disconnected.jpg'
url_kopytow = urlcam + str(kopytow_id)

x = datetime.datetime.now()
dzientyg="Poniedzialek","Wtorek","Sroda","Czwartek","Piatek","Sobota","Niedziela"
miesiac="null","Styczen","Luty","Marzec","Kwiecien","Maj","Czerwiec","Lipiec","Sierpien","Wrzesien","Pazdziernik","Listopad","Grudzien"
# tuntinronyt = int(datetime.datetime.now().strftime('%H'))
tuntinronyt = int(x.strftime('%H'))
godzina = str(x.strftime('%H'))+':'+str(x.strftime('%M'))

#zmienna is_connected


def czy_podlaczony():
    try:
        r = requests.get('http://www.google.com/')
        r.raise_for_status()
        return True
    except requests.exceptions.HTTPError as err:
        return False


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# pobieramy dane o lokalizacji, zwracamy liste
def pobierzCam(url_id,label):

    # print(x)
    wynik=[label]

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
    elementy=[[141,"Kopytów"],[138,"Puławska"]]
    parametry = []

    obraz = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)  # 1: clear the frame
    draw = ImageDraw.Draw(obraz)
    # czcionki
    f_ = ImageFont.truetype('_ttf/OpenSans-Light.ttf', 15)
    f_temp = ImageFont.truetype('_ttf/OpenSans-Light.ttf', 20)

    f_cyfr = ImageFont.truetype('_ttf/ds_digi.ttf', 60)

    f_iso = ImageFont.truetype('_ttf/OpenSans-Light.ttf', 40)
    # f_symbol_p = ImageFont.truetype('fontit/WeatherIcons.ttf', 40)

    for x in elementy:
        # print(x)
        # print("----")
        parametry.append(pobierzCam(x[0],x[1]))

    if is_connected == True:
        ikona_sieci='_ikony/net-connected.jpg'

    stan_sieci_img=Image.open(ikona_sieci,'r')
    obraz.paste(stan_sieci_img, (int(EPD_WIDTH-50), int(EPD_HEIGHT - 50)))

    # print(parametry)
    if(len(parametry)==2):
        print("poprawna liczba parametrow")
    powietrze = Image.open(obr_powietrze,'r')
    asfalt = Image.open(obr_asfalt,'r')

    xpos=5
    for stacja in parametry:
        draw.text((xpos, MARG_Y + 10), "  "+str(stacja[0]), font=f_)
        draw.text((xpos+80, MARG_Y + 80), str(stacja[1]), font=f_temp)
        obraz.paste(powietrze, (int(xpos), int(MARG_Y + 50)))

        draw.text((xpos+80, MARG_Y + 130), str(stacja[2]), font=f_temp)
        obraz.paste(asfalt, (int(xpos), int(MARG_Y + 100)))
        draw.text((xpos, MARG_Y + 180), "Jezdnia " + str(stacja[4]), font=f_)
        tempstring=str(stacja[1])
        tempfloat=float(tempstring[0:len(tempstring)-2])


        print(tempfloat)
        if (str(stacja[4]) == "sucha"):
            sucha = Image.open(obr_sucha, 'r')
            obraz.paste(sucha, (int(xpos), int(MARG_Y + 200)))
        else:
            mokra = Image.open(obr_mokra, 'r')
            obraz.paste(mokra, (int(xpos), int(MARG_Y + 200)))

        if(tempfloat <= 1):
            szklanka = Image.open(obr_szklanka, 'r')
            obraz.paste(szklanka, (int(xpos)+80, int(MARG_Y + 200)))

        # draw.text((xpos, MARG_Y + 200), "Sezdnia: "+str(stacja[4]), font=f_temp)
        xpos=EPD_WIDTH/4+5

    # Linie:
    # linia oddzielajaca gorny panel od reszty
    draw.line((MARG_X,MARG_Y,EPD_WIDTH-MARG_X,MARG_Y),fill=0)

    #linia dzielaca prognoze od odczytow GDDKiA
    draw.line((EPD_WIDTH/2, MARG_Y, EPD_WIDTH/2, EPD_HEIGHT), fill=0)

    #linia rozdzielajaca stacje pomiarowe
    draw.line((EPD_WIDTH / 4, MARG_Y, EPD_WIDTH / 4, EPD_HEIGHT), fill=0)


    # Prostokat z kalendarzem
    draw.rectangle((MARG_X, 20, MARG_X+100, MARG_Y))
    draw.rectangle((MARG_X, 0, MARG_X+100, 30), fill=0)

    draw.text((10, 0), miesiac[int(datetime.datetime.now().strftime('%-m'))], font=f_, fill=255)
    # draw.rectangle((0, 20, 100, 80))
    draw.text((44, 20), datetime.datetime.now().strftime('%-d'), font=f_iso, fill=0)
    draw.text((9, 60), dzientyg[datetime.datetime.now().weekday()], font=f_, fill=0)

    # Prostokat z godzina
    draw.text((EPD_WIDTH-150, 10), godzina, font=f_cyfr)


    draw.text((EPD_WIDTH/2+5, MARG_Y+10), "Prognoza Warszawa:", font=f_)

    draw.text((EPD_WIDTH / 2 + 5, EPD_HEIGHT-30 ), "Adres IP: {}".format(get_ip()), font=f_)
    obraz.save(obraz_name)


# Pierwsze 84 px od gory czesc techniczna

def rysujCzas():
    print("")



is_connected = czy_podlaczony()


rysujobraz()


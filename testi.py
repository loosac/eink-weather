# -*- coding: utf-8 -*-

import epd7in5
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
from bs4 import BeautifulSoup
import urllib2
#from ruuvitag_sensor.ruuvitag import RuuviTag



#näytön alustus
EPD_WIDTH = 640
EPD_HEIGHT = 384
epd = epd7in5.EPD()
epd.init()
obraz = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
draw = ImageDraw.Draw(obraz)


#muuttujat
dzientyg="Poniedzialek","Wtorek","Sroda","Czwartek","Piatek","Sobota","Niedziela"
miesiac="null","Styczen","Luty","Marzec","Kwiecien","Maj","Czerwiec","Lipiec","Sierpien","Wrzesien","Pazdziernik","Listopad","Grudzien"
tuntinronyt = int(datetime.datetime.now().strftime('%H'))

vrkmax=-100
vrkmin=100
yomin=100

sadevrk=0
sadeyo=0

huomen=0
onetime=0

y=34
vrkh=0
i=0
x=110



#fontit
f_ = ImageFont.truetype('fontit/ClearSans-Regular.ttf', 18)
f_iso = ImageFont.truetype('fontit/unispace.ttf', 44)
f_symbol_p = ImageFont.truetype('fontit/WeatherIcons.ttf', 40)




# lämpötilannyt
draw.text((x, y-20), "Kolumna1", font=f_, fill=0)
draw.text((x + 170, y-20), "Kolumna2", font=f_, fill=0)
draw.text((x + 380, y-20), "Kolumna3", font=f_, fill=0)

#********* Piirtely alkaa
#Vasen palkki
draw.rectangle((0, 0,100,20),fill=0)
draw.text((10, 0), miesiac[int(datetime.datetime.now().strftime('%-m'))], font=f_, fill=255)
draw.rectangle((0, 20,100,80))
draw.text((19, 20), datetime.datetime.now().strftime('%-d'), font=f_iso, fill=0)
draw.text((9, 60),dzientyg[datetime.datetime.now().weekday()], font=f_, fill=0)
draw.text((2, 80), "Aurinko", font = f_, fill = 0)
draw.text((2, 130), "Min / Max", font = f_, fill = 0)
draw.text((2, 180), "Sade", font = f_, fill = 0)
draw.text((2, 230), "Nimpparit", font = f_, fill = 0)
nimiy=250

draw.line((450, 0, 450,384), fill=0)
draw.line((270, 0, 270,384), fill=0)
#tallennetaan obraz levylle ja näyttöön
obraz.save("test.jpg")
epd.display_frame(epd.get_frame_buffer(obraz))



import epd7in5
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime

EPD_WIDTH = 640
EPD_HEIGHT = 384
epd = epd7in5.EPD()
epd.init()
obraz = Image.open("tresc.jpg")

epd.display_frame(epd.get_frame_buffer(obraz))



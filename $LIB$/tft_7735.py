#From boochow/ST7735.py
#from ST7735 import TFT,TFTColor
from machine import Pin,SPI
from PRECONFIG import LCD_SIZE
#from PRECONFIG import TFT_SPI

import time
spi=SPI(1,sck=Pin(2),mosi=Pin(3),miso=Pin(10),baudrate=60000000)#OPTIONAL
#tft=TFT(spi,6,10,7)
#tft.initg()
#tft.rotation(2)
#tft.rgb(True)
dc=Pin(6, Pin.OUT, Pin.PULL_DOWN)
reset=Pin(10, Pin.OUT, Pin.PULL_DOWN)
cs=Pin(7, Pin.OUT, Pin.PULL_DOWN)
_size=LCD_SIZE#Screen Size
#col = bytearray(2)


def fill(c=bytes(2)):
    setarea((0,0),(_size[0]-1,_size[1]-1))
    dc(1)
    for i in range(_size[1]):spi.write(_size[0]*c)

def _reset() :
    dc(0)
    reset(1)
    time.sleep_us(500)
    reset(0)
    time.sleep_us(500)
    reset(1)
    time.sleep_us(500)

from st_common import *
invert=lambda b:com(32+b%2)
init=lambda:exec(open('tft_init_7735.py').read(),{'com':com,'area':area,'dat':dat,'dc':dc,'cs':cs,'_reset':_reset,'_size':_size})
init()


'''
TO DO:
rotation
gu gu gu ~
'''
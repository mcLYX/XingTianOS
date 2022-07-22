#From boochow/ST7735.py
#from ST7735 import TFT,TFTColor
from machine import Pin
from PRECONFIG import TFT_SPI
import time
spi=TFT_SPI
#tft=TFT(spi,6,10,7)
#tft.initg()
#tft.rotation(2)
#tft.rgb(True)
dc=Pin(6, Pin.OUT, Pin.PULL_DOWN)
reset=Pin(10, Pin.OUT, Pin.PULL_DOWN)
cs=Pin(7, Pin.OUT, Pin.PULL_DOWN)
_size=(128,160)#Screen Size
#col = bytearray(2)
area = bytearray(4)
_offset=bytearray(2)

def setarea(aPos0, aPos1 ) :
    com(42)            #Column address set.
    area[0] = _offset[0]
    area[1] = _offset[0] + int(aPos0[0])
    area[2] = _offset[0]
    area[3] = _offset[0] + int(aPos1[0])
    dat(area)

    com(43)            #Row address set.
    area[0] = _offset[1]
    area[1] = _offset[1] + int(aPos0[1])
    area[2] = _offset[1]
    area[3] = _offset[1] + int(aPos1[1])
    dat(area)

    com(44)            #Write to RAM.

_setwindowloc=setarea

invert=lambda b:com(32+b%2)

def fill(c=bytes(2)):
    setarea((0,0),(_size[0]-1,_size[1]-1))
    dc(1)
    for i in range(_size[1]):spi.write(_size[0]*c)
    
def com(aCommand ) :
    dc(0)
    #cs(0)
    spi.write(bytearray([aCommand]))
    #cs(1)

  #@micropython.native
def dat(aData ) :
    dc(1)
    #cs(0)
    spi.write(aData)
    #cs(1)

def _reset() :
    dc(0)
    reset(1)
    time.sleep_us(500)
    reset(0)
    time.sleep_us(500)
    reset(1)
    time.sleep_us(500)

init=lambda:exec(open('tft_init.py').read(),{'com':com,'area':area,'dat':dat,'dc':dc,'cs':cs,'_reset':_reset,'_size':_size})
init()

'''
TO DO:
rotation
gu gu gu ~
'''
from machine import Pin, SPI
from PRECONFIG import LCD_SIZE
import st7789

TFA = 0
BFA = 80
reset=Pin(34, Pin.OUT)
dc=Pin(33, Pin.OUT)
spi=SPI(2, baudrate=800000000, polarity=1, sck=Pin(36), mosi=Pin(35))
def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        spi,
        *LCD_SIZE,
        reset=reset,
        dc=dc,
        rotation=rotation,
        options=options,
        buffer_size=buffer_size)

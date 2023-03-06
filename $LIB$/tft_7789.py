# Required st7789_mpy library
import tft_config_7789 as cfg
import config
from PRECONFIG import LCD_SIZE
spi=cfg.spi
dc=cfg.dc
reset=cfg.reset
rot=int(config.read('Rot'))
tft=cfg.config(rot)
tft.init()
from st_common import *
import st_common as st
invert=lambda b:com(33-b%2)
def setOffset(rot=rot):
    if rot==2:st.offset=bytearray([240-LCD_SIZE[0],320-LCD_SIZE[1]])
    elif rot==3:st.offset=bytearray([320-LCD_SIZE[0],240-LCD_SIZE[1]])
    else:st.offset=bytearray(2)
setOffset()
def fill(c=bytes(2)):tft.fill((c[0]<<8)+c[1])
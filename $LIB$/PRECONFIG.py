#移植到其他板子上要改这个
#PRECONFIG SCRIPT FOR ESP32C3
from machine import SPI,Pin,I2C,ADC
OLED_I2C=I2C(0,scl=Pin(5),sda=Pin(4),freq=1110000)
TFT_SPI=SPI(1,sck=Pin(2),mosi=Pin(3),miso=Pin(10),baudrate=60000000)#OPTIONAL
ADC_PIN=ADC(Pin(0))
ADC_PIN.atten(ADC.ATTN_11DB)
TQ_VOLT=16383
CPU_FREQ=160000000

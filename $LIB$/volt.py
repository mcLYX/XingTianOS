from PRECONFIG import ADC_PIN
from machine import Pin,ADC
import time
volt=ADC_PIN.read_u16
def volt(samp=0,delay=500):
    if samp:
        value=0
        for i in range(samp):
            value+=ADC_PIN.read_u16()
            time.sleep_us(delay)
        return value/samp
    else:
        return ADC_PIN.read_u16()
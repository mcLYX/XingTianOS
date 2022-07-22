from volt import volt
from machine import ADC,Pin
y=ADC(Pin(1))
y.atten(ADC.ATTN_11DB)
b=Pin(12,Pin.IN)
#m为假时返回原始值
def jstk(m=1):return ( volt()//21846-1 if m else volt() ),( y.read_u16()//21846-1 if m else volt() ),( not b.value() )
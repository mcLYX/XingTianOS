from scr import s,f,r,m,_
from math import sin,pi,cos
from time import ticks_ms as ms
spd=250
t=ms()
while ms()-t<spd:
    pos=64-int(cos((ms()-t)/spd*pi/2)*64)
    m(0,pos);_(0,0,128,pos,0);s();m(0,-pos)
    print(pos)
t=ms()
while ms()-t<spd:
    i=64-int(sin((ms()-t)/spd*pi/2)*64)
    f(0);r(9,24+i,48,48,1);r(40,16+i,48,48,1);r(71,24+i,48,48,1);_(41,17+i,46,46,0);_(40,i,48,9,1);s()
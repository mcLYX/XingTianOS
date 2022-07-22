import scr,lstui,touch
from math import *
from dscn import *
fx,zone=[],.5
while 1:
  scr.f(0);dscd([345,857,14]*2+['...']);scr.s();scr.f(0)
  scr.h(0,31,128,1);scr.v(63,0,64,1)
  for i in fx:
    for j in range(128):
      try:
        global x
        x=zone*(j-63)
        y1=int(eval(i)/zone)
        x+=zone
        y2=int(eval(i)/zone)
        scr.l(int(x/zone+62),31-y1,int(x/zone+63),31-y2,1)
      except:
        pass
  scr.s()
  if touch.prstime():
    sel=lstui.lstui(([2234,920,2219],[1859,1389],[1002,29],[2357,34],[1694,494],[1381,293,'...']),[12,657,857,848],0)[1]
    if sel==0:
      fx.append(lstui.ime())
    elif sel==1:
      fx=[]
    elif 1<sel<4:
      zone*=2 if sel==3 else .5
    elif sel==4:
      fx.append(lstui.lstui(('-x','x**2','x*sin(x)','cos(x)','sin(x)+cos(x)','1/x'),'f(x)=',0)[0])
    else:
      break
  elif fx:
    lstui.lstui(fx,[920,2219])
del fx,zone

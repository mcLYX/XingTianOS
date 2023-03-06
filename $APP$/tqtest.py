from scr import s,t,f,l
from volt import volt
import touch,time
from machine import Pin, PWM
a=[]
mode=touch.d()

while 1:
  v=volt()
  a.append(v)
  if not mode:
    f(0)
    t('Value:'+str(v),0,9)
  elif mode and len(a)<128:continue
  if len(a)>128:
    del a[0]
  for i in range(len(a)-1):
    l(i,63-int(a[i]/1024),i+1,63-int(a[i+1]/1024),1)
  if v>767 and not mode:
    t('Touch Detected!',0,0)
  s()
  if mode:a=[];f(0)
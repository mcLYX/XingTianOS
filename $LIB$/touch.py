from PRECONFIG import TQ_VOLT
import volt,machine,scr;from time import sleep,ticks_ms

d=lambda:volt.volt()>=TQ_VOLT
detect=d

if 65535>volt.volt()>TQ_VOLT*1.1:
    scr.f(0)
    posbak=scr.pos
    scr.t('JoyStick Ready',8,0)
    scr.pos=(0,0),(127,63)
    scr.s()
    scr.pos=posbak
    del posbak
    sleep(1)
    import jstk
    def d():return max(jstk.jstk())
    detect=d

def prstime():
  prs=0
  while d():
    sleep(.088)
  t=ticks_ms()
  while d()==0:
    sleep(.088)
    '''if ticks_ms()-t>60000:
      scr.f(0)
      scr.s()
      machine.deepsleep()'''
  while 1:
    prs+=1;sleep(.088);print(prs)
    if d()==0 or prs>5:
      return prs>5
'''
try:
  import volt,machine,scr;from time import sleep,ticks_ms
except:
  detect,prstime=print,input
'''
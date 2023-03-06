from PRECONFIG import TQ_VOLT
import machine,scr,volt;from time import sleep,ticks_ms
from config import read

jit=[]
#d=lambda s=0:volt.volt(s)>=TQ_VOLT
def d(j=int(read('AntiJoggle')),s=0):
    if j:
        jit.append(volt.volt())
        if len(jit)>j:del jit[0]
        return (sum(jit)//j>=TQ_VOLT and jit[-1]>=TQ_VOLT)
    return volt.volt(s)>=TQ_VOLT
detect=d

def prstime():
  prs=0
  while d():
    sleep(.01)
  t=ticks_ms()
  while d()==0:
    sleep(.01)
  while 1:
    prs+=1;sleep(.09);print(prs)
    if d()==0 or prs>5:
      return prs>5
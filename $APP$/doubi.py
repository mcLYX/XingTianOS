#草，duobi（躲避）打成doubi了，不管了MD
from scr import _,r,s,t,f,color,i
from time import ticks_ms as tm
from time import sleep
from jstk import jstk
from rd import rdi
pos=[60,28]
#barrier=[]
HP=1
score=0
'''
f(0)
t('PLZ WAIT',0,0)
s()
'''
spd=1
#sleep(5)
while HP:
  f(0)
  bar=[rdi(0,96),rdi(0,48),rdi(32,96),rdi(24,64)]
  col=color(rdi(128,255),rdi(128,255),rdi(128,255))
  ti=tm()
  while tm()-ti<1000-min(score,500):
    t2=tm()
    f(0)
    pos[0]+=jstk()[0]*spd
    pos[1]+=jstk()[1]*spd
    pos[0]=min(120,pos[0])
    pos[0]=max(0,pos[0])
    pos[1]=min(60,pos[1])
    pos[1]=max(0,pos[1])
    _(bar[0],bar[1],bar[2],bar[3],col)
    r(int(pos[0]+.5),int(pos[1]+.5),8,8,1)
    t(str(score),0,0)
    t(str(pos),0,56)
    s()
    spd=(tm()-t2)/10
  if not (bar[1]+bar[3]<pos[1] or pos[1]+8<bar[1] or pos[0]>bar[0]+bar[2] or bar[0]>pos[0]+8):
    i(1)
    sleep(1)
    i(0)
    f(0)
    t('SCORE:'+str(score),0,0)
    s()
    sleep(2)
    break
  else:
    score+=1
  #if n2y+n2h<n1y or n1y+n1h<n2y or n1x>n2x+n2w or n2x>n1x+n1w

import touch,lstui,pbmds,math,time
from scr import s,f,t,_,l,b
from machine import RTC
r,p=RTC(),pbmds.ds
with open('num.pbm','rb') as fi:
  fi.readline();fi.readline()
  num=pbmds.getfb(fi,20,341)
exec(open('tsync.py').read(),{})
def pointer():
  global r,f,t,l,math
  N,Y,R,Z,S,F,M,U=r.datetime()
  f(0);t(str(N)+'/'+str(Y)+'/'+str(R),0,45);t(str(S)+':'+str(F)+':'+str(M),0,54)
  l(103,23,int(103+math.sin((S+F/60)*math.pi/6)*16),int(23-math.cos((S+F/60)*math.pi/6)*16),1)
  l(103,23,int(103+math.sin(F*math.pi/30)*21),int(23-math.cos(F*math.pi/30)*21),1)
  l(103,23,int(103+math.sin(M*math.pi/30)*24),int(23-math.cos(M*math.pi/30)*24),1)
def digital():
  global r,f,b,_,t,num
  N,Y,R,Z,S,F,M,U=r.datetime()
  f(0)
  for i in (1,45,89):_(i-1,12,40,36,1)
  b(num,0,13-S//10*34)
  b(num,19,13-S%10*34)
  b(num,44,13-F//10*34)
  b(num,63,13-F%10*34)
  b(num,88,13-M//10*34)
  b(num,107,13-M%10*34)
  _(0,0,128,13,0);_(0,48,128,16,0)
  t(str(N)+'/'+str(Y)+'/'+str(R),0,55)

style=1
while 1:
  digital() if style else pointer()
  s()
  time.sleep(.1)
  if touch.detect():
    if lstui.qna([[2213,900,616,1229]],[[494,2197,'...'],[380,611]]):
      sel=lstui.lstui([[380,611],[99,1447,1473,311],[1381,293,'...']],[616,1229,494,2197],0)[1]
      if sel==1:
        style=0 if style else 1
      if sel==2:
        break
    exec(open('tsync.py').read(),{})
del r,p,pointer,digital,num

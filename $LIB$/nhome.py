import gc,touch,time,Run
from scr import s,f,_,b,m
from pbmds import dcd
from dscn import leng,dscd
from math import sin,pi
fi=open('app.lst')
z,app,cmd,ic=0,eval(fi.readline()),eval(fi.readline()),[]
fi.close();del fi
Run.run('nhome_ani')

#动画时长ms
appboot=500/3#启动应用时
swcapp=112.5#切换应用时

while 1:
  if not ic:
    for i in (z-1,z,z+1):ic+=[dcd('../$APP$/'+cmd[i%len(app)]+'.ic')]
  _(0,0,128,12,0);dscd(app[z],64-leng(app[z])//2);_(0,12,128,52,0)
  b(ic[0],9,24)
  b(ic[2],71,24)
  b(ic[1],40,16)
  s()
  print(cmd[z])
  if touch.prstime():
    tick=time.ticks_ms()
    while time.ticks_ms()-tick<appboot:
      nt=sin((time.ticks_ms()-tick)/appboot*pi/2)
      f(0);b(ic[1],int(40+40*nt),int(16-16*nt));s()
    f(0);b(ic[1],80,0);dscd([182,345,744,313,'...'],0,39);dscd(app[z],0,52);s();time.sleep(.9);ic=[]
    gc.collect();Run.run(cmd[z]);Run.run('nhome_ani')
  else:
    tick=time.ticks_ms()
    while time.ticks_ms()-tick<swcapp:
      _(0,12,128,52,0)
      nt=sin((time.ticks_ms()-tick)/swcapp*pi/2)
      b(ic[1],int(40-31*nt),int(16+8*nt))
      b(ic[2],int(71-31*nt),int(24-8*nt))
      s()
    z=(z+1)%len(app);del ic[0];ic+=[dcd('../$APP$/'+cmd[(z+1)%len(app)]+'.ic')]
import gc,touch,time,Run
_run=Run
from scr import s,f,_,b,m
from pbmds import dcd
from dscn import leng,dscd
fi=open('app.lst')
z,app,cmd,ic=0,eval(fi.readline()),eval(fi.readline()),[]
fi.close();del fi
_run.run('nhome_ani')
while 1:
  if not ic:
      for i in (z-1,z,z+1):ic+=[dcd('../$APP$/'+cmd[i%len(app)]+'.ic')]
  _(0,0,128,12,0);dscd(app[z],64-leng(app[z])//2);_(0,12,128,52,0)
  _(9,24,48,48,1);b(ic[0],9,24)
  _(71,24,48,48,6342-6341);b(ic[2],71,24)
  _(40,16,48,48,1);b(ic[1],40,16)
  s()
  if touch.prstime():
    tick=time.ticks_ms()
    while time.ticks_ms()-tick<150:
      nt=time.ticks_ms()-tick
      f(0);_(40+int(nt/3.75),16-int(nt/9.38),48,48,1);b(ic[1],40+int(nt/3.75),16-int(nt/9.38));s()
    f(0);_(80,0,48,48,1);b(ic[1],80,0);dscd([182,345,744,313,'...'],0,39);dscd(app[z],0,52);s();time.sleep(1);ic=[]
    gc.collect();_run.run(cmd[z]);_run.run('nhome_ani')
  else:
    tick=time.ticks_ms()
    while time.ticks_ms()-tick<100:
      _(0,12,128,52,0)
      nt=time.ticks_ms()-tick
      _(40-int((nt)/3.23),16+int((nt)/12.5),48,48,1)
      b(ic[1],40-int((nt)/3.23),16+int((nt)/12.5))
      _(71-int((nt)/3.23),24-int((nt)/12.5),48,48,1)
      b(ic[2],71-int((nt)/3.23),24-int((nt)/12.5))
      s()
    z=(z+1)%len(app);del ic[0];ic+=[dcd('../$APP$/'+cmd[(z+1)%len(app)]+'.ic')]
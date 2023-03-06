import os
os.chdir('/$LIB$')

from PRECONFIG import LCD_SIZE as size
from scr import scrType,f,s,t,r,c,_,i
import touch,rd,time,Run,gc
if scrType=='LCD' and size[0]>=240 and size[1]>=120 and gc.mem_free()>999999:
  Run.run('dinop')
  raise
from math import sin,cos,pi
rdi=rd.rdi#,(6,11,17,21,25,28,29,30,29,28,25,21,17,11,6)#(8,15,21,26,29,30,29,26,21,15,8)
tuse=1
s()
def dino():
  global tuse,hi,rdi,phy,touch,rd,f,s,t,r,c,_,i
  pos,h,mp,mh,air,wd,tgt,edt=0,0,[128],[10],0,1,2000,0#玩家位置,高度,障碍等
  while mp[0]>6 or h>mh[0]-5:#玩家没碰到障碍时
    fdelay=time.ticks_ms()
    if len(mp)<3:#新增障碍
      if rdi(0,1) and rdi(0,pos/20000) and mp[-1]-mp[-2]>8+pos//1000:
        mp.append(mp[-1]+7+pos//1000);print(pos)
      else:
        mp.append(mp[-1]+rdi(12*(3+pos//3000),99+pos//99))
      mh.append(rdi(9,min(25,15+pos//500)))
    if touch.detect():
      if not air:
        air,edt=tuse,1#若未起跳，则起跳
    elif edt>0:
      edt=0
    if not edt and air and touch.detect():#起跳并松手
      edt,air=-1.3,8-abs(8-air)
    
    #h=int(phy[air-1]*min(edt,-1)*-1) if 0<air<16 else 0
    h=int(30*sin(air/16*pi)*min(edt,-1)*-1) if 0<air<16 else 0
    
    air=(air+tuse) if 0<air<16 else 0
    
    pos+=bool(pos)*tuse
    f(0);_(0,60,128,4,1);r(0,52-int(h),8,8,1)#清屏绘制地面，玩家
    for j in range(len(mp)):
      mp[j]-=tuse*(2+pos//2000)
      _(int(mp[j]),60-mh[j],int(5+pos//1000),mh[j],1)#移动绘制障碍物
    if mp[0]<-3-pos/1000:
      pos+=10*mh[0];del mp[0],mh[0]
    if mp[0]<7 and h<mh[0]-4 and wd and pos:
      mp,mh=[99]*2,[0,0];f(1);wd=0
    hi=max(int(pos),hi)
    
    if wd and pos:
      r(120,0,8,8,1)
    t(str(int(pos)),0,0);s()
    
    if pos>tgt:
      tgt+=2000;i(int(pos//2000))
    
    tuse=(time.ticks_ms()-fdelay)/40
    #time.sleep_ms(35-(time.ticks_ms()-fdelay))
  t('Game Over',56,0);t('Tap Retry',56,9);t(str(hi),0,9);s();i(0);return hi
fi=open('../$DAT$/dinohi','r+')
hi=int(fi.read())
while 1:
  hi=dino()
  if touch.prstime():
    fi.seek(0);fi.write(str(hi));fi.close();del dino,hi,rdi,touch,rd;break

from scr import f,s,t,r,c,_,i
import touch,rd,time
rdi=rd.rdi
fi=open('../$DAT$/flpchi','r+')
hi=int(fi.read())

def flpc():
  global hi,f,s,t,r,c,_,i,touch,rdi
  pos,h,mp,mh,air,a,tq=0,30,[128],[10],0,0,1#玩家位置,高度,障碍等
  tuse=1
  while mp[0]>6 or mh[0]+17>h>mh[0]-1:#玩家没碰到障碍时
    fdelay=time.ticks_ms()
    if len(mp)<3:#如果地图长度短于3，新增障碍
      mp.append(mp[-1]+rdi(40,80));mh.append(rdi(0,40))
    if touch.detect() and tq:
      a,tq=4+(a>0),0
    elif tq==0 and touch.detect()==0:
      tq=1
    h+=a*tuse;a-=tuse
    f(0);r(0,int(56-h),8,8,1)#清屏绘制玩家
    for j in range(len(mp)):
      mp[j]-=3*tuse;r(int(mp[j]),64-mh[j],8,mh[j],1);r(int(mp[j]),0,8,40-mh[j],1)#移动绘制障碍物
    if int(mp[0])<-5:
      pos+=1;del mp[0],mh[0]
      hi=max(pos,hi)
    t(str(pos),0,0);s()
    tuse=(time.ticks_ms()-fdelay)/50
    #time.sleep_ms(50-(time.ticks_ms()-fdelay))
  _(0,0,128,17,0);t('Game Over',56,0);t('Tap Retry',56,9);t(str(hi),0,9);t(str(pos),0,0);s();i(0);return hi

while 1:
  hi=flpc()
  if touch.prstime():
    fi.seek(0);fi.write(str(hi));fi.close();del hi,f,s,t,r,c,_,i,touch,rd,flpc;break

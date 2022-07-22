from scr import f,s,t,r,c,_,l
import touch,rd,time
from math import sin,cos,pi
rdi=rd.rdi
#tri=(.087,.174,.259,.342,.423,.5,.574,.643,.707,.766,.819,.866,.906,.94,.967,.985,.996)
def game():
  global hi,f,s,t,r,c,_,l,rdi,tri,touch,rd
  sc,stl,d,w=0,0,30,27#分数，棍长，地距，地宽
  f(0)
  while 1:
    _(0,48,8,16,1);r(0,40,8,8,1);_(d,48,w,48,1);stl=0;t(str(sc),0,0);s()#玩家和路
    while touch.detect()==False:
      pass
    _(0,9,96,8,0)
    while touch.detect() or stl<9:
      t1=time.ticks_ms()
      l(8,48,8,48-int(stl),1)#画竖线
      _(12,40,96,8,0)#擦除数字
      t(str(int(stl)),12,40)#显示数字
      s()
      stl+=(time.ticks_ms()-t1)/16
    l(8,0,8,64,0)#擦除竖线
    _(12,40,96,8,0)#擦除指示数字
    stl=int(stl)
    t1=time.ticks_ms()
    while time.ticks_ms()-t1<350:#for i in range(len(tri)):#放下棍子动画
      tuse=(time.ticks_ms()-t1)/700*pi
      l(8,48,int(8+stl*sin(tuse)),int(48-stl*cos(tuse)),1)
      t(str(sc),0,0);s()
      l(8,48,int(8+stl*sin(tuse)),int(48-stl*cos(tuse)),0)
    l(8,48,8+stl,48,1);s()#显示横线
    if d-9<=stl<=d-9+w:#落地范围
      acc=((d-9)+(d-9+w))/2#路面中点坐标值
      acc=abs(stl-acc)#棍到中点的距离
      acc=int((w/2-acc)/(w/2)*100)#边缘距中比值（准确度）
      sc+=(100 if acc>70 else acc)*(30-w)#加分
      t('Perfect!!!',0,9) if acc>70 else t('Good!('+str(acc)+'%)',0,9)
      t1=time.ticks_ms()
      while time.ticks_ms()-t1<8*(d+w-8):
        tuse=(time.ticks_ms()-t1)//8
        _(0,40,128,8,0)#擦除玩家
        r(tuse,40,8,8,1);s()
      f(1);s();f(0)
    else:
      hi=max(hi,sc)
      _(0,9,96,8,0);t('Game Over',0,9);t('HI:'+str(hi),0,18);s()
      break
    d,w=rdi(30,min(100,50+sc//250)),rdi(max(8,20-sc//1000),27)
fi=open('../$DAT$/stickhi','r+')
hi=int(fi.read())
while 1:
  game()
  if touch.prstime():
    fi.seek(0);fi.write(str(hi));fi.close();del hi,f,s,t,r,c,_,l,rdi,touch,rd,game;break

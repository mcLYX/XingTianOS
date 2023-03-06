import os
os.chdir('/$LIB$')
import lstui,tft,scr,time,config,gc,random,touch
d='../$USR$/'
rd=random.randint
c=scr.color
color=(
    (c(255,255,255),c(255,255,128)),
    (c(128,255,128),c(255,255,255)),
    (c(255,255,255),c(128,255,255)),
    (c(128,128,255),c(255,128,128)),
    (c(255,192,192),c(255,255,255)),
    (c(96,96,96),c(0,192,192)),
    (c(96,96,96),c(255,128,0)),
    ())[lstui.lstui([
        '明月',
        '草原',
        '青云',
        '霓虹',
        '糖果',
        '青墟',
        '篝火',
        '自定义',
        ],'颜色',0,1)[1]]
if not color:
    color1=[0,0,0]
    scr.f(c(*color1))
    scr.t('COLOR1',0,0,rd(0,65535))
    scr.t(str(color1),0,9,rd(0,65535))
    scr.s()
    i=0
    while touch.prstime():
        scr.f(c(*color1))
        scr.t('COLOR1',0,0,rd(0,65535))
        scr.t(str(color1),0,9,rd(0,65535))
        scr.s()
        while touch.d():
            color1[i]=(color1[i]+1)%256
            scr.f(c(*color1))
            scr.t('COLOR1',0,0,rd(0,65535))
            scr.t(str(color1),0,9,rd(0,65535))
            scr.s()
        i=(i+1)%3
        print(color1)
    color2=[0,0,0]
    scr.f(c(*color2))
    scr.t('COLOR2',0,0,rd(0,65535))
    scr.t(str(color2),0,9,rd(0,65535))
    scr.s()
    i=0
    while touch.prstime():
        scr.f(c(*color2))
        scr.t('COLOR2',0,0,rd(0,65535))
        scr.t(str(color2),0,9,rd(0,65535))
        scr.s()
        while touch.d():
            color2[i]=(color2[i]+1)%256
            scr.f(c(*color2))
            scr.t('COLOR2',0,0,rd(0,65535))
            scr.t(str(color2),0,9,rd(0,65535))
            scr.s()
        i=(i+1)%3
    color=(c(*color1),c(*color2))
    
wp=lstui.lstui([i for i in os.listdir(d) if '.jpg' in i],'壁纸',0,1)[0]
pic=tft.tft.jpg_decode(d+wp)
scr.f(0)
if pic[1]==240==pic[2]:
  config.write('homep_cfg',str(color[0])+'\n'+str(color[1])+'\n'+d+wp)
  scr.t('OK',0,0)
else:
  scr.t('Fail',0,0)
scr.s()
del pic
gc.collect()
time.sleep(1)
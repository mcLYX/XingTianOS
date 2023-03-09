import os
os.chdir('/$LIB$')

import gc,scr
if scr.scrType=='OLED' or gc.mem_free()<999999:import home

import touch,Run,mlgl,config,framebuf
from _scr import Screen,c2fb,lcdinit
from pbmds import dcd
from tft import tft
from dscn import dscd
from math import sin,pi
from machine import RTC
from time import ticks_ms,sleep

Scr=lcdinit()
s,f,_,b,m,o,t=Scr.s,Scr.f,Scr._,Scr.b,Scr.m,Scr.o,Scr.t

def getBG():
    global bg,bgc,frc,color,color2
    bgc,frc,bgf=config.read('homep_cfg').split('\n')
    bgc,frc=int(bgc),int(frc)
    color=c2fb(bgc)
    color2=c2fb(frc)
    bg=mlgl.Spirit(framebuf.FrameBuffer(*tft.jpg_decode(bgf),framebuf.RGB565),o)
try:getBG()
except:import home

fi=open('app.lst')
z,app,cmd=-1,eval(fi.readline()),eval(fi.readline())
fi.close();del fi
rtc=RTC()

#动画时长ms
drawer=180#开关应用抽屉时
appboot=300#启动应用时
swcapp=120#切换应用时

num=open('numbig.pbm','rb')
num.readline();num.readline()
clkbuf=[]
for i in range(10):
    clkbuf.append(framebuf.FrameBuffer(bytearray(num.read(48*68//8)),44,68,framebuf.MONO_HLSB))
num.close()
del num

def appUI(k):
    global app,cmd,bg,bgc,frc
    ic=[]
    z=k if k!=-1 else 0
    pos=24
    try:
        for i in (z-1,z,z+1,z+2):
            if i>=0:ic.append(mlgl.Spirit(dcd('../$APP$/'+cmd[i]+'.ic'),o,288,pos))
            pos+=48+24
    except:
        pass

    tick=ticks_ms()   
    pos=96-72*bool(z)
    for i in ic:
        i.moveEvent(180,pos,drawer,2)
        pos+=48+24
      
    pos=240
    while ticks_ms()-tick<=drawer:
        nt=sin((ticks_ms()-tick)/drawer*pi/2)
        m(int(240-72*nt)-pos,0)
        pos=int(240-72*nt)
        _(pos,0,240,240,0)   
        for i in ic:
            i.blit(0,color)
        s()

    while 1:
        bg.moveTo(-72,0)
        bg.blit()
        dscd(app[z],0,2,mv=(-2,1),bf=o,p=color2,c=frc)
        _(168,0,240,240,0)
        for i in range(len(ic)):
            ic[i].blit(0,color2 if len(ic)-i==3-max(0,z-len(app)+3) else color)
        s()
        if touch.prstime():
            return z
        elif z==len(app)-1:
            return -1
        else:
            pos=-48 if z else 24
            z+=1
            if len(app)-2>z:
                ic+=[mlgl.Spirit(dcd('../$APP$/'+cmd[(z+2)]+'.ic'),o,180,269)]
            for i in ic:
                i.moveEvent(180,pos,swcapp,1)
                pos+=48+24
            tick=ticks_ms()
            while ticks_ms()-tick<=swcapp:
                _(168,0,240,240,0)
                for i in ic:
                    i.blit(0,color)
                s()
            if z>1:del ic[0]

def mainUI(x=0):
    bg.moveTo(x,0)
    bg.blit()
    blitClk(x+2)
    s()

def blitClk(x=2,y=3,xsp=2,ysp=9):
    now=rtc.datetime()
    b(clkbuf[now[4]//10],x,y,0,color)
    b(clkbuf[now[4]%10],x+44+xsp,y,0,color)
    b(clkbuf[now[5]//10],x,y+ysp+68,0,color2)
    b(clkbuf[now[5]%10],x+44+xsp,y+ysp+68,0,color2)
    t('%02d'%now[6],x+1,y+ysp*2+68*2,frc)
    t('%02d'%now[1]+'/'+'%02d'%now[2]+' '+('MON','TUE','WED','THU','FRI','SAT','SUN')[now[3]],x+1,240-8-y,bgc)

while 1:
    if z!=-1:
        getBG()
    bg.blit()
    if z==-1:
        while touch.d():
            pass
        mainUI()
        while (not touch.d()):
            sleep(.1)
            mainUI()
    selapp=appUI(z)
    z=selapp
    if selapp!=-1:
        ic=[]
        tick=ticks_ms()
        pos=240
        while ticks_ms()-tick<=appboot:
            nt=sin((ticks_ms()-tick)/appboot*pi/2)
            m(int(240-240*nt)-pos,0)
            pos=int(240-240*nt)
            _(pos,0,240,240,0) 
            s()
        f(0);s();del pos,bg,tick;gc.collect();Run.run(cmd[selapp])
    else:
        pos=168
        tick=ticks_ms()
        while ticks_ms()-tick<=drawer and (not touch.d()):
            nt=sin((ticks_ms()-tick)/drawer*pi/2)
            m(int(168+72*nt)-pos,0)
            pos=int(168+72*nt)
            mainUI(int(72*nt-72))
        mainUI()
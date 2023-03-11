import os,gc
os.chdir('/$LIB$')
gc.collect()

#检查连接的啥屏幕及适配内存大小
import scr
scr.f(0);scr.t('Please Wait...',0,0);scr.s()
from _scr import Screen,color,c2fb,lcdinit
if scr.scrType=='OLED' or gc.mem_free()<999999:
    sw,sh,nh=128,64,6
    mspx=0.1#每ms多少像素(流速)
else:
    sw,sh,nh=200,120,8#屏幕宽高,note高度
    del scr
    scr=Screen(sw,sh,sw*sh*2)
    mspx=0.2
import dstxt,key4,zlib,touch,time,lstui,dscn,pbmds,framebuf,machine

d='../$DAT$/Melopy/'
maxload=16 #最大加载note数
c=color(128,255,255)#蓝色
c2=color(255,255,128)#黄色
c3=color(255,64,64)#红
perfms=72#Perfect ms
goodms=128
badms=160
songsel=['',0]
pause=0#暂停计数器
uart=machine.UART(1,tx=18,rx=16,baudrate=9600)
volume=15#音量
delay=-40#音频延迟
dspbuf=1.0018#谱面速度修正

def ctrl(com):
    uart.write(bytes((0x7e,0xff,0x06))+com+bytes([0xef]))

def play(song):
    try:
        with open(d+'Charts/'+song+'/songid.txt') as f:
            songid=int(f.read())
            ctrl(bytes((0x0f,0x00,0x01,songid)))
    except:
        pass

def stop(s=1):
    ctrl(bytes((0x0D+s,0x00,0x00,0x00)))

def vol(value=15):
    ctrl(bytes((0x06,0x00,0x00,value)))

def init():
    global notes,record,prskey,keystat,holds,hitfb,playing
    notes=[[],[],[],[]]
    record=[0,0,0,0]#PGBM
    prskey=[0,0,0,0]#按住了按键？
    keystat=[0,0,0,0]#刚被按下的按键？
    holds=[0,0,0,0]#正在按长条？
    hitfb=[]#打击判定提醒 [text,time]
    playing=0#音乐已播放？

def lennote():#获取场上note数量
    return len(notes[0])+len(notes[1])+len(notes[2])+len(notes[3])

def acc():#获取当前ACC
    total=sum(record)
    return ("%.2f" % abs((record[0]/total+record[1]/total/2)*100-0.005)) if total else '100.00'

def loadnote():#加载下一个note
    load=file.readline().split()
    if len(load)==2:#Tap
        tick,col=load
        tick,col=int(tick),int(col)
        notes[col].append(tick)
    elif len(load)==3:#Hold
        tick,col,end=load
        tick,col,end=int(tick),int(col),int(end)
        notes[col].append((tick,end))
    else:
        return 0
    return 1

def checkotn(t):#检查超时(miss/已结束Hold)note
    global hitfb
    for i in range(4):
        if not notes[i]:continue
        last=notes[i][0]
        if isinstance(last,int) and last+goodms<t:
            dnote(t,i,3)
        elif isinstance(last,tuple) and last[1]+goodms<t:
            dnote(t,i,holds[i]-1)
            holds[i]=0

@micropython.native
def shownote(t):#显示画面
    global hitfb
    scr.o.fill(0)
    scr.o.rect(0,0,sw,sh,65535)
    scr.o.hline(0,sh-nh,sw,65535)
    for i in range(4):
        for j in notes[i]:
            if isinstance(j,int):
                if mspx*(j-t)>sh:break
                scr.o.fill_rect(sw//4*i+2,int(sh-mspx*(j-t))-nh,sw//4-4,nh,c if 0<i<3 else 65535)#Tap
            else:
                start=int(sh-mspx*(j[0]-t))
                if start<0:break
                end=int(sh-mspx*(j[1]-t))
                scr.o.fill_rect(sw//4*i+2,end-1,sw//4-4,start-end+1,c if 0<i<3 else 65535)
        scr.o.vline(sw//4+i*(sw//4),0,sh,65535)
        if prskey[i]:
            scr.o.fill_rect(i*sw//4,sh-nh+1,sw//4,nh-2,c2)
        scr.o.text(acc()+'%',1,2,7)
    if hitfb:
        scr.o.text(('BEST','GOOD','POOR','MISS')[hitfb[0]],sw//2-16,45-(t-hitfb[1])//20,(c2,c,c3,c3)[hitfb[0]])
        if t-hitfb[1]>200:hitfb=[]
    scr.s(0)

def dnote(t,col,reason):#记录并删除某轨道最近的note
    global hitfb
    record[reason]+=1
    hitfb=(reason,t)
    del notes[col][0]

def chktp(t,i):#检查Tap和Hold头判
    global hitfb
    last=notes[i][0]
    if isinstance(last,int):#TAP
        delta=abs(last-t)
        if delta<perfms:dnote(t,i,0)#Perfect/BEST
        elif delta<goodms:dnote(t,i,1)#Good
        elif delta<badms:dnote(t,i,2)#Bad/POOR
    else:#HOLD头判
        delta=abs(last[0]-t)
        if delta<perfms:holds[i]=1;hitfb=(0,t)#Perfect/Best
        elif delta<goodms:holds[i]=2;hitfb=(1,t)#Good
        elif delta<badms:holds[i]=0;dnote(t,i,2)#Bad/Poor

def panding(t,kstat,prsk):#检查判定
    for i in range(4):
        #是否按下按键且有note
        if kstat[i] and notes[i]:chktp(t,i)
        #Hold持续判定
        if holds[i] and not prsk[i]:
            if notes[i][0][1]-t>goodms:dnote(t,i,2)#如果提前松手超过good判定范围，直接poor
            elif notes[i][0][1]-t>perfms:dnote(t,i,1)#如果不超过good范围，但超过best范围，改判good
            else:dnote(t,i,holds[i]-1)#松的挺准，保持原判
            holds[i]=0

def result():
    global song,chart,d
    scr.f(0)
    dscn.dscd(dscn.tran(song),0,0,bf=scr.o)
    dscn.dscd(dscn.tran(chart),0,13,bf=scr.o)
    scr.t('ACC: '+acc()+'%',0,sh-8,1)
    scr.s()
    if sh<120 and touch.prstime():return
    scr.t('BEST '+str(record[0]),0,40,c2)
    scr.t('GOOD '+str(record[1]),0,50,c)
    scr.t('POOR '+str(record[2]),0,60,c3)
    scr.t('MISS '+str(record[3]),0,70,c3)
    icons=('您','S+','S','A','B','C','F')
    for i in range(7):
        if float(acc())>=(100,98,95,90,80,70,0)[i]:
            icon=pbmds.dcd(d+'ICON/'+icons[i]+'.pbm')
            scr.b(icon,sw-64,32,0,c2fb([c2,c2,c2,c,7,65535,c3][i]))
            break
    scr.s()
    touch.prstime()

while 1:
    init()
    songsel=lstui.lstui([[1381,293,'...']]+os.listdir(d+'Charts/')+[[1641,1477],[1313,1990]],'Select Music',songsel[1],1)
    song=songsel[0]
    print(song)
    if song==[1381,293,'...']:break#退出
    if song==[1641,1477]:#流速
        mspx=0.1+lstui.lstui([str(i/100) for i in range(100,400+1,25)],'Speed',int((mspx-0.1)*40))[1]/40
        continue
    if song==[1313,1990]:#VOLUME
        volume=lstui.lstui(('0','5','10','15','20','25','30'),'VOL',volume//5)[1]*5
        continue
    chart=lstui.lstui([i[:-4] for i in os.listdir(d+'Charts/'+song) if i[-4:]=='.mpc']+[[675,389,'...']],'Difficulty',0,1)[0]
    if chart==[675,389,'...']:continue
    file=zlib.DecompIO(open(d+'Charts/'+song+'/'+chart+'.mpc','rb'))
    scr.f(0)
    dscn.dscd(dscn.tran(song),0,0,bf=scr.o)
    dscn.dscd(dscn.tran(chart),0,13,bf=scr.o)
    scr.s()
    time.sleep(1)
    scr.f(0)
    vol(volume)
    start=time.ticks_ms()+1000
    #play(song)
    while 1:
        #fpsticker=time.ticks_us()
        curtime=int((time.ticks_ms()-start)*dspbuf)
        notelen=lennote()
        for i in range(maxload-notelen):
            load=loadnote()
        checkotn(curtime)
        shownote(curtime)
        if not(load or notelen):
            time.sleep(1)
            break
        if not playing and curtime>delay:
            playing=1
            play(song)
        #检查按键
        curprs=key4.get()
        for i in range(4):
            if curprs[i]!=prskey[i]:keystat[i],prskey[i]=curprs[i],curprs[i]
            else:keystat[i]=0
        panding(curtime,keystat,prskey)
        pause=pause+1 if touch.d() else 0
        if pause>=10:
            pausetime=time.ticks_ms()
            stop(1)
            scr.t('PAUSED',sw-49,2,c3)
            scr.s()
            if touch.prstime():break
            start+=time.ticks_ms()-pausetime
            stop(0)
        #print(1000000/(time.ticks_us()-fpsticker))
    if pause<10:result()

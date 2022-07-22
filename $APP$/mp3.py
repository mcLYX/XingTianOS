import machine,scr,dscn,lstui,touch,os

uart=machine.UART(0,baudrate=9600)
#uart2=machine.UART(1,baudrate=9600)
os.dupterm(None)

#部分命令
rdplay=bytes((0x18,0x00,0x00,0x02,0xfe,0xe1))#随机歌曲
nextp=bytes((0x01,0x00,0x00,0x00))#下一首
prevp=bytes((0x02,0x00,0x00,0x00))#上一首
play=bytes((0x0D,0x00,0x00,0x00))#播放
pause=bytes((0x0E,0x00,0x00,0x00))#暂停
cyplay=bytes((0x11,0x00,0x00,0x01))#全部循环
xinao=bytes((0x19,0x00,0x00,0x01))#洗脑循环

def ctrl(com):uart.write(bytes((0x7e,0xff,0x06))+com+bytes([0xef]))
def vol(value=30):ctrl(bytes((0x06,0x00,0x00,value)))
vol()
ctrl(play)

t=dscn.tran
opt=[]
for i in ('上一首','下一首','暂停','播放','随机歌曲',
          '全曲循环','洗脑循环','音量','退出...'):opt.append(t(i))
a=0
while 1:
    a=lstui.lstui(opt,'MP3',a)[1]
    if a==0:ctrl(prevp)
    elif a==1:ctrl(nextp)
    elif a==2:ctrl(pause)
    elif a==3:ctrl(play)
    elif a==4:ctrl(rdplay)
    elif a==5:ctrl(cyplay)
    elif a==6:ctrl(xinao)
    elif a==7:vol(lstui.lstui(('0','5','10','15','20','25','30','35'),'VOL',6)[1]*5)
    else:break
    scr.f(0)
    scr.t('OK',0,0)
    scr.s()
    while touch.d():pass
    if uart.any():
        scr.f(0);scr.t(str(uart.read()),0,0);scr.s();touch.prstime()
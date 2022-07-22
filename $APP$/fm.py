from machine import I2C,Pin
from scr import f,t,s
from dscn import dscd
from lstui import lstui,qna
from touch import prstime,d
from time import sleep

i2c = I2C(scl=Pin(9), sda=Pin(8))
print(i2c.scan())

freq=97.9
rssi=0

#rdaaddr = 16 
stat=bytearray(8)
info=bytes(4)

#02H
stat[0]=0b11010000#15~8
stat[1]=0b00000001#7~0

#03H
stat[2]=0b00010111#15~8,freq
stat[3]=0b11010000#7~0,freq(7~6)

#04H，不用管，全是0
stat[4]=0
stat[5]=0

#05H
stat[6]=0b10001000
stat[7]=0b10110000

#调整音量（0~16）
def volume(value=9):
    value=int(value)
    if value>16:
        value=16
    elif value<0:
        value=0
    if value:
        stat[0]=stat[0] | 0b01000000
        stat[7]=stat[7] & 0b11110000 | (value-1)
    else:
        stat[0]=stat[0] & 0b10111111
    i2c.writeto(16,stat)

#重低音(1开0关）
def bass(value=1):
    if value:
        stat[0]=stat[0] | 0b00010000
    else:
        stat[0]=stat[0] & 0b11101111
    i2c.writeto(16,stat)

#搜台
def seek(value=1):
    stat[0]=(stat[0] | 0b00000001) if value else (stat[0] & 0b11111110)
    i2c.writeto(16,stat)

#获取当前状态
getrssi=lambda:i2c.readfrom(17,4)[2]>>1

def rdreset():
	i2c.writeto(16,b'\x00\x02')

def rdinit():
	i2c.writeto(16,b'\xc1\x03\x00\x00\x0a\x00\x88\x0f\x00\x00\x42\x02')

def tune(freq):
	fq = int((freq-87.0)*10.0+0.5)
	stat[2]=fq>>2
	stat[3]=(fq<<6)+0b00010000
	i2c.writeto(16,stat)

def resetfm():
    rdreset()  #复位
    rdinit()   #初始化
    tune(freq) #调频

try:
    resetfm()
    while 1:
        f(0)
        dscd([220,305,':',("%.1f"%freq),'Mhz'])
        sleep(.5)
        rssi=getrssi()
        dscd([1262, 221, 2114, 1304,':'+str(rssi)],0,13);s()
        if prstime():
            while d():
                freq=freq+0.1 if int(freq*10+.5)<1080 else 87
                sleep(.05)
                f(0);dscd([220,305,':',("%.1f"%freq),'Mhz']);s()
            tune(freq)
        else:
            sel=lstui(([675,389],'0.1Mhz',[1313,1990],[1247,664,1313],[1247,2197],[1930,305],[1381,293,'...']),'FM',0)[1]
            if sel==2:
                vol=stat[7]%16
                while d():
                    vol=(vol+1)%17
                    f(0);t('VOLUME:'+str(vol),0,0);s()
                    sleep(.2)
                volume(vol)
            elif sel==1:
                freq+=.2*(qna(['+ OR -?'],['+0.1Mhz','-0.1Mhz'])-.5)
                if freq>108:freq=87
                elif freq<87:freq=108
                tune(freq)
            elif sel==3:bass(qna(['BASS EFFECT'],['ON','OFF']))
            elif sel==4:resetfm()
            elif sel==5:seek()
            elif sel==6:break
except:
    f(0)
    dscd(['FM', 178, 610, 1721, 856, 58, 1856, 72])
    s()
    sleep(1)
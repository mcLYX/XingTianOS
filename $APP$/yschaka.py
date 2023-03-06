import scr,dscn,lstui,gc
from random import randint as rd
import tft,touch,time
jpg=tft.tft.jpg
path='../$DAT$/'
chakatimes=0
baodi5=0#是否大保底
#baodi4=0#是否四星保底
chaka5=0#距上次5星已抽
chaka4=0#距上次4星已抽
getht=0
get5=0
get4=0
records=['尚未出金','','','','']
lowmem=gc.mem_free()<999999

# 简易的概率模型 E(X)=62
def p(i):
    return 6 if i<74 else 6+60*(i-73)

bgcolor=0b1100010111111111
bgcolor=bytes([bgcolor>>8,bgcolor%256])
ckcolor=0b0011000101100110
ckcolor=bytes([ckcolor>>8,ckcolor%256])

def mainbg():
    tft.fill(bgcolor)
    jpg(path+'hutao.jpg',0,30,1)
    jpg(path+'button1.jpg',0,185,1)
    jpg(path+'button2.jpg',120,185,1)

def ckani():
    for i in range(0,6,1+lowmem):
        jpg(path+'ChakaAni/'+str(i+1)+'.jpg',0,0,lowmem)
    time.sleep(.5)

def result(result,f=1):
    result.sort()
    startx=120-12*len(result)
    photolist=['ht','5','4','3']
    if f:tft.fill(ckcolor)
    for i in range(len(result)):
        jpg(path+'chaka'+photolist[result[i]]+'.jpg',startx+i*24,45,1)
        
def chaka(times):
    global chakatimes,baodi5,chaka5,chaka4,getht,get5,get4,path
    get=[]
    def gotht():
        global baodi5,chaka5,chaka4,getht
        get.append(0)
        del records[0]
        records.append('胡桃 ['+str(chaka5+1)+']')
        baodi5=0
        chaka5=0
        chaka4+=1
        getht+=1
    def got5():
        global baodi5,chaka5,chaka4,get5
        get.append(1)
        del records[0]
        #麻了，字库里没有放 [娜] 和 [迪] 字，焯！
        records.append(('卢姥爷','琴','刻晴','七七','莫那','提纳里')[rd(0,5)]+' ['+str(chaka5+1)+']')
        baodi5=1
        chaka5=0
        chaka4+=1
        get5+=1
    def got4():
        global chaka5,chaka4,get4
        get.append(2)
        chaka4=0
        chaka5+=1
        get4+=1
    for i in range(times):
        num=rd(1,1000)
        if num<=p(chaka5+1):
            if baodi5:
                gotht()
            else:
                if rd(0,1):gotht()
                else:got5()
        elif chaka5>=89:
            if baodi5:
                gotht()
            else:
                if rd(0,1):gotht()
                else:got5()
        elif num>949:got4()
        elif chaka4>=9:got4()
        else:
            get.append(3)
            chaka4+=1
            chaka5+=1
        chakatimes+=1
    return get
              
while 1:
    mainbg()
    if not touch.prstime():
        print('抽卡')
        #单抽 十连抽 科技速抽 返回 退出... 祈愿
        sel=lstui.lstui([[1010,807],[3,610,807],[1246,540,1477,807],[675,389],[1381,293,'...']],[2797,2297],0)
        sel=sel[1]
        if sel==0:
            ckani()
            result(chaka(1))
            touch.prstime()
        elif sel==1:
            ckani()
            result(chaka(10))
            touch.prstime()
        elif sel==2:
            result(chaka(10))
            while not touch.d():
                result(chaka(10))
        elif sel==4:
            tft.fill()
            break
    else:
        print('详情')
        scr.f(0);scr.s()
        dscn.cn('总抽数:'+str(chakatimes),0,0)
        dscn.cn('限定五星数:'+str(getht),0,13)
        dscn.cn('常驻五星数:'+str(get5),0,26)
        dscn.cn('四星数:'+str(get4),0,39)
        dscn.cn('已垫抽数:'+str(chaka5),0,52)
        scr.s()
        touch.prstime()
        scr.f(0);scr.s()
        for i in range(5):
            dscn.cn(records[-i-1],0,i*13)
        scr.s()
        touch.prstime()
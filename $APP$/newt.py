from scr import f,s,t,r,c,_,i
invert=i
import touch,rd,time,dscn
try:
    fi=open('../$DAT$/newtonr')
except:
    fi=open('../$DAT$/newtonr','w')
    fi.write('0')
    fi.close()
    fi=open('../$DAT$/newtonr')
record=int(fi.read())
fi.close()
while 1:
    
    #init
    level=[[128,0,32]]#level map
    boost=[256,0]
    #0是正的，1是倒着的
    h=0#player current height
    G=1#Gravitity value,1down
    score=0#player score
    tq=0
    fspd=0#player fall speed
    mrspd=3#map rolling speed
    tuse=1
    #main
    while level[0][0]>6 or ((h<=(56-level[0][2])) if not level[0][1] else (h>=(level[0][2]))):
        
        fdelay=time.ticks_ms()
        
        #添加障碍
        if len(level)<4:
            level.append([level[-1][0]+rd.rdi(9+9*mrspd,45+15*mrspd),
                          rd.rdi(0,1),
                          rd.rdi(16,48)])
        
        if -7<boost[0]<7:
            if abs(h-boost[1]%72+8)<7:
                score+=mrspd*500
                mrspd+=1
                boost=[rd.rdi(256+20*mrspd,384+30*mrspd),0]
                for i in range(9):
                    invert(i)
                    time.sleep(.05)
                level=[level[-1]]
                fdelay=time.ticks_ms()
        elif boost[0]<=-7:
            boost=[rd.rdi(256+20*mrspd,384+30*mrspd),0]
            
        
        for i in range(len(level)):
            level[i][0]=level[i][0]-mrspd*tuse
        if level[0][0]<-mrspd*2-1:
            score+=level[0][2]*mrspd
            del level[0]
        boost[0]-=tuse
        boost[1]+=G*tuse
        score+=bool(score)*tuse
        record=max(record,int(score))
        
        #按键部分
        tqnow=touch.d()
        if tqnow!=tq:
            tqstat,tq=tqnow,tqnow
        else:
            tqstat=0
            
        #按键按下后
        if tqstat:
            G=-G
        
        if h>=0 and h<=56:
            if fspd*G>=0:
                fspd+=G*tuse
            else:
                fspd=0
        h+=fspd*tuse
        if h<0:
            h=0
        if h>56:
            h=56
            
        #画画
        f(0)
        for i in level:
            if i[1]:
                _(int(i[0]),0,2+2*mrspd,i[2],63551)#倒柱子
            else:
                _(int(i[0]),64-i[2],2*mrspd+2,i[2],2047)#正柱子
        t('+',int(boost[0]),int(boost[1]%72-8))#加速块
        r(0,int(h),8,8,63)#画玩家
        t(str(int(score)),64-len(str(int(score)))*4,0)
        s()
        tuse=(time.ticks_ms()-fdelay)/40
        #time.sleep_ms(35-(time.ticks_ms()-fdelay))
    
    #GG之后
    invert(1)
    time.sleep(1)
    f(0)
    score=int(score)
    if score<1:rank='开摆！'
    elif score<2000:rank='菜'
    elif score<5000:rank='D'
    elif score<10000:rank='C'
    elif score<20000:rank='B'
    elif score<30000:rank='A'
    elif score<50000:rank='S'
    elif score<100000:rank='S+'
    else:rank='人否？'
    
    dscn.cn('本局得分:'+str(score))
    dscn.cn('评级:'+rank,y=13)
    
    if score>=record:
        dscn.cn('新纪录！',y=26)
    else:
        dscn.cn('纪录:'+str(record),y=26)
        
    dscn.cn('轻触重试',40,52)
    
    invert(0)
    s()
    if touch.prstime():
        fi=open('newtonr','w')
        fi.write(str(record))
        fi.close()
        break

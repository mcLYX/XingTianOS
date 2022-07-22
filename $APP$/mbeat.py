from scr import *
import touch,machine,rd,time,lstui,dscn
a=machine.Pin(2)
L=touch.d
R=a.value
LSTAT=0
RSTAT=0
HP=100
score=0
total=0
count=[0,0,0,0,0]#PGBMC
maxc=0
tuse=1000
file=open('../$DAT$/'+('badapple.bct' if (L() and R()) else'ysjd.bct'))
speed=lstui.lstui(['1','2','3','4'],'SPEED')[1]+1
chartL,chartR=[],[]
def load():
    global total
    l=file.readline()
    if l:
        l=float(l)
        if l>0:
            chartL.append(total+l)
        else:
            chartR.append(total-l)
        total+=abs(l)
load()
stime=time.ticks_ms()
while HP>0 and (chartL or chartR):
    if len(chartL+chartR)<9:
        load()
    f(0)
    h(13,63,HP,1)
    r(4,4,56,56,1)
    r(68,4,56,56,1)
    t(str(score),0,0)
    #t(str(count),-8,56)
    t('FPS:'+str(int(1000/tuse)),72,0)
    LC=L()
    RC=R()
    
    if LC!=LSTAT:
        if chartL and (not LSTAT) and LC:
            if chartL[0]<=6:
                acc=3-abs(chartL[0]-3)
                score+=5 if acc>1 else 2
                HP=min(100,HP+(acc>1))
                t('Perfect' if acc>1 else 'Good', (4 if acc>1 else 16) ,30)
                count[acc<=1]+=1
                count[4]+=1
                del chartL[0]
            elif chartL[0]<9:
                HP-=5
                t('Bad',20,30)
                count[2]+=1
                count[4]=0
                del chartL[0]
        LSTAT=not LSTAT
        
    if RC!=RSTAT:
        if chartR and (not RSTAT) and RC:
            if chartR[0]<=6:
                acc=3-abs(chartR[0]-3)
                score+=5 if acc>1 else 2
                HP=min(100,HP+(acc>1))
                t('Perfect' if acc>1 else 'Good', 64+(4 if acc>1 else 16) ,30)
                count[acc<=1]+=1
                count[4]+=1
                del chartR[0]
            elif chartR[0]<9:
                HP-=5
                t('Bad',84,30)
                count[2]+=1
                count[4]=0
                del chartR[0]
        RSTAT=not RSTAT
        
    if chartL and chartL[0]<0:
        del chartL[0]
        HP-=5
        count[3]+=1
        count[4]=0
        t('Miss',16,30)
    if chartR and chartR[0]<0:
        del chartR[0]
        HP-=5
        count[3]+=1
        count[4]=0
        t('Miss',80,30)
    maxc=max(maxc,count[4]) 
    for i in chartL:r(int(speed*i),int(speed*i),64-int(i*2*speed),64-int(i*2*speed),i<(32/speed))
    for i in chartR:r(int(i*speed)+64,int(i*speed),64-int(i*2*speed),64-int(i*2*speed),i<(32/speed))
    s(0)
    tuse=time.ticks_ms()-stime
    stime+=tuse
    #print(tuse)
    for i in range(len(chartL)):chartL[i]-=tuse/36#保持同步
    for i in range(len(chartR)):chartR[i]-=tuse/36#1秒=27.78
    total-=tuse/36
time.sleep(2)

f(0)
t('LEVEL COMPLETED' if HP>0 else 'LEVEL FAILED',4 if HP>0 else 16,0)
t('P/G/B/M:',0,18)
t(str(count[0])+'/'+str(count[1])+'/'+str(count[2])+'/'+str(count[3]),0,27)
t('MAX Combo:'+str(maxc),0,36)
t('SCORE:'+str(score),0,54)
s()
touch.prstime()

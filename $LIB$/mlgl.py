import time,math
class Spirit(object):
    def __init__(self,picbuf,scrbuf,x=0,y=0):
        self.picbuf,self.scrbuf,self.x,self.y=picbuf,scrbuf,x,y
        self.moveEvt=[]
    def moveTo(self,x,y):
        self.x,self.y=x,y
    def moveEvent(self,toX,toY,times=0,aniType=0,cycle=0):
        if not isinstance(times,list):
            times=[time.ticks_ms(),time.ticks_ms()+times]
        self.moveEvt=[[self.x,self.y],[toX,toY],times,aniType,cycle]
    def update(self):
        if self.moveEvt:
            currentTime=time.ticks_ms()
            moveEvt=self.moveEvt
            if currentTime>=moveEvt[2][1]:#endtime
                if moveEvt[4]:
                    deltat1=(currentTime-moveEvt[2][0])
                    deltat2=(moveEvt[2][1]-moveEvt[2][0])
                    moveEvt[2][0]+=(deltat1//deltat2)*deltat2
                    moveEvt[2][1]=moveEvt[2][0]+deltat2
                    self.update()
                    return
                else:
                    self.x,self.y=moveEvt[1][0],moveEvt[1][1]
                    self.moveEvt=[]
            else:
                deltat=(currentTime-moveEvt[2][0])/(moveEvt[2][1]-moveEvt[2][0])%1#deltatime
                deltax=(moveEvt[1][0]-moveEvt[0][0])
                deltay=(moveEvt[1][1]-moveEvt[0][1])
                if moveEvt[3]==0:
                    dx=deltat * deltax + moveEvt[0][0]
                    dy=deltat * deltay + moveEvt[0][1]
                elif moveEvt[3]==1:
                    dx=math.sin(deltat*math.pi/2) * deltax + moveEvt[0][0]
                    dy=math.sin(deltat*math.pi/2) * deltay + moveEvt[0][1]
                elif moveEvt[3]==2:
                    dx=(1-math.cos(deltat*math.pi/2)) * deltax + moveEvt[0][0]
                    dy=(1-math.cos(deltat*math.pi/2)) * deltay + moveEvt[0][1]
                elif moveEvt[3]==3:
                    dx=(math.sin(deltat*math.pi/2)) * deltax + moveEvt[0][0]
                    dy=(1-math.cos(deltat*math.pi/2)) * deltay + moveEvt[0][1]
                elif moveEvt[3]==4:
                    dx=(1-math.cos(deltat*math.pi/2)) * deltax + moveEvt[0][0]
                    dy=(math.sin(deltat*math.pi/2)) * deltay + moveEvt[0][1]
                self.x,self.y=dx,dy
    def blit(self,a=-1,c=None):
        self.update()
        self.scrbuf.blit(self.picbuf,int(.5+self.x),int(.5+self.y),a,c)
    def __del__(self):
        del self.picbuf
        print('test')

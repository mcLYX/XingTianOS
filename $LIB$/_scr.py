import framebuf,tft,gc
from PRECONFIG import LCD_SIZE as size
color=lambda R=0,G=0,B=0 : (R//8<<3) + (G//4>>3) + (G//4%8<<13) + (B//8<<8)
c2fb=lambda c=65535 : framebuf.FrameBuffer(bytearray([0,0,c%256,c//256]),2,1,framebuf.RGB565)
class Screen(object):
  def __init__(self,x=size[0],y=size[1],buf=size[0]*size[1]*2,typ=framebuf.RGB565):
    self.pos=((size[0]//2-x//2,size[1]//2-y//2),(size[0]//2-x//2+x-1,size[1]//2-y//2+y-1))
    #tft.fill()
    self.o=framebuf.FrameBuffer(bytearray(buf),x,y,typ)
    self.t=lambda s,x=0,y=0,c=1:self.o.text(s,x,y,65535 if c==1 else c)
    self.f=lambda c=1:self.o.fill(65535 if c==1 else c)
    self.p=lambda x=0,y=0,c=1:self.o.pixel(s,x,y,65535 if c==1 else c)
    self.h=lambda x=0,y=0,l=128,c=1:self.o.hline(x,y,l,65535 if c==1 else c)
    self.i=tft.invert
    self.l=lambda x1=0,y1=0,x2=128,y2=64,c=1:self.o.line(x1,y1,x2,y2,65535 if c==1 else c)
    self.v=lambda x=0,y=0,l=64,c=1:self.o.vline(x,y,l,65535 if c==1 else c)
    self._=lambda x1=0,y1=0,x2=128,y2=64,c=1:self.o.fill_rect(x1,y1,x2,y2,65535 if c==1 else c)
    self.r=lambda x1=0,y1=0,x2=128,y2=64,c=1:self.o.rect(x1,y1,x2,y2,65535 if c==1 else c)
    self.b=lambda f,x,y,a=-1,c=framebuf.FrameBuffer(bytearray([0,0,255,255]),2,1,framebuf.RGB565):self.o.blit(f,x,y,a,c)
    self.m=self.o.scroll
    self.c=int
    print('LCD READY')
    self.scrType='LCD'
  def s(self,rs=1):
    if rs:tft.setarea(self.pos[0],self.pos[1])
    tft.dc(1)
    tft.spi.write(self.o)
  def __del__(self):
    gc.collect()
    print('DEL SCREEN')
  
def lcdinit():
    global lcd
    try:lcd
    except:lcd=Screen()
    return lcd
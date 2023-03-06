pos=(0,0),(239,239)
color=lambda R=0,G=0,B=0 : (R//8<<3) + (G//4>>3) + (G//4%8<<13) + (B//8<<8)
try:
  from ssd1306 import SSD1306_I2C
  from PRECONFIG import OLED_I2C
  o=SSD1306_I2C(128,64,OLED_I2C)
  s=lambda rs=1:o.show()
  t,f,p,h,c,i,l,v,_,r,b,m=o.text,o.fill,o.pixel,o.hline,o.contrast,o.invert,o.line,o.vline,o.fill_rect,o.rect,o.blit,o.scroll
  print('OLED READY')
  scrType='OLED'
except:
  import framebuf,tft,gc
  from PRECONFIG import LCD_SIZE as size
  pos=(size[0]//2-64,size[1]//2-32),(size[0]//2+63,size[1]//2+31)
  tft.fill()
  o=framebuf.FrameBuffer(bytearray(128*64*2),128,64,framebuf.RGB565)
  def s(rs=1):
    if rs:tft.setarea(pos[0],pos[1])
    tft.dc(1)
    tft.spi.write(o)
  t=lambda s,x=0,y=0,c=1:o.text(s,x,y,65535 if c==1 else c)
  f=lambda c=1:o.fill(65535 if c==1 else c)
  p=lambda x=0,y=0,c=1:o.pixel(s,x,y,65535 if c==1 else c)
  h=lambda x=0,y=0,l=128,c=1:o.hline(x,y,l,65535 if c==1 else c)
  i=tft.invert
  l=lambda x1=0,y1=0,x2=128,y2=64,c=1:o.line(x1,y1,x2,y2,65535 if c==1 else c)
  v=lambda x=0,y=0,l=64,c=1:o.vline(x,y,l,65535 if c==1 else c)
  _=lambda x1=0,y1=0,x2=128,y2=64,c=1:o.fill_rect(x1,y1,x2,y2,65535 if c==1 else c)
  r=lambda x1=0,y1=0,x2=128,y2=64,c=1:o.rect(x1,y1,x2,y2,65535 if c==1 else c)
  b=lambda f,x,y,a=-1,c=framebuf.FrameBuffer(bytearray([0,0,255,255]),2,1,framebuf.RGB565):o.blit(f,x,y,a,c)
  m=o.scroll
  c=int
  print('LCD READY')
  scrType='LCD'

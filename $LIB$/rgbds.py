import tft,scr
t=tft
def ds(f,x=0,y=0,m=640,w=1):
    dx,dy=f.readline().decode().split()
    dx,dy=int(dx),int(dy)
    if dy+y>160:dy-=y
    if dx+x>128:pass
    if w:
      t.setarea((x,y),(min(127,dx+x-1),min(159,dy+y-1)))
      t.dc(1)
    size=dx*dy*2
    print(dx,dy)
    m=min(size,m)
    try:
      for i in range(size//m):t.spi.write(f.read(m))
      t.spi.write(f.read(size%m))
    except:
      pass
rgb=lambda f,x=0,y=0:ds(open(f,'rb'),x,y)
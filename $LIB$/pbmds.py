import scr,framebuf
def info(f):
  try:
    f=open(f,'rb')
  except:
    f=open('null.pbm','rb')
  f.readline()
  l,h=f.readline().split()
  return f,int(l),int(h)
def dcd(f,v=-1,c=1):
  f,l,h=info(f)
  return getfb(f,l,h,v) if c else (getfb(f,l,h,v),l,h)
getfb=lambda f,x,y,v=-1:framebuf.FrameBuffer(bytearray(f.read(v)),x,y,framebuf.MONO_HLSB)
#ds=lambda f,x=0,y=0,a=-1:scr.b(dcd(f),x,y,a)
def ds(f,x=0,y=0,a=-1):
  f,l,h=dcd(f,c=0)
  scr._(x,y,l,h,1)
  scr.b(f,x,y,a)
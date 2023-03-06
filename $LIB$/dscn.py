import pbmds,scr,framebuf
dex,font,uns=open('c2k.lib'),open('c2k.bmf','rb'),0
def leng(t):
  k=0
  for i in t:
    k+=12 if isinstance(i,int) or len(i.encode())>len(i) else 8*len(i)
  return k
def tran(t,f=dex,s=100):
  if not isinstance(t,str):
    text=''
    for i in t:
      if isinstance(i,str):text+=i
      else:
        f.seek(i*3)
        text+=f.read(1)
    return text
  t=t.rstrip()
  if len(t)==len(t.encode()):return t
  f.seek(0);code,words,w=[],{'：':':','；':';','，':',','。':'.','？':'?','！':'!','”':'"','“':'"','《':'<','》':'>','、':',','·':'-','…':'...','「':'<','」':'>','—':'-'},1
  while w:
    w=f.read(s)
    for i in [n for n in t if n in w]:
      words[i]=f.tell()//3+w.index(i)-len(w)
  for i in t:
    if i in words:code+=[words[i]]
    else:code+=[i]
  del t
  return code
def dscd(code,x=0,y=0,f=font,mv=(0,3),bf=scr.o,a=0,c=65535,p=framebuf.FrameBuffer(bytearray([0,0,255,255]),2,1,framebuf.RGB565)):
  if isinstance(code,str):
    bf.text(code,x,y,c);return 8*len(code)
  for i in code:
    if isinstance(i,str):
      bf.text(i,x,y+mv[1],c);x+=8*len(i)
    else:
      f.seek(24*i)
      bf.blit(wdfb(f),x,y+mv[0],a,p);x+=12
  return x
wdfb=lambda f:pbmds.getfb(f,12,12,24)
cn=lambda t,x=0,y=0,f=dex,s=64:dscd(tran(t,f,s),x,y)

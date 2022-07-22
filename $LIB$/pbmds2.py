import scr,pbmds
def ds2(f,l,h,x=0,y=0,g=64):
  f.seek(0);f.readline();f.readline()
  i,k,m=0,y,l//8+(l%8>0)
  if y<0:
    f.seek(m*-y,1);k=0
  while k+i<g and i<h+min(0,y):
    scr.h(x,k+i,l,1)  
    scr.b(pbmds.getfb(f,l,1,m),x,k+i);i+=1

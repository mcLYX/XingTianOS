#FileNAME
import lstui,scr,touch,pbmds,pbmds2
def picv(f):
  mode,x,y,m,i=0,0,0,3,0
  f,l,h=pbmds.info(f)
  while 1:
    while touch.detect():
      x+=(0,0,0,-1,1)[mode]*m
      y+=(0,-1,1,0,0)[mode]*m
      scr.f(0)
      pbmds2.ds2(f,l,h,x,y)
      scr.s()
      scr.i(i)
    if touch.prstime()==0:
      scr.i(0);mode=lstui.lstui(([33,1791],[28,1791],[196,1791],[198,1791],[1791,1477],[128,451],[1381,293,'...']),[1674,2429],0)[1]+1
      if mode==5:
        m=(1,3,9,64)[lstui.lstui(([2346],[104],[734],[2481,350]),[1791,1477],0)[1]]
      if mode==6:
        i+=1
      if mode>6:
        scr.i(0);break
      if mode>4:
        mode=0
  f.close()
picv(FileNAME)
del picv
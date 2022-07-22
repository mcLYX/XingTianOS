#麻了，谁教教我排版咋写
from dscn import *
import scr,touch
def txtv(f):
  g=open(f)
  pagetxt=''
  linelen=[]
  curlen=0
  txtlen=0
  last=''
  while 1:
    scr.r(0,0,128,64,1)
    scr.s()
    load=g.read(1)
    if load and len(linelen)<5:
      if load=='\n':
        linelen+=[txtlen]
        curlen,txtlen=0,0
        continue
      elif load!='\r':
        pagetxt+=load
        curlen+=leng(load)
        txtlen+=1
        if curlen>128:
          linelen.append(txtlen-1)
          curlen,txtlen,last=leng(load),1,load
    else:
      if txtlen and not load:
        linelen.append(txtlen)
      if linelen:
        scr.f(0)
        code=tran(pagetxt)
        for i in range(5):
          dscd(code[sum(linelen[:i]):sum(linelen[:i+1])],0,i*13)
        scr.s()
        pagetxt=last if txtlen else ''
        linelen=[]
        if touch.prstime():
          break
      if load:
        if load not in ['\r','\n']:
          pagetxt+=load
          curlen+=leng(load)
          txtlen+=1
      else:
        break
  g.close()
  del pagetxt,linelen,code,g

from touch import prstime,detect
import time
slp=time.sleep
tk=time.ticks_ms
from scr import f,s,t,_
from dscn import leng,dscd,tran
c,l=dscd,leng
def lstui(fcs=[''],head='',fc=0,tr=0):
  if tr:fcs2,fcs,head=fcs,[(tran(i) if isinstance(i,str) else i) for i in fcs],tran(head) if isinstance(head,str) else head
  f(0);c(head,64-l(head)//2,0);t('-'*16,0,10)
  def lst(a,b,k):
    p=[fcs[fc%len(fcs)],fcs[(fc+1)%len(fcs)]]
    _(0,14,128,50,0)
    c(p[0],64-l(p[0])//2+a,18,mv=(-2,1));t('-'*16,0,26)
    c(p[1],int((64-l(p[1])/2)*(b/18)),36-b)
    for i in 2,3,4:c(fcs[(fc+i)%len(fcs)],0,27+i*9-k)
    s()
  while 1:
    lst(0,0,0)
    if prstime():return [fcs2[fc%len(fcs)] if tr else fcs[fc%len(fcs)],fc%len(fcs)]
    else:
      t1=tk()
      while tk()-t1<64:lst(int(2*(tk()-t1)),(tk()-t1)//4,(tk()-t1)//8)
      fc+=1
def ime(w=''):
  sel,stat=0,0
  while 1:
    f(0)
    for i in range(32,128):
      t(chr(i),(i-32)%16*8,(i-32)//16*9)
    t('_',sel%16*8,sel//16*9+1);t(w,0,54);t(str(stat%4),120,54);s()
    if prstime():stat+=1
    elif stat%4<2:sel+=2**(stat%4*4)
    elif stat%4==2:w=w+chr(sel+32) if sel<95 else w[:-1]
    else:return w
    sel=sel%96
def qna(text=[''],opt=('','')):
  f(0);c([116,1131]+list(opt[0]),0,39);c([1179,2229]+list(opt[1]),0,51)
  for i in range(len(text)):
    c(text[i],0,i*12)
  s();return prstime()

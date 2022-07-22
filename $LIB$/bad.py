#传入参数：FileNAME
from scr import s,h
import time,touch,lstui
def v(v):
  global rt
  for i in range(32):
    h(0,2*i,128,0)
  for i in range(0,len(v)-2,3):
    h(2*(v[i]-16),2*(v[i+1]-16),2*(v[i+2]-16),1)
  if avg<100:
    s()
    while time.ticks_ms()-rt<45:pass
  for i in range(32):
    h(0,2*i+1,128,0)
  for i in range(0,len(v)-2,3):
    h(2*(v[i]-16),2*(v[i+1]-16)+1,2*(v[i+2]-16),1)
  s()
  #while time.ticks_ms()-rt<90:pass
def play(fi):
  global avg,rt
  g,a=open(fi,'rb'),0
  while touch.detect():
    pass
  rt=time.ticks_ms()
  for i in g:
    a+=1
    avg=(time.ticks_ms()-rt)//a
    if avg<101:v(i)
    while avg<99:avg=(time.ticks_ms()-rt)//a
    print(avg)
    if touch.detect():
      if lstui.qna([[58,1978,1806]],([1381,293],[1699,1905])):
        g.close();break
      a,rt=0,time.ticks_ms()
play(FileNAME)
del play,v
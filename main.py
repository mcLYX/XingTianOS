import os
os.chdir('/$LIB$')
import dstxt,network,config,volt
#if volt.volt()==65535:
#  dstxt.en('Debug Mode',0);raise
import scr,time,machine,pbmds,PRECONFIG
machine.Pin(15,machine.Pin.OUT).off()
machine.Pin(14,machine.Pin.OUT,machine.Pin.PULL_DOWN).off()
home=config.read('Home')
scr.c(int(config.read('Brightness')))
machine.freq(int(config.read('Freq')))
try:
  pbmds.ds('xtos.pbm',a=1);scr.s()
  tq=0;tqs=[0]
  for i in range(99):
    v=volt.volt()
    tq+=v
    tqs.append(v)
    time.sleep(.009)
  tqs=max(tqs)
  tq//=77
  if isinstance(PRECONFIG.TQ_VOLT,float):
      PRECONFIG.TQ_VOLT=min(65535,tq+tqs//1.5)
  print('Avg:',tq,'Max:',tqs,'Set:',PRECONFIG.TQ_VOLT)
  scr.t(str(tq)+' '+str(tqs),0,0);scr.s()
  del tq,tqs
except:
  pass
try:
  exec('import '+home)
except Exception as e:
  machine.Pin(15,machine.Pin.OUT).on()
  dstxt.en(' :('+' '*29+str(e),1)

import os
os.chdir('/$LIB$')
import volt,dstxt,network,config
if volt.volt()==65535:
  dstxt.en('Debug Mode',0);x
import scr,time,machine,pbmds
machine.Pin(12,machine.Pin.OUT).off()
machine.Pin(13,machine.Pin.OUT).off()
#try:
#  open('crash')
#  exec('import '+c)
#except:
home=config.read('Home')
scr.c(int(config.read('Brightness')))
machine.freq(int(config.read('Freq')))
try:
  pbmds.ds('xtos.pbm',a=1);scr.s();time.sleep(1)
except:
  pass#import rgbds;rgbds.rgb('$USR$/Yanfei.rgb')
try:
  exec('import '+home)
except Exception as e:
  machine.Pin(12,machine.Pin.OUT).on()
  machine.Pin(13,machine.Pin.OUT).on()
  dstxt.en(' :('+' '*29+str(e),1)

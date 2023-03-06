import lstui,network,time,scr,config
from dscn import dscd
scr.f(0);dscd([2174,9,448,1541]);scr.s();time.sleep(1)
ssid=lstui.ime()
if ssid:
  scr.f(0);dscd([2174,9,1887,865]);scr.s();time.sleep(1)
  pswd=lstui.ime()
  if pswd:
    if 7<len(pswd)<17:
      network.WLAN(network.AP_IF).config(essid=ssid,authmode=4,password=pswd)
      config.write('Hotspot',ssid+'\n'+pswd);scr.f(0);dscd([735,358]);scr.s();time.sleep(1)
    else:
      scr.f(0);dscd([1887,865,75,1604]);scr.s();time.sleep(1)
  else:
    network.WLAN(network.AP_IF).config(essid=ssid,authmode=0)
    config.write('Hotspot',ssid+'\n');scr.f(0);dscd([735,358]);scr.s();time.sleep(1)
else:
  scr.f(0);dscd([448,1541,75,1604]);scr.s();time.sleep(1)

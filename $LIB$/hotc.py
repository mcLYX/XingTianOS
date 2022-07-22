import lstui,network,time,scr
from dscn import dscd
scr.f(0);dscd([2174,9,448,1541]);scr.s();time.sleep(1)
ssid=lstui.ime()
if ssid:
  scr.f(0);dscd([2174,9,1887,865]);scr.s();time.sleep(1)
  pswd=lstui.ime()
  if pswd:
    if 7<len(pswd)<17:
      network.WLAN(network.AP_IF).config(essid=ssid,authmode=network.AUTH_WPA_WPA2_PSK, password=pswd)
      scr.f(0);dscd([735,358]);scr.s();time.sleep(1)
    else:
      scr.f(0);dscd([1887,865,75,1604]);scr.s();time.sleep(1)
  else:
    network.WLAN(network.AP_IF).config(essid=ssid,authmode=0)
    scr.f(0);dscd([735,358]);scr.s();time.sleep(1)
else:
  scr.f(0);dscd([448,1541,75,1604]);scr.s();time.sleep(1)

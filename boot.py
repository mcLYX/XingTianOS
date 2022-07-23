# This file is executed on every boot (including wake-boot from deepsleep)\n#import esp\n#esp.osdebug(None)\n
import webrepl,gc,network
webrepl.start()
network.WLAN(network.STA_IF).active(True)
network.WLAN(network.AP_IF).active(True)
#cfg=eval(open('$LIB$/cfg.txt').readline())
wifif=open('/$DAT$/Config/BootWifi')
hsf=open('/$DAT$/Config/Hotspot')
wssid=wifif.readline().rstrip()
wpswd=wifif.readline()
hssid=hsf.readline().rstrip()
hpswd=hsf.readline()
wifif.close()
hsf.close()
network.WLAN(network.STA_IF).connect(wssid,wpswd)
#network.WLAN(network.STA_IF).connect('','')
network.WLAN(network.AP_IF).config(essid=hssid,authmode=0)
del cfg,network,webrepl,essid,wpswd,hssid,hpswd
gc.collect()
# This file is executed on every boot (including wake-boot from deepsleep)\n#import esp\n#esp.osdebug(None)\n
import webrepl,gc,network,machine
machine.Pin(15,machine.Pin.OUT).on()

wifif=open('/$DAT$/Config/BootWifi')
hsf=open('/$DAT$/Config/Hotspot')
wssid=wifif.readline().rstrip()
wpswd=wifif.readline()
hssid=hsf.readline().rstrip()
hpswd=hsf.readline()
wifif.close()
hsf.close()
try:wireless=eval(open('/$DAT$/Config/Wireless').read())
except:wireless=True
network.WLAN(network.AP_IF).config(essid=hssid,authmode=4 if hpswd else 0,password=hpswd)
#network.phy_mode(1)
if wireless:
    network.WLAN(network.STA_IF).active(True)
    network.WLAN(network.AP_IF).active(True)
    network.WLAN(network.STA_IF).connect(wssid,wpswd)
    webrepl.start()
else:
    network.WLAN(network.STA_IF).active(False)
    network.WLAN(network.AP_IF).active(False)
machine.Pin(14,machine.Pin.OUT).off()
machine.Pin(15,machine.Pin.OUT).off()
del network,webrepl,wssid,wpswd,hssid,hpswd,wifif,hsf,wireless
gc.collect()
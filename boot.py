# This file is executed on every boot (including wake-boot from deepsleep)\n#import esp\n#esp.osdebug(None)\n
import webrepl,gc,network,machine,btree
machine.Pin(15,machine.Pin.OUT).on()
config=open('/$DAT$/Config.db','r+b')
db=btree.open(config)

wifif=db['BootWifi'].decode().split('\n')
hsf=db['Hotspot'].decode().split('\n')
wssid,wpswd=wifif
hssid,hpswd=hsf

try:wireless=eval(open(db['Wireless'].decode()).read())
except:wireless=True

db.close()
config.close()

network.WLAN(network.AP_IF).config(essid=hssid,authmode=4 if hpswd else 0,password=hpswd)
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

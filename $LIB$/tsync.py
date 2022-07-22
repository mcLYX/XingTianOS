import ntptime,network,time
from scr import s,f
from dscn import dscd

if network.WLAN(network.STA_IF).isconnected():
  f(0);dscd([380,611,104,'...']);s();time.sleep(1)
  ntptime.NTP_DELTA=3155644800
  ntptime.host='ntp1.aliyun.com'
  try:
    ntptime.settime()
    f(0);dscd([735,358,'!']);s();time.sleep(1)
  except:
    f(0);dscd([394,1412,2200,1376]);s();time.sleep(1)
else:
  f(0);dscd([178,1942,394,'!']);s();time.sleep(1)


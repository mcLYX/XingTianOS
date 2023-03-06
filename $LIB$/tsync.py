import ntptime,network,time,machine
from scr import s,f
from dscn import dscd
from PRECONFIG import TIME_ZONE

if network.WLAN(network.STA_IF).isconnected():
  f(0);dscd([380,611,104,'...']);s();time.sleep(1)
  #ntptime.NTP_DELTA=3155644800#奇怪了这玩意为啥没用了
  ntptime.host='ntp1.aliyun.com'
  try:
    ntptime.settime()
    curtime=list(machine.RTC().datetime())
    curtime[4]+=TIME_ZONE
    machine.RTC().datetime(curtime)
    f(0);dscd([735,358,'!']);s();time.sleep(1)
  except:
    f(0);dscd([394,1412,2200,1376]);s();time.sleep(1)
else:
  f(0);dscd([178,1942,394,'!']);s();time.sleep(1)


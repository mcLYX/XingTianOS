import lstui,network,time,scr,config,os
sta=network.WLAN(network.STA_IF)
from dscn import dscd
wifidir='../$DAT$/SavedWifi/'
if lstui.qna([['Wi-Fi',494,2197]],[[325,1707],[1156,1236,58,348]]):
    scr.f(0);dscd([182,345,325,1707,'Wi-Fi...']);scr.s()
    sta.active(True)
    try:
      signal,wifi=[],sta.scan()
      if not wifi:
        sta.active(False)
        time.sleep(1)
        sta.active(True)
        time.sleep(1)
        wifi=sta.scan()
      for i in range(len(wifi)):
        name=wifi[i][0].decode()
        #name=name[2:len(name)-1]
        if name:signal.append(name)
      cnkt=lstui.lstui(['退出...']+signal,'Wi-Fi',0,1)
      if cnkt[0]!='退出...':
          scr.f(0);dscd([2174,9,1887,865]);scr.s();time.sleep(1)
          pswd=lstui.ime()
          scr.f(0);dscd([610,1721,104,'...']);scr.s();sta.connect(cnkt[0],pswd);wait=0
          while wait<9 and not sta.isconnected():
            time.sleep(2);wait+=1
          if sta.isconnected():
            scr.f(0);dscd([58,610,1721]);scr.s();time.sleep(1)
            wifi=os.listdir(wifidir)
            if len(wifi)<9 or cnkt[0] in wifi:
                sav=open(wifidir+cnkt[0],'w')
                sav.write(pswd)
                sav.close()
          else:
            scr.f(0);dscd([610,1721,1922,616]);scr.s();time.sleep(1)
    except:
      scr.f(0);dscd([592,620,729,1691,394,'?']);scr.s();time.sleep(1)
    del wifi,signal
else:
    wifi=os.listdir(wifidir)
    if wifi:
      sta.active(False)
      ssid=lstui.lstui(wifi,[58,348],0)[0]
      sta.active(True)
      print(ssid)
      sel=lstui.lstui([[610,1721],[1255,762],[692,1389],[494,152,2437,158],[1381,293]],ssid,0)[1]
      if sel==0:sta.connect(ssid,open(wifidir+ssid).read())
      elif sel==1:
          pswd=lstui.ime()
          sav=open(wifidir+ssid,'w')
          sav.write(pswd)
          sav.close()
      elif sel==2:
          os.remove(wifidir+ssid)
          if config.read('BootWifi').split()[0]==ssid:config.write('BootWifi','')
      elif sel==3:config.write('BootWifi',ssid+'\n'+open(wifidir+ssid).read())

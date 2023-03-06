import lstui,scr,machine,config,rd,network
sel=0
while 1:
  sel=lstui.lstui(([75,1089],[616,717],['OLED',1303,1304],[267,1205,1173,'UI'],
                   ['CPU',616,1229,1477,1304],[1635,566],['LCD',2104,35,667,2197],['LCD',150,425],[472,20],[1381,293,'...']),[494,2197],sel)[1]
  if sel==0:
    subsel=lstui.lstui([[610,1721,'Wi-Fi'],[1449,1184],[744,252],[2154,252],[675,389,'...']],[75,1089],0)[1]
    if subsel==0:
      exec(open('wific.py').read(),{})
    elif subsel==1:
      exec(open('hotc.py').read(),{})
    elif subsel in (2,3):
      network.WLAN(network.STA_IF).active(bool(subsel-3))
      network.WLAN(network.AP_IF).active(bool(subsel-3))
      config.write('Wireless',str(bool(subsel-3)))
  elif sel==1:
      if lstui.qna([[616,717]],[[112,313,494,2197],[1942,394,1459,831]]):
          try:
            setTime=int(lstui.ime('Year:20')[5:]),int(lstui.ime('Month:')[6:]),int(lstui.ime('Day:')[4:]),0,int(lstui.ime('Hour:')[5:]),int(lstui.ime('Minute:')[7:]),0,0
            machine.RTC().datetime(setTime)
            del setTime
          except:print('无效时间')
      else:exec(open('tsync.py').read(),{})
  elif sel==2:
    nv=(1,31,79,143,255)[lstui.lstui(([1989,664],[664],[104],[1594],[1989,1594]),[1303,1304],4)[1]]
    config.write('Brightness',nv)
    scr.c(nv)
  elif sel==3:config.write('Home',('nhome\n','home\n','homeplus\n')[lstui.lstui(([[920,1151,'UI'],[356,798,'UI'],[920,1151,'UI Plus']]),[267,1205,1173,'UI'])[1]])#('Home','nhome\n'if lstui.qna([[267,1205,1173,'UI']],([920,1151,'UI'],[356,798,'UI']))else'home\n')
  elif sel==4:
    machine.freq(240000000 if lstui.qna([['CPU',616,1229,1477,1304]],('240MHz','80MHz'))else 80000000)
    config.write('Freq',machine.freq())
  elif sel==5:config.write('AntiJoggle',str((0,3,5,9)[lstui.lstui(([472],[664],[104],[1594]),[1635,566],0)[1]]))
  elif sel==7:
    rot=lstui.lstui(('0','1','2','3'),['LCD',150,425])[1]
    config.write('Rot',('0','1','2','3')[rot])
    try:
      import tft
      tft.tft.rotation(rot)
      tft.setOffset(rot)
    except:
      pass
  elif sel==8:exec(open('about.py').read(),{})
  elif sel==6:
    try:
      from PRECONFIG import LCD_SIZE as size
      scr.pos=(((0,0),(127,63)), ((size[0]//2-64,0),(size[0]//2+63,63)), ((size[0]-128,0),(size[0]-1,63)),
               ((0,size[1]//2-32),(127,size[1]//2+31)), ((size[0]//2-64,size[1]//2-32),(size[0]//2+63,size[1]//2+31)), ((size[0]-128,size[1]//2-32),(size[0]-1,size[1]//2+31)),
               ((0,size[1]-64),(127,size[1]-1)), ((size[0]//2-64,size[1]-64),(size[0]//2+63,size[1]-1)), ((size[0]-128,size[1]-64),(size[0]-1,size[1]-1))
               )[lstui.lstui(
                   ([196,33],[812,1612],[198,33],
                    [196,150],[104,717],[198,150],
                    [196,28],[996,1612],[198,28]),
                   ['LCD',2104,35,667,2197],rd.rdi(0,8))[1]]
      scr.tft.fill()
    except:pass
  else:
    break
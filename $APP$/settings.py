import lstui,scr,machine,config
sel=0
while 1:
  sel=lstui.lstui(('Wi-Fi',[1449,1184],[616,717,380,611],[1303,1304],[267,1205,1173],
                   [297,1477,2287,311],[472,20],'LCD DispPos',[675,389,'...']),[494,2197],sel)[1]
  if sel==0:exec(open('wific.py').read())
  elif sel==1:exec(open('hotc.py').read())
  elif sel==2:exec(open('tsync.py').read(),{})
  elif sel==3:
    nv=(1,31,79,143,255)[lstui.lstui(([1989,664],[664],[104],[1594],[1989,1594]),[1303,1304],4)[1]]
    config.write('Brightness',nv)
    scr.c(nv)
  elif sel==4:
    config.write('Home','nhome\n'if lstui.qna([[267,1205,1173,494,2197]],([936,252,920,1151,1205,1173],[936,252,356,798,1205,1173]))else'home\n')
  elif sel==5:
    machine.freq(160000000 if lstui.qna([[297,1477,2287,311]],([72],[472]))else 80000000)
    config.write('Freq',machine.freq())
  elif sel==6:
    exec(open('about.py').read())
  elif sel==7:
    try:
      scr.pos=(((0,0),(127,63)), ((0,48),(127,111)), ((0,96),(127,159)))[lstui.lstui(('UPPER','MIDDLE','BOTTOM'),'LCD DispPos')[1]]
      scr.tft.fill()
    except:pass
  else:
    break

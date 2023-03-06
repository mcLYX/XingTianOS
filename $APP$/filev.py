import pbmds,lstui,scr,touch,os,dscn,time
t=(0,0)
d='/'if touch.d()else'../$USR$/'
while 1:
    t=lstui.lstui(([430,1612],[920,119],[313,857],[1313,255],[148,1465],[1381,293,'...']),[148,413,1325,1107,'(ROOT)'if d=='/'else''],t[1])
    if t[1]<5:
      fi,g=(0,0),[];scr.f(0);dscn.dscd([297,1432,104,'...']);scr.s()
    if 0<t[1]<5:
      for i in os.listdir(d):
        j=i.split('.')[-1]
        if j in(['bmp','pbm','rgb','qoi','jpg'],['hla','zla'],['pwm'],['txt'])[t[1]-1]:
          g.append(i)
    elif t[1]==0:
      types=[]
      osdir=os.listdir(d)
      for i in osdir:
          j=i.split('.')[-1]
          if j not in types:
              types.append(j)
      t=lstui.lstui(types,[148,413,1325,1107],0)
      for i in osdir:
        j=i.split('.')[-1]
        if j==t[0]:
          g.append(i)
    else:break
    while g:
      scr.f(0);dscn.dscd([297,1432,104,'...']);scr.s()
      fi,a=lstui.lstui(g+[[1381,293,'...']],t[0],fi[1],1),0
      if fi[0]==[1381,293,'...']:break
      else:fd=d+fi[0]
      print(fd)
      fn=fi[0].split('.')[-1]
      try:
        open(fd).close()
      except:
        d='/'+fd+'/'
        g=os.listdir(d)
        continue
      try:
        if fn in ['pbm','ic']:
          exec(open('../$LIB$/picv.py').read(),{'FileNAME':fd})
        elif fn in ('hla','zla'):
          exec(open('../$LIB$/bad.py').read(),{'FileNAME':fd})
        elif fn=='pwm':
          exec(open('../$LIB$/ysjd.py').read(),{'FileNAME':fd})
        elif fn=='txt':
          import txtv;txtv.txtv(fd)
        elif fn=='bmp':
          import bmpds;bmpds.bmp(fd)
        elif fn=='rgb':
          import rgbds;scr.f(0);scr.s();rgbds.rgb(fd);touch.prstime()
        elif fn=='qoi':
          import qoidsx;qoidsx.ds(fd)#;exec(open('../$LIB$/qoids.py').read(),{'FileNAME':fd})
        elif fn=='py':
          exec(open(fd).read(),{})
        elif fn=='jpg':
          import tft
          spd=time.ticks_ms()
          try:
            tft.tft.jpg(fd,0,0,0)
          except:
            tft.tft.jpg(fd,0,0,1)
          print(time.ticks_ms()-spd)
          touch.prstime()
      except:
        pass
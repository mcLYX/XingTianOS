import pbmds,lstui,scr,touch,os,dscn
t=(0,0)
d='/'if touch.d()else'../$USR$/'
while 1:
    t=lstui.lstui(([430,1612],[920,119],[313,857],[1313,255],[148,1465],[1381,293,'...']),[148,413,1325,1107,'(ROOT)'if d=='/'else''],t[1])
    if t[1]<5:
      fi,g=(0,0),[];scr.f(0);dscn.dscd([297,1432,104,'...']);scr.s()
    if 0<t[1]<5:
      for i in os.listdir(d):
        j=i.split('.')[-1]
        if j in(['bmp','pbm','rgb'],['hla'],['pwm'],['txt'])[t[1]-1]:
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
    for i in range(len(g)):g[i]=dscn.tran(g[i])
    while g:
      scr.f(0);dscn.dscd([297,1432,104,'...']);scr.s()
      fi,a=lstui.lstui(g+[[1381,293,'...']],t[0],fi[1]),0
      if fi[0]==[1381,293,'...']:break
      else:
        if isinstance(fi[0],list):fi[0]=dscn.tran(fi[0])
        fd=d+fi[0]
      print(fd)
      fn=fi[0][-4:]
      try:
        open(fd).close()
      except:
        d='/'+fd+'/'
        g=os.listdir(d)
        continue
      if fn=='.pbm'or '.ic'in fn:
        exec(open('../$LIB$/picv.py').read(),{'FileNAME':fd})
      elif fn=='.hla':
        exec(open('../$LIB$/bad.py').read(),{'FileNAME':fd})#import bad;bad.play(fd)
      elif fn=='.pwm':
        exec(open('../$LIB$/ysjd.py').read(),{'FileNAME':fd})#import ysjd;ysjd.play(fd)
      elif fn=='.txt':
        import txtv;txtv.txtv(fd)
      elif fn=='.bmp':
        import bmpds;bmpds.bmp(fd)
      elif fn=='.rgb':
        import rgbds;scr.f(0);scr.s();rgbds.rgb(fd)
        if touch.prstime():rgbds.rgb(fd,0,63)
      elif '.py'in fn:
        try:
          exec(open(fd).read(),{})
        except:
          pass
    #del t,fi,g,fn

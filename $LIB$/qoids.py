#打开文件,传入FileNAME

import os,time,touch,tft,scr
f=open(FileNAME,'rb')
scr.f(0);scr.s()

#解码配置设置
bytemin=8#加载的最少字节数(8,不要改,除非QOI规范变了)
loadstep=96#每次加载多少字节，更改可能影响速度
cachesize=64#解码后的缓存大小，更改可能影响速度
cache565=b''#16位色缓存
dat=bytearray(2)

def rgb565(bgr=None):
  global cache565,dat
  if not bgr:
    tft.dc(1)
    try:
      tft.spi.write(cache565)
      del cache565
    except:
      pass
    return

  color=((bgr[0] & 0xF8) << 8) | ((bgr[1] & 0xFC) << 3) | (bgr[2] >> 3)
  dat[0]=color>>8
  dat[1]=color
  cache565+=dat
  if len(cache565)>=cachesize:
    tft.dc(1)
    tft.spi.write(cache565)
    cache565=b''
    
t=time.ticks_ms()

#检测文件头
if f.read(4)!=b'qoif':
  f.close()
  del f
  print('不是一个有效的QOI文件')
else:
  #获取图像信息
  w=f.read(4)
  width=(w[0]<<24)+(w[1]<<16)+(w[2]<<8)+w[3]
  h=f.read(4)
  height=(h[0]<<24)+(h[1]<<16)+(h[2]<<8)+h[3]
  channels=f.read(1)[0]
  colorspace=f.read(1)[0]#这玩意干啥的？？
  print(width,height,channels)
  scr.t('Width:'+str(width),0,9)
  scr.t('Height:'+str(height),0,18)
  scr.t('Depth:'+str(channels*8),0,27)
  scr.t('Size:'+("%.2f"%(os.stat(FileNAME)[6]/1024))+'KB',0,54)
  scr.s()
  tft.setarea([0,0],[width-1,height-1])
  channels=3#强制RGB

  #创建index
  index=bytearray(64*4)
  
  #开始图像数据解码
  byte=bytearray(f.read(loadstep))
  rgba=bytearray((0,0,0,255))
  
  while byte:
    
    byte+=bytearray(f.read(loadstep))
    
    while len(byte)>bytemin:
      if byte[0]>=0b11111110:#RGB(A)
        rgba=byte[1:byte[0]-250]+(rgba[-1:] if (byte[0]-255) else b'')
        byte=byte[byte[0]-250:]
        
      elif (byte[0]>>6)==0:#INDEX
        indexp=byte[0]&0b00111111
        rgba=index[indexp*4:(1+indexp)*4]
        byte=byte[1:]
        
      elif (byte[0]>>6)==1:#DIFF
        rgba=bytearray(((rgba[-4] + (byte[0]>>4)%4-2) %256,(rgba[-3] + (byte[0]>>2)%4-2) %256,(rgba[-2] + byte[0]%4-2) %256,rgba[-1]))
        byte=byte[1:]
        
      elif (byte[0]>>6)==2:#LUMA
        dg=byte[0]%64-32
        dr,db=(byte[1]>>4)+dg-8,(byte[1]%16)+dg-8
        rgba=bytearray(((rgba[-4] + dr) %256,(rgba[-3] + dg) %256,(rgba[-2] + db) %256,rgba[-1]))
        byte=byte[2:]
        
      elif (byte[0]>>6)==3:#RUN
        for i in range(byte[0]%64):
          rgb565(rgba)
        byte=byte[1:]
        
      #写入INDEX
      if rgba:
        indexp=(rgba[-4]*3+rgba[-3]*5+rgba[-2]*7+rgba[-1]*11)%64
        index[indexp*4:indexp*4+4]=rgba
        rgb565(rgba)

      #解码完毕
      if len(byte)==8 and byte==b'\x00'*7+b'\x01':
        rgb565()
        f.close()
        byte=b''
        print('OK')

print(time.ticks_ms()-t)
touch.prstime()

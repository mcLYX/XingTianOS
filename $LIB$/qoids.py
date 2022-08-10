#打开文件,传入FileNAME

import os,time,touch,tft,scr
f=open(FileNAME,'rb')
scr.f(0);scr.s()

#解码配置设置
bytemin=8#加载的最少字节数(8,不要改,除非QOI规范变了)
loadstep=96#每次加载多少字节，更改可能影响速度
cachesize=64#解码后的缓存大小，更改可能影响速度
#cache=b''#24/32位色缓存
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
  del w
  h=f.read(4)
  height=(h[0]<<24)+(h[1]<<16)+(h[2]<<8)+h[3]
  del h
  tft.setarea([0,0],[width-1,height-1])
  channels=f.read(1)[0]
  colorspace=f.read(1)[0]#这玩意干啥的？？
  print(width,height,channels)
  channels=3#强制RGB

  #创建index
  index=bytearray(64*4)
  
  #开始图像数据解码
  byte=bytearray(f.read(loadstep))
  rgba=b''
  
  while byte:
    
    byte+=bytearray(f.read(loadstep))
    
    while len(byte)>bytemin:
      if byte[0]==0b11111110:#RGB
        rgba=byte[1:4]+(rgba[-1:] if len(rgba)==4 else b'\xff')
        #cache+=rgba[:channels]
        byte=byte[4:]
        #input('Detected RGB')
        
      elif byte[0]==0b11111111:#RGBA
        rgba=byte[1:5]
        #cache+=rgba[:channels]
        byte=byte[5:]
        #input('Detected RGBA')
        
      elif (byte[0]>>6)==0:#INDEX
        indexp=byte[0]&0b00111111
        rgba=index[indexp*4:(1+indexp)*4]
        #cache+=rgba[:channels]
        #del byte[0]
        byte=byte[1:]
        #input('Detected INDEX')
        
      elif (byte[0]>>6)==1:#DIFF
        #indexp=len(cache)-channels-1
        prev=rgba
        rgba=bytes([(prev[-4] + (byte[0]>>4)%4-2) %256])
        rgba+=bytes([(prev[-3] + (byte[0]>>2)%4-2) %256])
        rgba+=bytes([(prev[-2] + byte[0]%4-2) %256])
        rgba+=bytes([prev[-1]])
        #cache+=rgba[:channels]
        #del byte[0]
        byte=byte[1:]
        #input('Detected DIFF')
        
      elif (byte[0]>>6)==2:#LUMA
        #indexp=len(cache)-channels-1
        prev=rgba
        dg=byte[0]%64-32
        dr,db=(byte[1]>>4)+dg-8,(byte[1]%16)+dg-8
        rgba=bytes([(prev[-4] + dr) %256])
        rgba+=bytes([(prev[-3] + dg) %256])
        rgba+=bytes([(prev[-2] + db) %256])
        rgba+=bytes([prev[-1]])
        #cache+=rgba[:channels]
        #del byte[0:2]
        byte=byte[2:]
        #input('Detected LUMA')
        
      elif (byte[0]>>6)==3:#RUN
        prev=rgba
        for i in range(byte[0]%64+1):
          rgba=prev[-4:] if prev else b'\x00'*4
          #cache+=rgba[:channels]
          if i:rgb565(rgba)

        byte=byte[1:]
        #input('Detected RUN')
        
      #写入INDEX
      if rgba:
        indexp=(rgba[-4]*3+rgba[-3]*5+rgba[-2]*7+rgba[-1]*11)%64
        index[indexp*4:indexp*4+4]=rgba
        rgb565(rgba)
        
      #满缓存
      '''
      if len(cache)>=cachesize:
        cache=cache[loadstep:]
      '''
      
      #解码完毕
      if len(byte)==8 and byte==b'\x00'*7+b'\x01':
        rgb565()
        f.close()
        byte=b''
        #del cache
        print('OK')

print(time.ticks_ms()-t)
touch.prstime()

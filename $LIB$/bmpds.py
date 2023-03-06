import tft
import dscn,scr,os

def bmp(fn,r=2,cd=0):
  try:
    scr.f(0)
    dscn.cn('传输中...')
    scr.s()
  except:
    print('Transporting...')
  f=open(fn, 'rb')
  if f.read(2) == b'BM':  #header
    dummy = f.read(8) #file size(4), creator bytes(4)
    offset = int.from_bytes(f.read(4), 'little')
    hdrsize = int.from_bytes(f.read(4), 'little')
    width = int.from_bytes(f.read(4), 'little')
    height = int.from_bytes(f.read(4), 'little')
    if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
      depth = int.from_bytes(f.read(2), 'little')
      if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
        print("Image size:", width, "x", height)
        rowsize = (width*3+3) & ~3
        if height < 0:
          height = -height
          flip = False
        else:
          flip = True
        w,h=width,height
        w,h=min(128,w),min(160,h)
        tft.setarea((0,0),(w - 1,h - 1))
        if cd:
            f2=open(fn.split('.')[0]+'.rgb','wb')
            f2.write((str(width)+' '+str(height)+'\n').encode())
        for row in range(h):
          pos=offset+(height-1-row)*rowsize if flip else offset+row*rowsize
          if f.tell() != pos:
            dummy = f.seek(pos)
          for col in range(w):
            bgr = f.read(3)
            dat=bytearray(2)
            color=((bgr[2] & 0xF8) << 8) | ((bgr[1] & 0xFC) << 3) | (bgr[0] >> 3)#TFTColor(bgr[2],bgr[1],bgr[0])
            dat[0]=color>>8
            dat[1]=color
            tft.dat(dat)
            if cd:f2.write(dat)
  if cd:
      f2.close()
      os.remove(fn)

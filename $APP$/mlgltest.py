import mlgl,_scr,framebuf,tft,random,time
a=tft.tft.jpg_decode('../$USR$/瑶瑶.jpg')
yao=framebuf.FrameBuffer(a[0],240,240,framebuf.RGB565)
bg=mlgl.Spirit(yao,_scr.o)
t=time.ticks_ms()
del yao
fps=0
for i in range(2000):
    t1=time.ticks_ms()
    _scr.f(0)
    bg.blit()
    _scr.t('Frame:'+str(i+1),0,0)
    _scr.t('FPS:'+str(fps),0,9)
    _scr.s()
    if i%20==0:
        bg.moveEvent(random.randint(-240,240),random.randint(-240,240),random.randint(500,800),i//20%2+3)
    fps=round(1000/(time.ticks_ms()-t1),2)
print('avg fps:',2000/(time.ticks_ms()-t)*1000)
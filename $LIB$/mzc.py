# mld bpm
from machine import Pin,PWM
from time import sleep_ms as slp
import touch
# 设置D8（GPIO 15）口为IO输出，通过PWM控制蜂鸣器发声
tones={'1': 262, '2': 294, '3': 330, '4': 349, '5': 392, '6': 440, '7': 494,' ':[],'a':523,'b':587,'0': 0,'c':659,'d':698,'e':784,'f':880,'g':988,'h':1000,'u':'1','v':'1.5','z':'2','y':"4",'x':'8','w':'16'}
def mzc(mld,bpm):
  global tones
  dur,bar,bp,p0=1,0,PWM(Pin(12, Pin.OUT), freq=1, duty=1023),Pin(2,Pin.OUT)
  for t in mld:
    freq=tones[t]
    if isinstance(freq,int):
      if freq==0:
        bp.duty(0);print('Empty')# 空拍时不上电
      else:
        bp.init(duty=1000, freq=freq);p0.off();print('Freq=',freq)# 调整PWM的频率，使其发出指定的音调
    else:
      if isinstance(freq,str):
        dur=4/float(freq);print('Duration:1/'+freq)# 调整时值
      else:
        bar+=1;print('Current bar:',bar)# 小节数+1
      continue
    slp(int(800*(60/bpm)*dur))# 声音持续时长
    bp.duty(0)  # 设备占空比为0，即不上电
    p0.on() # 灭灯
    slp(int(199*(60/bpm)*dur))# 停顿时长
    if touch.d():break
  bp.deinit()  # 释放PWM
mzc(mld,bpm)
del mzc
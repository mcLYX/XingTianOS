from machine import Pin, I2C
import time
import machine
class RDA5807(object):
  def __init__(self,scl=8,sda=9):
    self.i2c = I2C(scl=Pin(scl),sda=Pin(sda))
    self.i2c_buf = bytearray(2)
    self.i2c_buf4 = bytearray(4)
    self.is_mute = 0
    self.rssi = 0
    self.tune = 0

  def next_sta(self): #向下搜台
    self.i2c_buf[0] = 0xd3
    self.i2c_buf[1] = 0x81
    self.i2c.writeto(0x10, self.i2c_buf)

  def pro_sta(self): #向上搜台
    self.i2c_buf[0] = 0xd1
    self.i2c_buf[1] = 0x81
    self.i2c.writeto(0x10, self.i2c_buf)

  def set_ch(self, ch): #设置频率eg. 965  unit 100KHz
    self.i2c_buf4[0] = 0xd0
    self.i2c_buf4[1] = 0x01
    ch -= 870
    self.i2c_buf4[2] = ((ch >> 2) & 0xff)
    self.i2c_buf4[3] = ((ch << 5) & 0xff)
    self.i2c.writeto(0x10, self.i2c_buf4)
    self.refresh_info()

  def refresh_info(self):  #获取当前频率，信号强度等
    self.i2c.readfrom_into(0x11, self.i2c_buf4)
    self.tune = 870 + self.i2c_buf4[1]
    self.rssi = self.i2c_buf4[2] >> 1
    print(self.tune,self.rssi)

  def mute(self): #静音/取消静音
    if self.is_mute == 1:
      self.i2c_buf[0] = 0xd0
      self.is_mute = 0
    else:
      self.i2c_buf[0] = 0x90
      self.is_mute = 1

    self.i2c_buf[1] = 0x01
    self.i2c.writeto(0x10, self.i2c_buf)

#Thanks to 我是鹏老师 https://www.bilibili.com/read/cv13860007?from=search&spm_id_from=333.337.0.0 出处：bilibili
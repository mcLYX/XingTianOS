#From boochow/ST7735.py
import time
_reset()

com(1)              #Software reset.
time.sleep_us(150)
com(17)               #out of sleep mode.
time.sleep_us(255)

data3 = bytearray([0x01, 0x2C, 0x2D])       #fastest refresh, 6 lines front, 3 lines back.
com(177)              #Frame rate control.
dat(data3)

com(178)              #Frame rate control.
dat(data3)

data6 = bytearray([0x01, 0x2c, 0x2d, 0x01, 0x2c, 0x2d])
com(179)              #Frame rate control.
dat(data6)
time.sleep_us(10)

com(180)               #Display inversion control
dat(bytearray([0x07]))
com(192)               #Power control
data3[0] = 0xA2
data3[1] = 0x02
data3[2] = 0x84
dat(data3)

com(193)               #Power control
dat(bytearray([0xC5]))

data2 = bytearray(2)
com(194)               #Power control
data2[0] = 0x0A   #Opamp current small
data2[1] = 0x00   #Boost frequency
dat(data2)

com(195)               #Power control
data2[0] = 0x8A   #Opamp current small
data2[1] = 0x2A   #Boost frequency
dat(data2)

com(196)               #Power control
data2[0] = 0x8A   #Opamp current small
data2[1] = 0xEE   #Boost frequency
dat(data2)

com(197)               #Power control
dat(bytearray([0x0E]))

com(32)

com(54)
dat(bytearray([192 | 0]))

com(58)
dat(bytearray([0x05]))

com(42)                #Column address set.
area[0] = 0x00
area[1] = 0x01                #Start at row/column 1.
area[2] = 0x00
area[3] = _size[0] - 1
dat(area)

com(43)                #Row address set.
area[3] = _size[1] - 1
dat(area)

dataGMCTRP = bytearray([0x02, 0x1c, 0x07, 0x12, 0x37, 0x32, 0x29, 0x2d, 0x29,
                        0x25, 0x2b, 0x39, 0x00, 0x01, 0x03, 0x10])
com(224)
dat(dataGMCTRP)

dataGMCTRN = bytearray([0x03, 0x1d, 0x07, 0x06, 0x2e, 0x2c, 0x29, 0x2d, 0x2e,
                        0x2e, 0x37, 0x3f, 0x00, 0x00, 0x02, 0x10])
com(225)
dat(dataGMCTRN)

com(19)                #Normal display on.
time.sleep_us(10)

com(41)
time.sleep_us(100)

cs(1)

del data2,data3,data6,dataGMCTRN,dataGMCTRP
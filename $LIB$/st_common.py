from PRECONFIG import LCD_DRV
exec('from '+LCD_DRV+' import dc,spi')

def com(aCommand) :
    dc(0)
    spi.write(bytearray([aCommand]))

def dat(aData) :
    dc(1)
    spi.write(aData)

area = bytearray(4)
offset=bytearray(2)

def setarea(aPos0, aPos1) :
    com(42)            #Column address set.
    area[0] = offset[0] + aPos0[0] >>8
    area[1] = offset[0] + aPos0[0]
    area[2] = offset[0] + aPos1[0] >>8
    area[3] = offset[0] + aPos1[0]
    dat(area)

    com(43)            #Row address set.
    area[0] = offset[1] + aPos0[1] >>8
    area[1] = offset[1] + aPos0[1]
    area[2] = offset[1] + aPos1[1] >>8
    area[3] = offset[1] + aPos1[1]
    dat(area)

    com(44)            #Write to RAM.

_setwindowloc=setarea
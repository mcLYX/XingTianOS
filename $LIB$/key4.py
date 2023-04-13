import machine
vcc=machine.Pin(2,machine.Pin.OUT)
vcc.on()

keys=[machine.Pin(i,machine.Pin.IN,machine.Pin.PULL_DOWN) for i in (6,4,10,8)]

def get(key=None):
    value=[k.value() for k in keys]
    if key:return value[key-1]
    return value

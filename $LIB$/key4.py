import machine
vcc=machine.Pin(2,machine.Pin.OUT)
vcc.on()

keys=[machine.Pin(6,machine.Pin.IN,machine.Pin.PULL_DOWN),
      machine.Pin(4,machine.Pin.IN,machine.Pin.PULL_DOWN),
      machine.Pin(10,machine.Pin.IN,machine.Pin.PULL_DOWN),
      machine.Pin(8,machine.Pin.IN,machine.Pin.PULL_DOWN)]

def get(key=None):
    value=[]
    for k in keys:
        value.append(k.value())
    if key:return value[key-1]
    return value
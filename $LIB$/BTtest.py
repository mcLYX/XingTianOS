import ble,touch,dscn,scr
import bluetooth
import utime
#新建ble对象
b = bluetooth.BLE()
#导入类
p = ble.BLESimplePeripheral(b)
#查看mac地址，能正常显示mac地址就是创建广播成功
aa=b.config('mac')
print('mac:')
print(aa)
#接受数据函数
def on_rx(v):
    print(v)
    scr.f(0)
    dscn.cn(v.decode())
    scr.s()
p.on_write(on_rx)
dscn.cn('轻触发包，长按退出')
scr.s()
while not touch.prstime():
    if p.is_connected():
        p.notify('XtOS BLE test')   #发送数据（以通知形式）
    utime.sleep_ms(300)
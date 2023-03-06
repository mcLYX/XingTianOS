import urequests as rq
import scr,dscn,time,rd,touch,network#,machine

while 1:
  if not network.WLAN(network.STA_IF).isconnected():
    scr.f(0);dscn.cn('未联网!');scr.s();time.sleep(1);break
  try:
    ay=rq.get('https://v1.jinrishici.com/all')# if rd.rdi(0,9) else 'https://api.xygeng.cn/one')
  except:
    scr.f(0);dscn.cn('网络错误');scr.s();time.sleep(1);break
  try:
    jsd=[ay.json()['content'],ay.json()['origin']]
  except:
    jsd=[ay.json()['data']['content'],ay.json()['data']['origin']]
  scr.f(0)
  dscn.cn(jsd[0][:10])
  dscn.cn(jsd[0][10:20],y=13)
  dscn.cn(jsd[0][20:30],y=26)
  dscn.cn(jsd[0][30:],y=39)
  dscn.cn('--'+jsd[1],y=52)
  scr.s()
  print(jsd[0],'——',jsd[1])
  ay.close()
  #machine.WDT().feed()
  for i in range(5):
    time.sleep(1)
    if touch.detect():
      del ay,jsd;break
  if touch.detect():break

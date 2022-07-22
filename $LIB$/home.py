import gc,lstui,Run,scr,time
a=(),0
while 1:f=open('app.lst');a=lstui.lstui(eval(f.readline()),[708,252,2029,711],a[1]);scr.r(0,0,128,64,1);scr.s();time.sleep(1);Run.run(eval(f.readline())[a[1]]);f.close();gc.collect()
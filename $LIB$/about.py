from scr import s,t,f
import network,gc,touch,dscn,os,rd
f(0)
dscn.dscd([312,74,'OS'])
dscn.dscd([938,192,':v0.0.1c'],y=13)

lib=('By mcLYX',)
dscn.dscd(lib[rd.rdi(1,len(lib))-1],y=52)
del lib
gc.collect()
s()
touch.prstime()
f(0)
flash=os.statvfs('/flash')
dscn.dscd([1330,348,2048,':'])
dscn.dscd([str(flash[2]*flash[0]//1024)+'KB'],y=13)
dscn.dscd([2027,676,1049,717,':'],y=39)
dscn.dscd([str(flash[3]*flash[0]//1024)+'KB'],y=52)
gc.collect()
s()
touch.prstime()
f(0)
info=os.uname()
dscn.dscd([494,985,':',info[4].split()[0]])
dscn.dscd(['MPY',903,413,':',info[2]],y=13)
#dscn.dscd
dscn.dscd([394,1412,702,870,':']+
          ([58]if network.WLAN(network.STA_IF).isconnected()else[178])+
          [610,1721],y=39)
gc.collect()
dscn.dscd([194,252,107,348,':'+str(gc.mem_free()),486,191],y=52)
s()
touch.prstime()

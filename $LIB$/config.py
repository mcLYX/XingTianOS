cfgdir='../$DAT$/Config/'
def write(name,value=0):
    f=open(cfgdir+name,'w')
    f.write(str(value))
    f.close()
    del f
def read(name=None):
    if name:
        try:f=open(cfgdir+name)
        except:return
        re=f.read()
        f.close()
        del f
    else:
        re=None
    return re
        
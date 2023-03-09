import btree
cfgfile=open('../$DAT$/Config.db','r+b')
db=btree.open(cfgfile)
def write(name,value=0):
    db[name]=value
    db.flush()
def read(name=None):
    try:return db[name].decode()
    except:return
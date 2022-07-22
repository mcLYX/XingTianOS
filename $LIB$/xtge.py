import pbmds,scr
p,g={},{}

#创建新图像（图名，文件io，图宽，图高，xy坐标，读取大小
def add(n,f,w,h,x,y,v=-1):
  p[n]=[pbmds.getfb(f,w,h,v),[x,y],[w,h]]#0图文件 12 xy坐标

#创建组(组名，图像list)
def gp(n,gn):
  g[n]=gn

#显示目标图像
s=lambda n:scr.b(p[n][0],pos(n)[0],pos(n)[1])

#显示所有图像
def sa():
  scr.f(0)
  for i in p:
    s(i)

#获取目标图像坐标
pos=lambda n:p[n][1]

#移动目标图像(图名，xy偏移，模式(0-移动到xy,1-向xy移动))
def mv(n,x=0,y=0,m=1):
  p[n][1]=[pos(n)[0]*m+x,pos(n)[1]*m+y]

#整组移动(组名，xy偏移，模式)
def gmv(gp,x=0,y=0,m=1):
  for i in g[gp]:
    mv(i,x,y,m)

#显示组中的某个图像(组名，位置)
gs=lambda gp,m=0:s(g[gp][m])

#删除目标图像
def rm(n):
  del p[n]

#清空所有
def c():
  p,g={},{}

#判断两图是否不重合
def umt(n1,n2):
  (n1w,n1h),(n2w,n2h),(n1x,n1y),(n2x,n2y)=p[n1][2],p[n2][2],pos(n1),pos(n2)
  return n2y+n2h<n1y or n1y+n1h<n2y or n1x>n2x+n2w or n2x>n1x+n1w

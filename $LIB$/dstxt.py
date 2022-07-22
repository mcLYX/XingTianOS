from scr import t,s,f
def en(text,y=0):
  hang=[];f(0)
  for i in range(1,len(text)//16+1):
    hang.append(text[(i-1)*16:i*16])
  if len(text)%16>0:
    hang.append(text[len(text)-len(text)%16:len(text)])
  for i in range(len(hang)):
    t(hang[i],0,(i+y)*9)
  s()

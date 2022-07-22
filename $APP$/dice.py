from dstxt import en
from time import sleep as slp
from rd import rdi
from touch import d,prstime
while 1:
  en('Press and hold  to throw dice!',3)
  while 0==d():
    slp(.1)
  while d():
    en('Dice is rolling,Release to view the result.'+' '*21+'Current:       '+str(rdi(1,6)),1)
    slp(.2)
  result=rdi(1,6)
  en('-RESULT NUMBER-'+' '*24+str(result)+' '*26+'Tap to next',1)
  if prstime():
    break

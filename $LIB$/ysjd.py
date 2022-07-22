from time import sleep_ms as slp
from scr import f,s,t
import lstui
'''
def run():
  song=lstui.lstui(('Sakura Street','Bad Apple!!','Back...'),'Playlist',0)[1]
  # 定义旋律
  if song==0:
    play('ysjd.pwm')
  elif song==1:
    play('badapple.pwm')
'''
def play(fi):
  with open(fi) as m:
    name,singer,mld,bpm=m.readline()[:-2],m.readline()[:-2],m.readline()[:-2],int(m.readline())
  while 1:
    f(0);t('Now Playing:',0,0);t(name+'-',0,18);t(singer,0,27);t(str(len(mld))+'B,PWM File',0,45);s()
    exec(open('../$LIB$/mzc.py').read(),{'mld':mld,'bpm':bpm})
    if lstui.qna(['Replay?'],(' No',' Yes')):
      break
    print('\n-Replay-\n')
play(FileNAME)
del play
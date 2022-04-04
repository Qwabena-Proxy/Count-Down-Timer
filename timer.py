from time import sleep as sp

hrs = int(input('Hours:'))
min = int(input('Minute:'))
sec = int(input('Second:'))
'''


'''
while True:
  if len(str(hrs)) == 1:
    h = f'0{hrs}'
  else:
    h = f'{hrs}'
  if len(str(min)) == 1:
    m = f'0{min}'
  else:
    m = f'{min}'
  if len(str(sec)) == 1:
    s = f'0{sec}'
  else:
    s = f'{sec}'
  time = f'{h}:{m}:{s}'
  print(time)
  sec -= 1
  sp(1) 
  if sec == -1:
    min -= 1
    sec = 59
  if min == -1 and hrs > 0:
    hrs -= 1
    min = 59
  if hrs == 0 and min == 0 and sec == 0:
    print(f'{h}:{m}:0{sec}')
    break

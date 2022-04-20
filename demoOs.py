# demoOs.py
from os.path import *
print(abspath("python.exe"))
print(basename('python.exe'))
print(getsize('c:\\python39\\python.exe'))
print(exists('c:\\python39\\python.exe'))
print(isfile('c:\\python39\\python.exe'))

from os import *
print('운영체제이ㅣ름:',name)
#다른 실행 파일 실행
#system('notepad.exe')

import glob
print(glob.glob('c:\\work\\*.py'))
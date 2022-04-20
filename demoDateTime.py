# demoDateTime.py

import time
import random
print(dir(time))

print(time.time())
#.sleep(4)
print(time.time())
print(time.gmtime())
print(time.localtime())

from datetime import *
d1 =date.today()
print(d1)
d2 = date(2022, 5, 10)
print(d2)
print(d2-d1)

import random
print(random.random())
print(random.random())

print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)]) # 중복됨.
print(random.sample(range(20),10)) # 숫자하나만
print(random.sample(range(20),10))


#로또나오는법
lotto = list(range(1,47))
print('lotto=', lotto)
random.shuffle(lotto)
print(lotto)
print(random.sample(lotto,6))

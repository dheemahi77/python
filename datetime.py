'''import datetime
from datetime import date
import time
help(time)
time.sleep(5)
help(date)
f=date.today()
print(f)
time=datetime.datetime.now()
print(time)
print(time.day)
print(time.year)
print(time.second)
print(time.hour)
print(time.minute)'''

import time
help(time)
print(time.time())
t="2026-06-29"
x=time.strptime(t,"%Y-%M-%S")
print(x)

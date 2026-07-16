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
print(time.minute)

import time
help(time)
print(time.time())
t="2026-06-29"
x=time.strptime(t,"%Y-%M-%S")
print(x)'''

'''from datetime import datetime
help(datetime)
c=datetime(2026,9,1,5,20,0)
print(c)
now=c.strftime("%y-%m-%d")
print(now)
n2=c.strftime("%a-%y-%b")
print(n2)'''

import time
help(time)
print(time.time())
current_time=time.localtime()
t="2026-06-29"
x=time.strftime("%y-%m-%d",current_time)
print(x)

import time
help(time)
print(time.time())
current_time=time.localtime()
t="2026-06-29"
x=time.strftime("%H-%M-%S",current_time)
print(x)






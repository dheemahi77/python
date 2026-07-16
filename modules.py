'''help("modules")'''#display the modules
#math module
'''import math
print(help(math))
#print(dir(math))#methods
x=1.23
print(math.ceil(x))
print(math.floor(x))
print(math.sqrt(64))
print(math.remainder(298,38392))#nearest
print(math.radians(30))
print(math.pow(10,3))
print(math.log(1))
print(math.lcm(10,20,30,20,102,213,122))
print(math.factorial(5))
print(math.fabs(-2891249.97384))#change the value  in positivet
print(math.sqrt(81))'''

#os module
'''import os
from os import getcwd,mkdir
#print(help(os))
# print(getcwd())
# print(mkdir("os.module.py"))

import os
os.chdir("D:\\")
print("success")
print(os.getcwd())
os.rmdir("osmodule.py")
print("done")#remove the directory'''

#sys module

'''import sys
help(sys)
print(sys.getwindowsversion())
print(sys.platform)
print(sys.version)
print(sys.maxsize)
print(sys.path)
print(sys.argv)
#sys.exit
print(sys.getsizeof(123435893683845843293759467))#9-28,12-32'''

#user module
'''def mounika(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j]<l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
            print(l)
        print()
l=[0,3,72,827,65,92]
mounika(l)'''

#random module
'''import random
help(random)
print(random.randint(1,10))#inclusive
print(random.randrange(1,10,2))
print(random.choice([1,2,3,54,56]))
print(random.choices([1,2,37,78,8,8],k=2))
print(random.sample(["a","b","c","d"],k=2))
x=[1,2,3,65,78,9,4,35]
random.shuffle(x)
print(x)'''

#datetime
import datetime
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
      

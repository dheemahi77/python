'''def fun(n,l=[]):#1 to 100 in  list
    
    for i in range(1,n+1):
        if i%2==0:#even
            l.append(i)
        elif i%2!=0 and i%5==0:
            l.append("something")
        elif i%2!=0:
            l.append("odd")#odd
    return l

n=100
print(fun(n))

print()#list comprehension
print([i if i%2==0 else "something" if i%2!=0 and i%5==0 else "odd" for i in range(1,n+1)])'''



'''def names(l,v):
    s=[]
    for i in l:
        w=""
        for j in i:
            if j in v:
                w+=j
        s.append(j)
    print(s)
                
l=["mahi","mouni","joshi","harika","yamini","gagan"]
v="aeiou"   
names(l,v)'''


'''def fun():
    l=[]
    for i in range(5):
        for j in range(5):
            l.append([i,j])
    return l
print(fun())

print()
print([[i,j] for i in range(5) for j in range(5)])#list comprehension'''


'''print((lambda:"this is the new way of function")())#lambda

result=((lambda:"this is the new way of function"))
print(result())


print((lambda x:x*x)(10))

print((lambda x,y,z:x if x>y and x>z else y if y>z and y>x else z)(5,12,21))

l=[1,2,3,4,5,6,7]
result=(lambda l:[i for i in l if i%2==0])#list
print(result(l))

print((lambda x,y:{x*x,x*y,x-y})(10,20))'''


'''def str(s):
    x=" "
    for i in s:
        x=i.upper()+x
    return x
print(str("mapping"))

print(list(map(str,"power")))#list

print("" .join(list(map(str,"power"))))#string'''

'''def len(l):
    x=[]
    for i in l:
        x.append(len(i))
    return x'''

'''l=["java","bava","oracle","miracle"]
print(len(l))


print(list(map((lambda x:len(x)),(l))))
result=map((lambda x:len(x)),(l))
print(list(result))#map

x=[10,29,39,48]
print(list(filter((lambda x:x%2==0),(x))))#filter'''



'''l=["tcs","wipro","infosys","zoho"]

result=map(lambda x:x.capitalize(),l)#first letter capitalize
print(list(result))'''

'''n=["raja","rani","ram","sam","john"]
result=filter((lambda x:x.startswith("r")),n)
print(list(result))#starts with letter

from functools import reduce
x=[1,2,3,4,5]
result=reduce((lambda x,y:x+y),x)
print(result)#reduce'''

l=[1,2,3]
for i,j in enumerate(l):#enumerate
    print(i,j)#i for index and j for list values
    
x=[10,20,37,37]
y=[1,2]
for i in zip(x,y):#combines the list in tuple
    print(i)

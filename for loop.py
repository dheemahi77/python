#for with iterable

"""x=[10,21,30,40,19,25,18,50]
for i in x:
    if i%2!=0:
        print(i)
    else:
        print("even")"""


"""x="srujana".upper()
for i in x:
    print(i)"""

"""x="srujana126374sri"
w=" "
n=""
for i in x:
    if i.isdigit():
        n+=i
    else:
        w+=i
print(n)
print(w)"""



"""x="srujana126374sri"
w=" "
n=0
for i in x:
    if i.isdigit():
        n+=int(i)#sum
    else:
        w+=i
print(n)
print(w)"""


"""d={"a":100,"b":200,"c":300}
for k,v in d.items():
    if v>150:
        print(k)"""

#for with range
'''for i in range(10,-30,-3):
    print(i)'''

#reverse
'''x=[1,2,3,4,5,6,7,8,9,0]
for i in range(len(x)-1,-1,-1):
    print(x[i])'''

'''x=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(x)-1,-1,-1):
    if i%2==0:
        if x[i]%2!=0:
            print(x[i])'''

for i in range(1,20,1):
    print(i)
else:
    print("completed")

    

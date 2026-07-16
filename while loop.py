#except divisible 5
'''for i in range(1,101):
    if i%5!=0:
        print(i)'''

'''for i in range(1,101):
    if i%5==0:
        continue
    print(i)'''


'''for i in range(1,101):
    if i%5==0:
        continue
    else:
        print(i)
else:
    print("completed")'''

#table
'''n=int(input())
for i in range(1,11):
    print(n,"*",i,"=",n*i)'''

#reverse table
'''n=int(input())
for i in range(10,0,-2):
    print(i,"*",n,"=",n*i)'''

#while
'''i=0
while i<=10:
    i+=1
    print(i)'''
    
'''i=0
while i<=5:
    i+=1
    print(i)
    i+=1'''

#1*2=2
'''n=int(input())
i=1
while i<=10:
    print(i,"*",n,"=",n*i)
    i+=1'''
    
#10*2=20
'''n=int(input())
i=10
while i>=0:
    print(i,"*",n,"=",n*i)
    i-=1'''

#list''
'''x=["a","b","c","d","e","f"]
i=0
while i<len(x):
    print(x[i])
    i+=1'''

#reverse
'''x=["a","b","c","d","e","f"]
i=len(x)-1
while i>=0:
    print(x[i])
    i-=1'''

'''x=["a","b","e","c","f"]
i=0
while i<=len(x):
    if i%2==0:
        print(x[i])
    i+=1'''

'''x=["a","b","e","c","f"]
l=""
i=0
while i<len(x):
    if i%2==0:
        l+=x[i]
    i+=1
print(l)'''

'''x=["a","b","e","c","f"]
#{0:"a",1:"b",3:"c",4:"d",5:"e"
d={}
i=0
while i<len(x):
   # print(i)
   #print(x[i])
    d[x[i]]=i
    i+=1
print(d)'''

x=["a","b","e","c","f"]
#{0:"a",1:"b",3:"c",4:"d",5:"e"
d={}
i=0
while i<len(x):
    if i%2!=0:
   # print(i)
   #print(x[i])
        d[x[i]]=i
    i+=1
print(d)

x=["a","b","e","c","f"]
#{0:"a",1:"b",3:"c",4:"d",5:"e"
d={}
i=0
while i<len(x):
    if i%2!=0:
   # print(i)
   #print(x[i])
        d[x[i]]=i
    i+=1
print(d)


'''x=["a","b","e","c","f"]
d={}
keys=[]
values=[]
l=[]
for k,v in d.items():#wrong
    if v%2!=0:
        keys.append(k)
        values.append(v)
print(keys,values)

#{1:"b",3:"c"}
di={}
for i in range(len(keys)):
    di[values[i]]=keys[i]
print(di)'''

'''x=["a","b","c","d","e","f"]
i=0
while i<len(x):
    print(i)
    i+=1'''
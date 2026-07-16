'''def fun(x,y):
    return x,y
print(fun(10,20))
#if result>0:
    #print("positive")
a,b=fun(2,3)
print(a)'''


#pass by value
'''def details(name,bio):
    name="srujana"
    print(name,bio)
    print(x,y)
    
x=input()
y=["developer"]
details(x,y)
print(x)
print(y)'''

#pass by reference
'''def details(name,bio):
    name="srujana"
    print(name,bio)
    y.append("python")
    print(x,y)
    
x=input()
y=["developer"]
details(x,y)
print(x)
print(y)'''

#factorial
'''n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''


'''def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(fact(5))'''

#recursion
'''def rec(n):
    if n==10:
        return
    else:
        print(n)
        rec(n+1)
rec(0)'''

#reverse
'''def rec(n):
    if n==-1:
        return
    else:
        print(n)
        rec(n-1)
rec(10) '''

'''def rec_fact(n):
    if n==1:
        return 1
    else:
        return n*rec_fact(n-1)
print(rec_fact(5))'''

#fibanocci
def fib(n):
    a=0
    b=1
    total=0
    for i in range(n+1):
        total+=a
        print(a,end=" ")
        a,b=b,a+b
    return a
print(fib(9))
    

    
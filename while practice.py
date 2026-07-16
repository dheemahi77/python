'''balance=int(input())
choice=int(input("enter your choice:"))
i=0
while i<=0:
    if choice==1:
        print(" check balance")
        print("available balance:",balance)
        i+=1
    elif choice==2:
        print("withdraw")
        amount=int(input("enter withdraw amount:"))
        if amount<=balance:
            balance=balance-amount
            print("transaction successful")
            print("withdraw amount:",amount)
            print("remaining balance:",balance)
    elif choice==3:
        print("deposit")
        amount=int(input("enter diposit amount:"))
        balance=balance+amount
        print("deposit successfully")
        print("current balance:",balance)
    else:
        print("invalid choice")
    i+=1'''


'''i=0
while i<=10:
    if i%2==0:
        print(i)
    i+=1'''

'''i=25
while i>=5:
    if i%5==0:
        print(i)
    i-=1'''

'''i=10
while i>=2:
    if i%2==0:
        print(i)
    i-=1'''

'''n=int(input())
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1'''

'''n=int(input())
i=10
while i>=1:
    print(n,"*",i,"=",n*i)
    i-=1'''

'''x=["a","b","c"]
i=0
while i<len(x):
    print(x[i])# ans abc
    i+=1'''

'''x=["a","b","c"]
i=len(x)-1
while i>=0:
    print(x[i])
    i-=1'''

'''i=1
while i<=5:
    print(i)
    i+=1'''

'''i=5
while i>=1:
    print(i)
    i-=1'''

'''x=["a","b","c","d"]#wrong
i=len(x)'''


'''x=[10,20,30,40,50]
i=10
while i<=50:  #10 20 30 40 50
    if i in x:
        print(i)
    i+=1'''


x=int(input())
i=1
sum=0
while i<=x:
    y=int(input("enter numbers:"))
    sum=sum+x
    i+=1
print(sum)
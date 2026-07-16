#string
"""x="harika"
for i in x:
    print(i)"""

'''x="mahikshatriya"
for i in x:
    print(i)'''

"""for i in range(1,9):
    print(i)"""

#upper
"""x="harika"
for i in x:
    print(i.upper())"""

#range
"""for i in range(1,10):
    print(i)"""

#list
"""x=[10,20,30,40,50]
for i in x:
    print(i)"""
#odd
"""x=[10,20,30,40,50,60]
for i in x:
    if i%3==0:
        print(i)"""

#even
"""x=[10,20,30,40,50,60]
for i in x:
    if i%2==0:
        print(i)"""

#alphabets
"""x="mahijoshi123456"
for i in x:
    if i.isalpha():
        print(i)"""
        
#digits
'''x="joshi123456768"
for i in x:
    if i.isdigit():
        print(i)'''

#alphadigit
'''x="abc123"
m=""
n=""
for i in x:
    if i.isdigit():
        m+=i
    else:
        n+=i
print(m)
print(n)'''

#dictionary
'''s={"mahi":2,"mouni":3,"harika":3}
for i in s.items():
    print(i)'''

#keys values
'''s={"mahi":2,"mouni":3,"harika":3}
for k,v in s.items():
    print(k,v)'''


#range for positive
"""for i in range(10,40,1):
    print(i)"""

"""for i in range(1,10,2):
    print(i)"""

'''for i in range(1,10,3):
    print(i)'''

'''for i in range(5,25,2):
    print(i)'''

'''for i in range(-20,-40,-5):
    print(i)'''

'''for i in range(-2,-10,-1):
    print(i)'''

'''for i in range(-3,-13,-3):
    print(i)'''

'''for i in range(-8,-20,-5):
    print(i)'''

#TABLE
"""n=int(input())
for i in range(1,11):
    print(n,"*",i,"=",n*i)"""

#total
"""n=input()
grocery=[10,20,30,40]
total=0
for i in grocery:
    total+=i
print("groceries:",total)"""

#only one value
'''x=[10,20,30,40,50]
n=20
for i in x:
    if i==20:
        print("Found")
    else:
        print("Not Found")'''
    
#index
'''x=[1,2,3,4,5,6]
for i in range(len(x)):
    print(i)'''

#numbers
'''x=[1,2,3,4,5,6]
for i in range(len(x)):
    print(x[i])'''
    
#reverse
'''x=[1,2,3,4,45,6]
for i in range(len(x)-1,-1,-1):
    print(i)'''

"""x=[1,2,3,4,45,6]
for i in range(len(x)-1,-1,-1):
    print(x[i])"""

'''for i in range(-1,10,-1):
    print(i)'''



'''for i in range(-5,-22,-2):
    print(i)'''

'''m="#coder1234mava"
for i in m:
    if i.isalpha()==0:
        print(i,end="")'''

#VOWELS
x="beautiful"
vowels="aeiouAEIOU"
count=0
for i in x:
    if i in vowels:
        count+=1
print(count)
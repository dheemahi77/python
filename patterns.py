#i is no of rows
'''for i in range(4):#0,1,2,3
    for j in range(3):#0,1,2
        print(i)
    print()'''
    
# j no of columns
'''for i in range(4):#0,1,2,3
    for j in range(4):#0,1,2,3
        print(j)
    print()'''

#square
'''for i in range(3):#0,1,2
    for j in range(4):#0,1,2,3
        print("*",end="")
    print()'''
 
#rectangle
'''for i in range(3):#0,1,2
    for j in range(7):#0,1,2,3,4,5,6
        print("*",end="")
    print()'''

#
'''for i in range(1,6,1):#i=1,i=2,i=3,i=4,i=5
    for j in range(i):
        print("*",end="")
    print()'''

#reverse
'''for i in range(5,0,-1):#i=5,i=4,i=3,i=2,i=1
    for j in range(i):
        print("*",end="")
    print()'''

#
'''for i in range(1,6,2):#i=1,i=3,i=5
    for j in range(i):
        print("*",end="")
    print()'''

#pyramid
'''for i in range(1,6,2):
    for j in range((5-i)//2):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()'''

#high to low
'''for i in range(5,-1,-1):#4,3,2,1,0
    for j in range(3):#0,1,2,3,4
        print(i,end=" ")
    print()'''

'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
    

'''n=5
for i in range(n):#c
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=5
for i in range(n):#D
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==n-3:
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print()'''


'''n=5
for i in range(n):#h
    for j in range(n):
        if j==0 or i==n-3 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=5
for i in range(n):#l
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=5
for i in range(n):#t
    for j in range(n):
        if i==0 or j==n-3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''n=5
for i in range(n):#8
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1 or i==n-3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=5
for i in range(n):#7
    for j in range(n):
        if i==0 or j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=5
for i in range(n):#A
    for j in range(n):
        if i==0 or j==0 or i==n-3 or j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=5
for i in range(n):#u
    for j in range(n):
        if j==0 or i==n-1 or j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''for i in range(6):#numbers
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''


'''n="A B C D"
for i in range(4):
    for j in range(1):
        print(n,end=" ")
    print()'''
 
 #letters
'''for i in range(3):#a b c d#caps
    for j in range(4):
        print(chr(65+j),end=" ")
    print()'''

'''for i in range(6):#small
    for j in range(3):
        print(chr(97+i),end=" ")
    print()'''

#numbers
'''n=1
for i in range(4):
    for j in range(4):
        print(n,end=" ")
        n+=1
    print()
o/p:1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16 '''


'''for i in range(1,5):
    for j in range(5):
        print(i,end=" ")
        i+=1
    print()
o/p:1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8'''

'''i=0
for i in range(4):
    for j in range(5):
        if i==0 or j==1:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input())
for i in range(n):
    for j in range(n):
        if i==n-1 or j==0 or i==n-3 or i==0  or j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''for i in range(1,5):
    for j in range(5,0,-1):
        print("*",end=" ")
    print()'''

#swasthick 
'''n=5
for i in range(n):
    for j in range(n):
        if i==n-3 or j==n-3 or (j==0 and i<=2) or (i==0 and j>=2) or (j==n-1 and i>=2) or (i==n-1 and j<=2):
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()
o/p:
*   * * * 
*   *     
* * * * * 
    *   * 
* * *   * '''

'''def print_pattern(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '*' * i)

n = int(input())
print_pattern(n)
o/p:*
   **
  ***
 ****
*****'''


n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for i in range(2*i-1):
        print("*",end=" ")
    print()
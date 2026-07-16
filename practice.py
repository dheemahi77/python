"""n=int(input())
if 10>n:
    print("true")
else:
    print("false")"""

"""age=int(input())
if age>18:
    print("eligible")
else:
    print("not eligible")"""

"""n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")"""

"""n=int(input())
if n>0:
    print("positive")
else:
    print("negative")"""

"""marks=int(input("marks:"))
if marks>40:
    print("pass")
else:
    print("fail")"""

"""n=int(input())
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")"""

"""age=int(input())
if age<=12:
    print("child")
elif age<=19:
    print("teenager")
else:
    print("adult")"""

"""marks=int(input())
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("c")
elif marks>=60:
    print("D")
else:
    print("fail")"""

"""age=int(input())
salary=int(input())
if age>=20:
    if salary>20000:
        print("eligible for loan")
else:
    print("not eligible")"""

"""student=int(input())
if student>90:
    print("student get a scholorship")
if student>=35:
    print("pass")
else:
    print("fail")"""


"""days1=["monday","tuesday","wednesday","thursday","friday"]
day2=["saturday","sunday"]
days=str(input())
if days in days1:
    print("working day")

else:
    print("weekend")"""


"""amount=int(input())
if amount>=20000:
    print("you get 50% discount")
elif amount>=10000:
    print("you get 25% discount")
elif amount>=5000:
    print("you get 10% discount")
else:
    print("no discount")"""
   
   
"""a,b,c=map(int,input().split())
largest=a
if b>largest:
    largest=b
if c>largest:
    largest=c
print(largest)"""



"""ru=["mahi","mouni","joshi"]
p=1234
user=input()
if user in ru:
    password=int(input())
    if password==p:
        print("login success")
    else:
        print("wrong password")
else:
    print("user name not found")"""





"""college=input()
if college=="yes":
    block=input()
    if block=="yes":
        floor=input()
        if floor=="yes":
            classes=input()
            if classes=="yes":
                print("present the class")
            else:
                print("floor")
        else:
            print("block")
    else:
        print("college")
        
else:
    print("absent")"""



"""year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:
    print("not a leap year")"""
    
    
"""color=input()
if color=="green":
    print("go")
elif color=="yellow":
    print("get ready")
elif color=="red":
    print("stop")
else:
    print(" not a traffic signals")"""


"""age=int(input())
if age>=10:
    print("the person enter the movie theater")
else:
    print("do not enter the movie theater")"""



"""name = input("Enter name: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
fees = input("Fees paid (yes/no): ")

if name != "":
    if age >= 18:
        if marks >= 35:
            if attendance >= 75:
                if fees == "yes":
                    print("Eligible")
                else:
                    print("Fees not paid")
            else:
                print("Low attendance")
        else:
            print("Failed")
    else:
        print("Age less than 18")
else:
    print("Invalid name")"""



username = input("Enter username: ")
password = input("Enter password: ")
product = input("Enter product: ")
stock = input("Stock available (yes/no): ")
payment = input("Payment done (yes/no): ")

if username != "":
    if password == "admin123":
        if product != "":
            if stock == "yes":
                if payment == "yes":
                    print("Order Confirmed")
                else:
                    print("Payment Pending")
            else:
                print("Out of Stock")
        else:
            print("Select Product")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

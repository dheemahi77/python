"""#if condition
age=int(input())
if age>18:
    print("eligible")
else:
    print("not eligible")"""



"""age=int(input())
card=input().lower()
if age>18 and card=="yes":
    print("eligible")
else:
    print("not eligible")"""


"""username="mahi"
password="mouni@123"
u=str(input())
p=str(input())
if username and password:
    print("login succesfully")
else:
    print("failed")"""


"""a=["a","b","c","d"]
user=input().lower()
if user in a:
    print("available")
else:
    print("not available")"""


"""a,b,c=map(int,input().split())
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)"""


"""n=int(input())
if n%3==0:
      print("fuzz")
elif n%5==0:
    print("buzz")
else:
    print(n)"""


"""n=int(input())
if n%3==0 and n%5==0:
    print("fizz buzz")
elif n%3==0:
    print("fizz")
else:
    print("buzz")"""



"""name=str(input())
marks=int(input())
print("")
if marks>90:
    print(f"name:{name},marks:{marks},grade:A")
elif marks>80:
    print(f"name:{name},marks:{marks},grade:B")
elif marks>70:
    print(f"name:{name},marks:{marks},grade:C")
else:
    print(f"name:{name},marks:{marks},grade:D")"""




name=input()
grade=input().lower()
if grade=="A":
    print("free")
elif grade=="b":
    seat_allocated="20%"
elif grade=="c":
    seat_allocated="15%"
elif grade=="d":
    seat_allocated="10%"
else:
    pay="50000"
print(f"name:{name},grade:{grade},seat_allocated")   





#single inheritance  #repetative of codeor reuse the code
'''class GrandFather():
    def G1(self):
        print("this is grandfather class")
class Father(GrandFather):
    def F1(self):
        print("this is father class")
class Child(Father):#multilevel
    def C1(self):
        print("this is child class")

        
# print(Father.mro())#single
# obj=Father()#first priority  is create the object
# obj.F1()
# obj.G1()

# g=GrandFather()
# g.G1()

c=Child()
c.C1()
c.F1()
c.G1()'''


#multiple inheritance:

'''class GrandFather():
    def G1(self):
        print("this is grandfather class")
class Father():
    def F1(self):
        print("this is father class")
class Child(Father,GrandFather):#grandfather,Father
    def C1(self):
        print("this is child class")
        
c=Child()
print(Child.mro())'''

#hierarchial inheritance
'''class Father():
    def F1(self):
        print("this is the father class")
        
class Child1(Father):
    def C1(self):
        print("this is child class")
class Child2(Father):
    def C2(self):
        print("this ischild2 class")
c=Child2()
c.C2()
c.F1()
print(Child1.mro())'''

'''class codegnan():
    def __init__(self,name,address,phone_no):
        self.name=name
        self.address=address
        self.phone_no=phone_no
    
class Teaching(codegnan):
    def __init__(self,name,email,phone_no,address,bankact,subject):
        
        self.name=name
        self.email=email
        self.phone_no=phone_no
        self.bankact=bankact
        self.subject=subject
    def Details():
        print(self.name,self.email,self.address,self.phone_no,self.bankact,self.subject)
class Students(codegnan):
    def __init__(self,name,email,phone_no,address,parent_no,cgpa,clg,fee):
        super().__init__(name,address,phone_no)
        self.email=email
        self.parent_no=parent_no
        self.cgpa=cgpa
        self.clg=clg
        self.fee=fee
    def Details(self):
        print(self.name,self.address,self.phone_no,self.parent_no,self.cgpa,self.clg,self.fee)
    def Offercheck(self,amount=50000):
        if self.cgpa>9.5:
            discount=amount-(amount*5/100)
            print(discount)
        else:
            print("Not eligible") 
class Development(codegnan):
    def __init__(self,name,email,phone_no,address,bankact,qua,designation):
        self.name=name
        self.email=email
        self.phone_no=phone_no
        self.address=address
        self.bankact=banckact
        self.qua=qua
        self.designation=desigantion
        
    def Details(self):
        print(self.name,self.email,self.address,self.phone_no,self.bankact,self.qua,self.clg.designation)

class Helpers(codegnan):
    def __init__(self,name,address,phone_no,work):
        self.name=name
        self.phone_no=phone_no
        self.address=address
        self.work=work
        
    def Details(self):
        print(self.name,self.address,self.phone_no,self.work)
s=Students("Dheemahi", "dheemahigmail.com",8897573106,"Vijayawada",9876544321,9.7,"srk",50000)
print(s.Details())
s.Offercheck()'''


#polymorphism
#method overriding
'''class Car():
    def Travel(self):
        print("i am travelling in car")
class Bike():
    def Travel(self):
        print("by walk")    
class Train():
    def Travel(self):
        print("this is by train")
class Walk(Car,Train,Bike):#method resolution order
    def Travel(self):
        print("this is by train")

obj=Walk()
print(Walk.mro())
obj.Travel()'''

'''class Phonepay():
    def Pay(self):
        print("pay on phnpay")
class Googlepay():
    def Pay(self):
        print("pay on google pay")    
class Debit():
    def Pay(self):
        print("pay on debit card")
class Paytm(Phonepay,Googlepay,Debit):#method resolution order
    def Pay(self):
        print("pay on paytm")

obj=Paytm()
print(Paytm.mro())
obj.Pay()
obj=Phonepay()
obj.Pay()'''


#method overloading
'''class Calculator:
    def __init__(self,a,b,c=0,d=0,f=0,g=0):#default
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.f=f
        self.g=g
    def Add(self):
        print(self.a+self.b+self.c+self.d+self.f+self.g)
x=Calculator(10,20)
x.Add()
y=Calculator(1,2,3,4,56)
y.Add()'''


'''class Calculator:#variable length
    def __init__(self,*values):
        self.values=values
    def add(self):
        print(sum(self.values))
x=Calculator(10,20)
x.add()
y=Calculator(1,2,3,4,56,36,2,2)
y.add()'''

'''class Calculator:#using for loop
    def __init__(self,*values):
        self.values=values
    def Add(self):
        print((self.values))
        for i in self.values:
            print(i)
x=Calculator(10,20)
x.Add()
y=Calculator(1,2,3,4,56,36,2,2)
y.Add()'''


'''class Calculator:#variable length
    def __init__(self,*values):
        self.values=values
    def __add__(self):
        print(sum(self.values))
x=Calculator(10,20)
print(dir(x))
x.__add__()'''

'''class Calculator:#variable length
    def __init__(self,*values):
        self.values=values
    def __add__(self):
        print(sum(self.values))
    def __eq__(self):
        print((self.values))
    def __gt__(self):
        print(gt(self.values))
x=Calculator(10,20)
print(dir(x))
x.__add__()
x.__eq__()'''

#duck typing
'''class Car():
    def Travel(self):
        print("i am travelling in car")
class Bike():
    def Travel(self):
        print("by bike")    
class Train():
    def Travel(self):
        print("this is by train")
class Walk(Car,Train,Bike):#method resolution order
    def Travel(self):
        print(" by walk")

def Calling(obj):
    obj.Travel()
w=Walk()
Calling(w)
v=Train()
Calling(v)
s=Bike()
Calling(s)
a=Car()
Calling(a)'''

#abstaction
#1.abc module
'''from abc import ABC,abstractmethod
class Phonepay():
    @abstractmethod#decarator
    def Pay(self):
        print("pay on phnpay")
    #@abstractmethod
    def Paying(self):
        print("phnpay")
class Googlepay():
    def Pay(self):
        print("pay on google pay")
    def Paying(self):
        print("gpay")
obj=Googlepay()
obj.Pay'''


'''class Contact:
  def __init__(self):
    self.book={}
class Details(Contact):
  def Create(self,name,phone_no):
    self.name=name
    self.phone_no=phone_no
    if name in self.book:
      print("Already exists")
    elif phone_no in self.book:
      print("Number already exist")
    else:
      self.book[name]=phone_no
      print("success")
  def view(self):
    if len(self.book)==0:
      print("No contact found")
    else:
      for name,phone in self.book.items():
        print(f"Name:{name}\tphone:{phone}")
  def update(self, name,new_name):'''
    '''if name in self.book:
      self.book[name] = phone_no
      print("Contact found")
      print("Update")
    else:
      print("contact not found")'''
    self.name=name
    self.new_name=new_name
    if self.name in self.book and self.new_name not in self.book:
        number=self.book[name]
        self.book[new_name]=number
        print(f"success change {name}-{new_name}")
    else:
        print(f"{name} or {new_name} already exists")
obj=Details()
while True:
  n=int(input("1.Create\n 2.View \n 3.Update\n 4.Exit\n "))
  if n==1:
    name=input("enter name:")
    phone_no=int(input("enter number:"))
    obj.Create(name,phone_no)
  elif n==2:
    obj.view()
  elif n==3:
    name = input("Enter Name to Update: ")
    phone_no = int(input("Enter New Number: "))
    obj.update(name, phone_no)
  elif n==4:
    break
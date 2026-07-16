'''class Main:
    x=10
    
obj=Main
print(obj.x)
obj2=Main
print(obj2.x)
obj2.x=99
print(obj2.x)'''

'''class Phone:
    ringtone="helo hello"
    def App(self):
        self.games="ludo"
    
mahi=Phone()
mahi.ringtone="chalo"
print(mahi.ringtone)
mahi.App()
print(mahi.games)

mouni=Phone()
print(mouni.ringtone)'''

'''class Main():
    x=30
    
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def details(self):
        print(self.name,self.age,self.marks)
    
obj=Main("mahi",21,478)
print(dir(obj))
obj.details()'''

#ATM
class Atm():
    amount=9999
    def __init__(self,n,p,balance):
        self.name=n
        self._p=p
        self.__b=balance
    def Details(self):
        print(self.name,self._p,self.__b)
        
    def Pin(self,new_pin):
        self._p=new_pin
        print(self._p)
    def Deposit(self,amount):
        if amount>0 and amount%100==0:
            self._amount=amount
            self.__b+=amount
            print("deposit money:",self._amount)
            print("balance:",self.__b)
        else:
            print("enter valid amount")
    def Withdraw(self,amount):
        if amount>100 and amount%100==0:
            self._amount=amount
            self.__b-=amount
            print("withdraw money:",self._amount)
            print("balance:",self.__b)
        else:
            print("withdraw valid amount")
            
ac1=Atm("x",1234,9999)
ac1.Details()
print(ac1._p)
ac1.Pin(8888)

ac1.Deposit(2000)
ac1.Withdraw(500)
ac1.Details()
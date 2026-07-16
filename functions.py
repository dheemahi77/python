'''def student(name,age,marks,institute="codegnan"):
    print(name,age,marks,institute)
student(name="mahi",age=20,marks=100)#keyword
student("joshi",20,400)#positional
student(456,23,"mouni")
student("ram",25,749,"techgnan")#default'''

'''def student(name,age,marks,institute="codegnan"):
    if age>=20 and marks>=400:
        print("eligible scholorship")
    else:
        print("not eligible")
student("mahi",25,450,"codegnan")'''#using conditional

'''def Calculator(x,y,z=0):
    print(x+y+z)
def Cal(*values):
    count=0
    print(sum(values))
    print(*values)
    for v in values:
        count+=v
    print(count)
if __name__=="__main__":
    #Calculator(10,20)
    #Calculator(10,30,40)
    Cal(10,20,30,40,40,50,1,23,45,56,7,8)'''

'''def user(table,*items):
    print(table)
    print(items)
user(102,"biryani","rice","ice_creame","startus")'''

'''def user(**items):#keyword length argument  #dictionary
    print(items)
user(food="biryani",topings=1,cheese=2,sause=4)'''

'''def report(**args):
    print(args)
report(h10=1.35,h11=23.32,h12=0.0,h13=0.7,h14=32.33)'''


x=50#global 
def local(a,b):
    print(a,b)#local scope
    global x
    x=50
    print(x)
local(10,20)
print(x)

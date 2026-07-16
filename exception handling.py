'''try:
    #import mahi
    print(10/2)#risky code
    x=123
    print(x)
    l=[1,2,3];print(l[2])
    d={1:"a",2:"b"}
    print(d[3])
    print("a"%1)
    print(mahi.x)
except Exception as e:
    print(e)
    
except ZeroDivisionError:
    print("you cannot divisible by zero")
except NameError:
    print("give element is not created")
except IndexError:
    print("you can use index only from 0-len(variable)-1")
except KeyError:
    print("key not found")
except ModuleNotFoundError:
    print("module is not available in python")
except TypeError:
    print("you cannot perfform str and int")
else:
    print("try worked")
finally:
    print("completed")'''

agae=18
try:
    age<=18:
        raise "age is less than 18"
except Exception as e:
    print(e)
finally:
    print("done")
    
    
    
#list
"""x=[10,20,30,["MAVA","weekend"],["entra","gola"]]
print(x[1])
print(x[3][0])
print(x[4][0])

a=10
b=10
print(id(a))
print(id(b))

a=[1,2,3,4]
b=[1,2,3,4]
print(id(a))
print(id(b))


l=[1,2,3,4]
print(l)
l.append(id(l))
print(l)

#tuple

t=(1,3,2,"john",2+3j,2.33)
print(t)
print(t[0:3])
print(len(t))"""

#set

"""s=set({True,False,1,2,3,4,True})
print(type(s))
print(s)
s.update({4,9,6,7})
print(s)
s.remove(7)
print(s)
s.pop()
print(s)
s.discard(True)
print(s)
s.clear()
print(s)
s.copy()
print(s)"""

"""dhoni={"jathin","balaji","dinesh","krishna","sumanth"}
virat={"krishna","sunman","akshya","pardu"}
#print(dhoni.union(virat))
print(virat&dhoni)
#print(dhoni.intersection(virat))
print(virat|dhoni)
#print(dhoni.difference(virat))
print(virat-dhoni)
#print(dhoni.symmetri_difference(virat))
print(virat^dhoni)"""

#methods

x={1,2,3,4,6,8,9}
y={1,2,4,5,6}
print(x.issubset(y))
print(y<=x)

print(x.issuperset(y))

print(x.isdisjoint(y))
a={1,2}
b={3,4}
print(a.isdisjoint(b))

print(False*1 and True

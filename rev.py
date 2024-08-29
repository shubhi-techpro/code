t=("red","yellow")
print(type(t))
print(t)
list=[]
for x in reversed(t):#reversed is a builtin function for tuple
    list.append(x)
o=tuple(list)
print(o)

a=[1,2,3,4]
print(type(a))
a.reverse()
print(a)
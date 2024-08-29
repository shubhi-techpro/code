list1=[30,40,70,60]
list2=[30,70,65,78]
list3=[89,30,70,76]

s1=set(list1)
s2=set(list2)
s3=set(list3)

s3=s1.intersection(s2)
s4=s1.intersection(s3)
print(s4)

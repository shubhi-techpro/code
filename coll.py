# list stre multiple item in single variable []
#item are indexed (0 based index)and ordered , mutable (change or update value in list )
# duplicate are allowed
# can contain diff data typ as well as same data type
fruits=["apple","bannana","jerry",9]
print(fruits[0])
fruits[1]="cherry"# update value in ist
print(fruits[1])
print(type(fruits))# type of list
print(len(fruits))#length of list
if "bannana" or "jerry" in fruits:# in not in operators
    print("present")
else:
    print("no")

    


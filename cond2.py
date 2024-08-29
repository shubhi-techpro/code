'''n1=int(input("enter number 1"))
n2=int(input("enter number 2"))
n3=int(input("enter number 3"))
if n1>n2 and n1>n3:
    print("n1 is greatest")
elif n2>n1 and n2>n3:
    print("n2 is greatest")
else:
    print("n3 is greatest")

if n1>n2:
    if n1>n3:
        print("n1")
    else:
        print("n3")
else:
    if n2>n3:
        print("n2")
    else:
        print("n3")

'''
div=int(input("enter number"))
if div%3==0 and div%5==0 and div%15==0 :
    print("div by 15")
elif div%3==0 and div%15!=0:
    print("div by 3")
elif div%5==0 and div%15!=0:
    print("div by 5")
else:
    print("not div")
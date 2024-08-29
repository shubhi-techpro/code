number=int(input("Enter a integer")) # input always take string as input
if number < 0 :
    print("negative")
    print("try again to be positive")
else:
    print("positive")

s=int(input("enter number to check even odd"))
if s%2==0:
    print("even")
else:
    print("odd")

sp=int(input("enter selling price"))
cp=int(input("enter cost price"))
pl=sp-cp
if pl>0:
    print("profit")
    print("rupee ",pl)
elif pl==0:
    print("no loss no profit")
else:
    print("loss",pl)


num=int(input("enter number to check 4 digit or not"))
if num>999 and num<10000:
    print("number is 4 digit number")
else:
    print("number is invalid")

    
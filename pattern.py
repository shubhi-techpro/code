a=9

for _ in range(a) :
    print("*"*9)

for i in range(a):
    print(i,end=" ")

for i in range(a):
    for j in range(1,a+1):
        print(i,end=" ")
    print()

for i in range(a):
    for j in range(i):
        print(j,end=" ")
    print()

'''   *  
     ***
    *****    '''   
for i in range(a):
    print(" "*i)
    for j  in range(i):
        for k in range(j):

            print(" ",i,end=" ")
    print()


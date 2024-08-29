s=input("enter string")

a="abcdefghijklmnopqrstuvwxyz"
ar=a[::-1]
dic=dict(zip(a,ar))
print(dic)
print(len(s))
rev=""
for i in range(0,len(s)):
    rev=rev+dic[s[i]]

print(rev)


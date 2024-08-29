s=input("enter string")
n=int(input("enter index"))

s1="abcdefghijklmnopqrstuvwxyz"
rev=s1[::-1]
dic1=dict(zip(s1,rev))
print(dic1)

prefix=s[0:n-1]
suffix=s[n-1:]

mirror=""
for i in range(0,len(suffix)):
    mirror=mirror+dic1[suffix[i]]

res=prefix+mirror
print(res)
g=list(s)
g.reverse()
f=str(g)
print(f)

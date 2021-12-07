import itertools as it
n=int(input())
a=input().split(" ")
k=int(input())
q=a[k-1]
m=0
b=list(it.combinations(a,k))
print(b)
p=len(b)
for i in b:
    if q in i:
        m+=1
r=m/p
print(round(r,4))

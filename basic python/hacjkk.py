def squre(a):
    n=len(a)
    for i in range(n):
        a[i]=a[i]*a[i]
    return a


n=input()
n1=list(n.split(' '))
n=int(n1[0])
k=int(n1[1])
b1=[]
for i in range(n):
    b=[]
    a=input()
    b=(list(a.split(' ')))
    for j in range(len(b)):
        b[j]=int(b[j])
    b1.append(max(b))
print(b1)
print(squre(b1))
print(sum(b1)%k)

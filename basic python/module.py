a=input('enter string\n')
b=[]
c=['0','1','2','3','4','5','6','7','8','9']

for i in range(len(a)):
        k=(a[i])
        if k in c:
           b.append(int(a[i]))

b.sort()
i=0
k=0
for i in range(len(b)):
    if b[i]%2==0:
        k=i
        break
if k==0:
    print("-1")
else:
    p=b[k]
    b.remove(p)
    b.reverse()
    b.append(p)
    sum1=0
    for i in range(len(b)):
        sum1=b[i]+sum1*10
    print(sum1)


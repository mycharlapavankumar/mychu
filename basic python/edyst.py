
p=input()
b=p.split(' ')
c=[]
k=[]
for i in range(0,len(b),2):
    c.append(b[i].lower())
for i in range(1,len(b),2):
    k.append(b[i])
c.sort()
k.sort()
for i in range(len(c)):
    print(f'{c[i]} {k[i]}',end=' ')


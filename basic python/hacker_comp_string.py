n=input()
p=n[0]
b=[]
k=1
for i in range(1,len(n)):
    if p==n[i]:
        k+=1
    else:
        a=(k,int(p))
        b.append(a)
        k=1
    p=n[i];
a=(k,int(p))
b.append(a)
for i in b:
    print(i,end=' ')
   

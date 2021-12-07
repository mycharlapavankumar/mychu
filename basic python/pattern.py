n=int(input())
k=n+n-1
p=0
b=[[]*k]*k
a=[['p']*k]*k
for p in range(n):
    for i in range(p,k-p,1):
        for j in range(p,k-p,1):
            if (i==p or j==p or i==k-1-p or j==k-p-1):
                a[i][j]=n-p
            b[i]=a[i].copy()

            
    
'''for i in range(k):
    for j in range(k):
        print(b[i][j],end=' ')
    print()'''
for i in b:
    for j in i:
        print(j,end=" ")
    print()
        

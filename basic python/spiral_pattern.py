'''n=3
1 2 3
8 9 4
7 6 5'''
n=3;
k=1;
a=[[5]*n]*n;
b=[[]*n]*n;
i=0;
for j in range(0,n):
    a[i][j]=k;
    k=k+1;
b[i]=a[i].copy()

print(a,j)
for i in range(1,n):
    a[i][j]=k;
    k+=1;
b[i]=a[i].copy()
print(a)
for j in range(n-1,0,-1):
    a[i][j]=k
    k+=1;
b[i]=a[i].copy()
print(a)
for i in range(n-1,1,-1):
    a[i][j]=k;
    k+=1
b[i]=a[i].copy()
    
    
    

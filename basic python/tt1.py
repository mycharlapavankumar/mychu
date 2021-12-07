'''
- - - - - c - - - - - 
- - - b - c - b - - - 
- a - b - c - b - a - 
- - - b - c - b - - - 
- - - - - c - - - - -
'''

n= int(input('eneter'))
n1=n+3*(n-1)
b=[];
for i in range(n):
    b.append(chr(97+i))


b1=[['-']*n1]*n
a=[[]*n1]*n
'''for j in range(n):
    for k in range(n1):
           print(b1[j][k],end=' ')
    print()'''

for i in range(n):
    p=-1
    k=0
    for j in range(i+1):
        b1[i][n1//2-j-k]=b[p]
        b1[i][n1//2+j+k]=b[p]
        p-=1
        k+=1
        a[i]=b1[i].copy()
        
      #  print("i,n1//2-j",n1//2-j)
        
     
for j in range(n):
    for k in range(n1):
           print(a[j][k],end=' ')
    print()
for j in range(n-2,-1,-1):
    for k in range(n1):
           print(a[j][k],end=' ')
    print()

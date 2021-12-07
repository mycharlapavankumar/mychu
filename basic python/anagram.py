def ror(a,n):
    
    for j in range(n):
        k=a[-1]
        for i in range(len(a)-1,0,-1):
            a[i]=a[i-1]
        a[0]=k
    return a
def lol(a,n):
    for j in range(n):
        k=a[0]
        for i in range(len(a)-1):
            a[i]=a[i+1]
        a[-1]=k
    return a
a=input()
b=int(input())
for i in range(b):
    a1=input()
    a1=a1.split(' ')
    n=len(a)
    c=[]
    for i in range(n):
        c.append(a[i])
    if a1[0]=='R':
        c=lol(c,int(a1[1]))
    else:
        c=ror(c,int(a1[1]))
        
if a[0]==c[0]:
    print('yes')
else:
    print('no')
print(c)
    

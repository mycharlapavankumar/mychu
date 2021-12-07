n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
        a.remove(i)
b.sort()
a.sort()
n1=a.count(a[-1])
n2=b.count(b[-1])
vis=0
if n1>n2:
    if a[-1]>b[-1]:
        vis=n1
    else:
        vis=n2+n1
else:
        if a[-1]>b[-1]:
            vis=n2
        else:
            vis=n1+n2
print(vis)
    

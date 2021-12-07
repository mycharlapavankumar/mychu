import math
def prime(a):
    b=1
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            b=0
            break
    return b
n=int(input())
b=[]
for i in range(2,n):
    a=prime(i)
    if a==1:
        b.append(i)
sum1=2
count=0
for i in range(2,len(b)):
    p=sum(b[:i])
    if p in b:
          count+=1
          print(p)
print(count)
                   

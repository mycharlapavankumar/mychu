k=int(input())
n=list(map(int,input().split()))
k1=int(input())
sum1=0
for i in range(k1):
    s,am=map(int,input().split())
    if s in n:
        n.remove(s)
        sum1=am+sum1
print(sum1)
    
    

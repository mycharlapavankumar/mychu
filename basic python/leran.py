k=set(map(int,input().split()))
n=int(input())
k1=1
for i in range(n):
    n1=set(map(int,input().split()))
   
    if k.difference(n1)!=0:
        k1=0
        print(k.difference(n1))
if k1==0:
    print("False")
else:
    print("True")


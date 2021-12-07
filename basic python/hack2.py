string=input()
k=int(input())
j=0
n=len(string)
a=['pav']*(n//k)
for i in range(0,n,k):
    a[j]=string[i:i+k]
    j=j+1
print(a)
for i in range(n//k):
    p=[]
    for j in range(len(a[i])):
        if a[i][j] not in p:
            p.append(a[i][j])
    for i1 in range(len(p)):
        #if p[i1] not in a[i]:
            print(p[i1],end='')
    print()

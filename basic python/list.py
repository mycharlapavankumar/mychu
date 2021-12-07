n=int(input())
a1=[]
for i in range(n):
    a=input()
    b=list(a.split(' '))
    if b[0]=='I':
        a1.append(int(b[1]))
    else:
        a1.remove(int(b[1]))
print(a1)
    

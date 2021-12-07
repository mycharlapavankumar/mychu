n=int(input())
b=[]
for i in range(1,n+1):
    b.append(i)
oc1=len(oct(n))
he1=len(hex(n))
bi1=len(bin(n))
for i in b:
    print(" "*3,end='')
    print(i,end=' ')
    oc=oct(i);
    print(oc[2:]," "*(oc1-len(oc)),end="")
    #print(oc[2:].rjust(len(oc[2:])+1," "),end='')
    he=hex(i).upper()
    print(he[2:]," "*(he1-len(he)),end="")
   # print(he[2:].rjust(len(he[2:])+1," "),end=' ')
    bi=bin(i)
    print(bi[2:]," "*(bi1-len(bi)),end="")
   # print(bi[2:].ljust(len(he[2:])+1," "),end='')
    print()

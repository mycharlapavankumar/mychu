size=int(input('size_of_sequncy='))
a=['none']*size
for i in range(size):
    a[i]=int(input(f'{i+1}enter'))
         
n=a.index(5)
n1=a.index(8)
sum1=0
sum2=0
l=len(a)
for i in range(n):
    sum1=sum1+a[i]
   
for i in range(n1+1,l):
    sum2=sum2+a[i]


sum3=0
for i in range(n,n1+1):
     sum3=a[i]+sum3*10
sum_all=sum1+sum2+sum3
print(sum_all)

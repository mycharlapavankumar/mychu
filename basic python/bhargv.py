n=input();
a=[]
for i in n:
    if (i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or  i=='6' or i=='7' or i=='8' or  i=='9'):
        a.append(int(i))
print(a);
a.sort()
for i in range(1,len(a)):
    if a[i]%2==1:
        k=a[i]
a.remove(k)
a.append(k)
sum=0;
for i in a:
    sum =sum*10+i;

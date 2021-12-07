a=input()
b=a.split(' ')
for i in range(len(b)):
    b[i]=int(b[i])
sum1=0
check=0
if b[0]>b[1]:
    move1=b[0]
    move2=b[1]
    sum1=b[0]
    k='F'
    check=b[3]
else:
    move1=b[1]
    move2=b[0]
    sum1=b[1]
    k="B"
    check=b[2]
count=sum1
while(sum1<check):
    sum1=sum1-move2
    sum1=sum1+move1
    count=move2+count+move1
    print(count)
if sum1>check:
    count=count-(sum1-check)
print(count*b[2],k)


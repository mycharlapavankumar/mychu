amount=int(input('enter_amount='))
no_of_five =int(input('enter_no_of_5='))
no_of_one=int(input('enter no_of_1='))
a=amount//5
chnge_1=0;
chnge_5=0;
if a==no_of_five:
    chnge_5=no_of_five
elif a<no_of_five:
    chnge_5=a
else :
    while((no_of_five*5)<(a*5)):
        a=a-1
    chnge_5=a
b=amount-5*chnge_5
if b<=no_of_one:
    chnge_1=b

if amount==(chnge_1+chnge_5*5):
    print(f'5rupee={chnge_5}--1rupee={chnge_1}')
else:
    print("chnge=-1")
    

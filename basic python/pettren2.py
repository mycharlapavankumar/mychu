'''1      1 
 2    2  
  3  3   
   44    
    5
   44   
  3  3  
 2    2 
1      1
'''





n=int(input());
k=2*n-1;
for i in range(1,n+1):
    for j in range(1,k+1):
        if(i==n):
            print(' '*(n-1),end="");
            print(i,end="");
            break;
        elif(j==i or j==k-i):
            print(i,end="");
        else:
            print(' ',end="");
    print();
for i in range(n-1,0,-1):
    for j in range(k-1,0,-1):
        if(i==n):
            
            break;
        elif(j==i or j==k-i):
            print(i,end="");
        else:
            print(' ',end="");
    print();

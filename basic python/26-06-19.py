import itertools
a=[1,2,3,4,5,6,7,8,9]
for i in range(1,len(a)):
    b=list(itertools.combinations(a,i))
    for j in range(len(b)):
        print(a.index(8))
        
  

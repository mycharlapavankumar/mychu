
n=[[1,2,3],[4,5,6],[7,8,9]]
k=2
nl=len(n)
ss=[]
for i in range(nl):
        s1=[]
        for j in range(nl):
                s=0;
                if i<nl-1 and j<nl-1:
                        for ii in range(i,i+k):
                                for jj in range(j,j+k):
                                        #print('i=',i,"j=",j,"ii=",ii,"jj=",jj)
                                        s+=n[ii][jj]
                        
                        s1.append(s)
        ss.append(s1)
        
             
for i in ss[:-1]:
        for j in i:
                print(j ,end=" ")
        print()
                

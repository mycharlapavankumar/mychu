class employee:
    def __init__(self,n,i,a,g):
        self.n=n
        self.i=i
        self.a=a
        self.g=g

class organ:
    def __init__(self,na,e):
        self.na=na
        self.e=e
    def addemp(self,n,i,a,g):
        s=employee(n,i,a,g)
        self.e.append(s)
    def getempc(self):
        return len(self.e)

    def finage(self,ii):
        for j in self.e:
            if(j.i==ii):
                return j.a

        return -1
    def countemp(self,ag):
        count=0
        for i in self.e:
            if(i.a>ag):
                count+=1

        return count




emp=[]
o=organ('asd',emp)
n=int(input())
for i in range(n):
    name=input()
    id=int(input())
    age=int(input())
    gen=input()
    o.addemp(name,id,age,gen)


id=int(input())
#age=input()
#print(o.getempc())
print(o.finage(id))
#print(o.countemp(age))

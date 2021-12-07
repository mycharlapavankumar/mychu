class time:
    def __init__(self,h,m):
        self.h=h
        self.m=m

    def add(t1,t2):
        t3=time(0,0)
        if t1.m+t2.m>60:
            t3.h=round(t1.h+1+t2.h)
            t3.m=t1.m+t2.m-60
        else :
            t3.h=t1.h+t2.h
            t3.m=t1.m+t2.m
            
        
        return t3
    def dis(self):
        print(self.h,self.m)

    def dispm(self):
        print(self.h*60+self.m)


a=time(2,10)
b=time(1,20)
c=time.add(a,b)
c.dis()
c.dispm()
a.dis()
b.dis()

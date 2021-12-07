class prof:
    def __init__(self,pid,pname,subdit):
        self.pid=pid
        self.pname=pname
        self.subdit=subdit
    
class univ:
    def __init__(self,name):
        self.name=name
    def getexp(self,pl,id):
        for i in pl:
            if i.pid==id:
                return sum(i.subdit.values()) 

        return 0
    def ssp(self,pl,s):
        m=0
        k=0
        for i in pl:
            if s in i.subdit.keys():
                if m<i.subdit[s]:
                    m=i.subdit[s]
                    p=i
                    k=1
        if k==1:
            return p
        else:
            return None



if __name__=='__main__':
    n=int(input())
    p=[]
    for i in range(n):
        pid=int(input())
        pname=input()
        l=int(input())
        s=dict()
        for j in range(l):
            pp=input().upper()
            s[pp]=int(input())
        p.append(prof(pid,pname,s))

    u=univ('xyz')
    k=int(input())
    print(u.getexp(p,k))
    sub=input().upper()
    pp=u.ssp(p,sub)
    print(pp.pid,pp.pname,pp.subdit)


if __name__ == '__main__':
    n=int(input())
    name=[5]*n
    score=[5]*n
    for i in range(n):
        name[i] = input()
        score[i] = float(input())
    c=score.copy()
    c.sort()
    c.reverse()
    print(score,c)
    k=[]
    p=-2
    if c.count(c[-1])==1:
        p=-2
    else:
        b=c.count(c[-1])
        p=p-b
    b=c.count(c[p])
    for i in range(b):
        h=c[p-i]
        k1=score.index[h]
        c.remove(c[h])
        k.append(name[k1])
    print(k)
     
            






def is_prime(x):
    return not bool(sum([x % i == 0 for i in range(2, int(1+x**.5))]))


def prime_list(n):
        a=[i for i in range(2,n+1) if is_prime(i)]
        return a
def sum_check(n):
    prime_sum = 0
    c=[]
    p = prime_list(n)
    for i in range(len(p)):
        check = sum(p[:i])
        if check in p:
            c.append(check)
    for i in c[1:]:
        print(i)
a=int(input())
sum_check(a)

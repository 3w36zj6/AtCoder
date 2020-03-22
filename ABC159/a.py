import math

def perm(n, r):
    return math.factorial(n)//math.factorial(n-r)

def comb(n, r):
    if n <= 1:
        return 0
    return perm(n, r)//math.factorial(r)

N, M = map(int,input().split(" "))

ans = comb(N,2) + comb(M,2)


print(int(ans))
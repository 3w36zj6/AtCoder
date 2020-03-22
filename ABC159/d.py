from collections import Counter
import math

def perm(n, r):
    return math.factorial(n)//math.factorial(n-r)

def comb(n, r):
    if n <= 1:
        return 0
    return perm(n, r)//math.factorial(r)

N = int(input())
A = list(map(int,input().split(" ")))

for k in range(N):
    #print(k)
    A_ = A[:]
    A_.pop(k)
    A_counter = Counter(A_)
    #print(A_counter)
    ans = 0
    for v in A_counter.values():
        #print(v)
        ans += comb(v,2)
    print(ans)

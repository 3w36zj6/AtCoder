N, K = map(int,input().split())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

L = prime_factorize(N)

if K > len(L):
    ans = [-1]
else:
    len_L = len(L)
    for i in range(len_L - K):
        #print(L)
        tmp = L.pop(-1)
        L[-1] *= tmp
        
    ans = L



print(*ans)
T = int(input())
cases = [list(map(int, input().split())) for i in range(T)]


def f(n): return n*(n+1)//2


for L, R in cases:
    #print(L, R)
    if R-2*L+1 > 0:
        print(f(R-2*L+1))
    else:
        print(0)

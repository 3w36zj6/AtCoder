N, Y = map(int,input().split())

def answer():
    for n_10000 in range(N+1):
        for n_5000 in range(N+1):
            n_1000 = N - n_10000 - n_5000
            if n_1000 < 0:
                continue
            if n_10000 * 10000 + n_5000 * 5000 + n_1000 * 1000 == Y:
                return (n_10000, n_5000, n_1000)
    return (-1, -1, -1)
                
print(" ".join(list(map(str,answer()))))
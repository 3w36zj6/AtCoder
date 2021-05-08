N, K = map(int,input().split())

n = N
for i in range(K):
    if n % 200 == 0:
        n //= 200
    else:
        n = int(str(n) + "200")

print(n)
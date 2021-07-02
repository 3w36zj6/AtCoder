N, X = map(int, input().split())
*A, = map(int, input().split())
A = [0]+A+[0]

ans = 0
for i in range(N+1):
    if A[i]+A[i+1] > X:
        ans += A[i+1] - (X - A[i])
        A[i+1] = X - A[i]


print(ans)

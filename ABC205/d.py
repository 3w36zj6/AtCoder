import bisect
N, Q = map(int, input().split())
*A, = map(int, input().split())
C = [A[i] - (i + 1) for i in range(N)]

for _ in range(Q):
    K = int(input())
    i = bisect.bisect_left(C, K)
    if i == 0:
        print(K)
    elif i == N:
        print(K + N)
    else:
        print(A[i - 1] + (K - C[i - 1]))

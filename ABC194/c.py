import itertools

N = int(input())
A = list(map(int, input().split()))
A.sort()
S = [0]+list(itertools.accumulate(A))
A2 = list(map(lambda x: x ** 2, A[:]))
S2 = [0]+list(itertools.accumulate(A2))

ans = 0
for i in range(1, N):
    a = A[i-1]
    ans += (N-i)*(a**2)+(S2[N]-S2[i])-2*a*(S[N]-S[i])

print(ans)
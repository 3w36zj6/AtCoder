N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    if A[i]%2 == 1 and (i+1)%2 == 1:
        ans += 1
print(ans)
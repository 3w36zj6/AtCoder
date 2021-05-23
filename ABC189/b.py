N, X = map(int, input().split())

total = 0
ans = -1
for i in range(N):
    V, P = map(int, input().split())
    total += V * P
    if total > X * 100:
        ans = i + 1
        break

print(ans)

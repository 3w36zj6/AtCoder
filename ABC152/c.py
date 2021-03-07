N = int(input())
P = list(map(int, input().split()))

ans = 0
max_p = min_p = P[0]

for p in P:
    if p > max_p or p > min_p:
        pass
    else:
        ans += 1

    max_p = max(max_p, p)
    min_p = min(min_p, p)

print(ans)
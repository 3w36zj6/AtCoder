N, M = map(int, input().split())
L = [-1] * (N + 1)

ans = 0
for i in range(M):
    s, c = map(int,input().split())
    if L[s] == -1 or L[s] == c:
        L[s] = c
    else:
        ans = -1
        break

if N == 1 and (L[1] == 0 or L[1] == -1):
    ans = 0
elif ans != -1:
    for i in range(1, N + 1):
        if L[i] == 0 and i == 1:
            ans = -1
            break
        if L[i] == -1:
            if i == 1:
                L[i] = 1
            else:
                L[i] = 0
        ans += L[i] * (10 ** (N - i))

print(ans)
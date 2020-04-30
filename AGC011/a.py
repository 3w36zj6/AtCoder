N, C, K = map(int,input().split())
T = [int(input()) for i in range(N)]

T.sort(reverse=True)

#print(T)
t_before = T[0]
cnt = 0
ans = 0
for t in T:
    #print(t, t_before, cnt, ans)
    if t_before - t <= K and cnt + 1 <= C:
        cnt += 1
        continue
    else:
        t_before = t
        cnt = 1
        ans += 1

print(ans+1)
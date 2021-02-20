N, K = map(int, input().split())

# init
a = N
ans = N
for i in range(1, K+1):
    g_1 = "".join(sorted(str(a), key=lambda x: int(x), reverse=True))
    g_2 = g_1[::-1]
    f = int(g_1) - int(g_2)

    if i == K or f == a:
        ans = f
        break

    # update
    a = f

print(ans)
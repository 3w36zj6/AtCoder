N = M = 4
c = [list(input().split()) for r in range(N)]

# 180度回転
ans = [[""]*M for r in range(N)]
for i in range(N):
    for j in range(M):
        # 上下逆にして左右逆
        ans[i][j] = c[N-1-i][M-1-j]

for row in ans:
    print(*row)


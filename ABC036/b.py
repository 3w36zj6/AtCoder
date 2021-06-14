N = M = int(input())
s = [list(input()) for r in range(N)]

# 時計回りに90度回転
ans = [[""]*N for r in range(M)]
for i in range(N):
    for j in range(M):
        # 上下逆にして転置
        ans[j][N-1-i] = s[i][j]

# 転置して上下逆で反時計回りに90度回転

for row in ans:
    print("".join(row))
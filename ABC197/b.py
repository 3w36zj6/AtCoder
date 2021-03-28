H, W, X, Y = map(int, input().split())
S = []
for h in range(H):
    S.append(input())

count = 1

# 上
x = X - 1 - 1
y = Y - 1
while (0 <= x <= H-1) and (0 <= y <= W-1):
    if S[x][y] == ".":
        count += 1
        x -= 1
    else:
        break

# 下
x = X - 1 + 1
y = Y - 1
while (0 <= x <= H-1) and (0 <= y <= W-1):
    if S[x][y] == ".":
        count += 1
        x += 1
    else:
        break

# 右
x = X - 1
y = Y - 1 + 1
while (0 <= x <= H-1) and (0 <= y <= W-1):
    if S[x][y] == ".":
        count += 1
        y += 1
    else:
        break

# 左
x = X - 1
y = Y - 1 - 1
while (0 <= x <= H-1) and (0 <= y <= W-1):
    if S[x][y] == ".":
        count += 1
        y -= 1
    else:
        break

print(count)
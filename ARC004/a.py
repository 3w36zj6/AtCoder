N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]

from math import sqrt

ans = 0
for i in range(N):
    for j in range(N):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        ans = max(ans, sqrt((x1 - x2)** 2 + (y1 - y2)** 2))

print(ans)
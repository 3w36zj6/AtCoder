N = int(input())
APX = [list(map(int, input().split())) for i in range(N)]

ans = -1
for apx in APX:
    if apx[0] < apx[2]:
        if ans == -1:
            ans = apx[1]
        else:
            ans = min(ans, apx[1])

print(ans)
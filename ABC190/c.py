N, M = map(int, input().split())

conditions = [list(map(int, input().split())) for i in range(M)]

K = int(input())
plates = [list(map(int, input().split())) for i in range(K)]

ans = 0
for i in range(2 ** K):
    # 選び方決定
    balls = [0 for i in range(N + 1)]
    for j, c in enumerate(format(i, 'b').zfill(K)):
        balls[plates[j][int(c)]] += 1

    # 満たす条件の個数
    cnt = 0
    for condition in conditions:
        if balls[condition[0]] > 0 and balls[condition[1]] > 0:
            cnt += 1

    ans = max(ans, cnt)

print(ans)
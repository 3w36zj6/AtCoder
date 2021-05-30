from collections import deque
N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[0])
ab = deque(AB)

k = K
ans = 0
cnt = 0

while k > 0:
    # いけるとこまでいく
    ans += k
    k = 0
    for i in range(N-cnt):  # 道中のお金をもらう
        if len(ab):
            a, b = ab[0]
        else:
            break
        if a <= ans:
            k += b
            ab.popleft()
        else:
            cnt += i
            break

print(ans)

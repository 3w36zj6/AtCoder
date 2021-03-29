N = int(input())
t = [int(input()) for i in range(N)]

import itertools

ans = float("inf")
for bits in itertools.product([0, 1], repeat=N):
    candidates = [0, 0]
    for i, bit in enumerate(bits):
        candidates[bit] += t[i]

    ans = min(max(candidates), ans)

print(ans)
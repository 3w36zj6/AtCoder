import itertools
N, M = map(int, input().split())
xy = [list(map(int, input().split())) for i in range(M)]

acquaintances = [[] for i in range(N + 1)]

for x, y in xy:
    acquaintances[x].append(y)
    acquaintances[y].append(x)

ans = 0

for bits in itertools.product([0, 1], repeat=N):
    check = True
    for i, bit in enumerate(bits):
        if bit:
            for j, bit in enumerate(bits):
                if i == j or not bit:
                    continue
                if not (i + 1) in acquaintances[j + 1]:
                    check = False
                    break
    if check:
        ans = max(bits.count(1), ans)

print(ans)
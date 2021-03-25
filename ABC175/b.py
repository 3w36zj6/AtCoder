N = int(input())
L = list(map(int, input().split()))

import itertools

ans = 0
for a, b, c in itertools.combinations(L, 3):
    if len(set([a, b, c])) == 3 and a + b > c and b + c > a and c + a > b:
        ans += 1

print(ans)
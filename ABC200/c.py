N = int(input())
*A, = map(int,input().split())

for i in range(N):
    A[i] %= 200

import collections

counter = collections.Counter(A)

ans = 0
for a, cnt in counter.items():
    ans += cnt*(cnt-1)//2

print(ans)
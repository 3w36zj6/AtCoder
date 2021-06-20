import collections
N = int(input())
*A, = map(int, input().split())

counter = collections.Counter(A)

ans = 0
for i, a in enumerate(A):
    counter[a] -= 1
    ans += N-(i+1)-counter[a]

print(ans)

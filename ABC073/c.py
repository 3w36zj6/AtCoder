import collections

N = int(input())
A = [int(input()) for i in range(N)]

A_counter = collections.Counter(A)

ans = 0
for a in A_counter.items():
    
    if a[1] % 2 != 0:
        ans += 1

print(ans)
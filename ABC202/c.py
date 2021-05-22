N = int(input())
*A, = map(int,input().split())
*B, = map(int,input().split())
*C, = map(int,input().split())

import collections

A_set = set(A)
A_counter = collections.Counter(A)


candidates = []
for c in C:
    candidates.append(B[c-1])


candidates_counter = collections.Counter(candidates)
candidates_set = set(candidates)

ans = 0
for a in A_set:
    ans += A_counter[a]*candidates_counter[a]

print(ans)
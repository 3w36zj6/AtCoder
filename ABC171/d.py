import collections

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
BC = [list(map(int,input().split())) for i in range(Q)]

sum_ = sum(A)
counter = dict(collections.Counter(A))

for i in range(Q):
    b, c = BC[i]
    if not b in counter:
        counter[b] = 0
    if not c in counter:
        counter[c] = 0
    cnt = counter[b]
    sum_ += (c-b)*cnt
    print(sum_)
    counter[b] -= cnt
    counter[c] += cnt
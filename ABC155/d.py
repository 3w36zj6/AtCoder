N, K = map(int,input().split(" "))
A = map(int,input().split(" "))

import itertools

L = []

for x in itertools.combinations(A, 2):
    L.append(x[0]*x[1])

L.sort()

print(L[K-1])
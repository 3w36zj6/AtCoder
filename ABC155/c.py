N = int(input())
S = [input() for i in range(N)]

import collections

c = collections.Counter(S)

#最頻値の個数
mx = c.most_common()[0][1]#c[max(c)]


L = set()
for s in S:
    if c[s] == mx:
        L.add(s)

L = list(L)
L.sort()
for l in L:
    print(l)


N, M, X = map(int,input().split())
lines = [list(map(int,input().split())) for i in range(N)]

#print(lines)

import itertools

result = []
for n in range(1,len(lines)+1):
    for conb in itertools.combinations(lines, n):
        result.append(list(conb)) #タプルをリスト型に変換

candidates = set()
for r in result:
    #print(r)
    tmp = [0 for _ in range(M+1)]
    for line in r:
        for i, l in enumerate(line):
            tmp[i] += l
    #print(r, tmp)#, list(enumerate(r)))
    flag_add = True
    for i in range(M):
        if tmp[1+i] < X:
            flag_add = False
            break
    if flag_add:
        candidates.add(tmp[0])

ans = min(candidates) if len(candidates) != 0 else -1
print(ans)
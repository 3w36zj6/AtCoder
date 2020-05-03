N, M = map(int,input().split())
H = list(map(int,input().split()))
pairs = [list(map(int,input().split())) for i in range(M)]

connection = {}
for pair in pairs:
    if not pair[0] in connection:
        connection[pair[0]] = set()
    if not pair[1] in connection:
        connection[pair[1]] = set()
    connection[pair[0]].add(pair[1])
    connection[pair[1]].add(pair[0])

#print(connection)

ans = 0
for i, h in enumerate(H):
    candidates = []
    for c in list(connection.get(i+1,set())):
        candidates.append(H[c-1])
    #print(i, h, candidates)
    if len(candidates) == 0 or h > max(candidates):
        ans += 1
print(ans)
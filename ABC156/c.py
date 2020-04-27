N = int(input())
X = list(map(int,input().split()))

candidates = []
for p in range(min(X), max(X)+1):
    #x=pで開催するとき
    #print(p)
    c = sum([(x - p)**2 for x in X])
    candidates.append(c)

print(min(candidates))
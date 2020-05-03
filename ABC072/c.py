N = int(input())
A = list(map(int,input().split()))

counts = {}
for a in A:
    for i in [a-1, a, a+1]:
        if not i in counts:
            counts[i] = 0
        counts[i] += 1


counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)

print(counts[0][1])
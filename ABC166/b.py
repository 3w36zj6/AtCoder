N, K = map(int,input().split())
counts = [0 for i in range(N)]

for i in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    for a in A:
        counts[a-1] += 1
    
print(counts.count(0))
N, K = map(int,input().split())
H = list(map(int,input().split()))
H.sort(reverse=True)

count = sum(H[K:])

print(count)
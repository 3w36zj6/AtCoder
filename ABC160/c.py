K, N = list(map(int,input().split(" ")))
A = list(map(int,input().split(" ")))
A.append(K+A[0])

D = []
for i in range(N):
    D.append(abs(A[i]-A[i+1]))


D.sort()
print(sum(D[:N-1]))
N = int(input())
*A, = map(int, input().split())
A = [0]+A+[0]

S = 0
for i in range(1, N+1+1):
    S += abs(A[i] - A[i-1])

for i in range(1, N+1):
    print(S-abs(A[i]-A[i-1])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))

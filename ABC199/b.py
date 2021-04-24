N = int(input())
* A, = map(int, input().split())
* B, = map(int, input().split())

check = set()
for j in range(A[0], B[0] + 1):
    check.add(j)

ans = 0
for i in range(1, N):
    if A[i] <= B[i]:
        c = set()
        for j in range(A[i], B[i] + 1):
            c.add(j)
        check = c & check

print(len(check))

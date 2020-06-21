N = int(input())
a = list(map(int,input().split()))

X = 0
for i in range(N):
    X ^= a[i]

answers = []
for i in range(N):
    answers.append(X^a[i])
print(*answers)
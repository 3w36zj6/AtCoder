N = int(input())
A = list(map(int,input().split()))

answers = [0 for i in range(N)]
for a in A:
    answers[a-1] += 1

for ans in answers:
    print(ans)
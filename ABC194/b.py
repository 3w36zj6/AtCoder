N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]
AB.sort(key=lambda x: x[0])
min_a = AB[0][0]
min_a2 = AB[1][0]
min_ab = AB[0][:]

AB.sort(key=lambda x: x[1])
min_b = AB[0][1]

if min_ab == AB[0]:
    ans = min(min_a+min_b, max(min_a, AB[1][1]), max(min_b, min_a2))
else:
    ans = max(min_a, min_b)

print(ans)
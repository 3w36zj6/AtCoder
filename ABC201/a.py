import itertools
*A, = map(int, input().split())

ans = "No"
for a1, a2, a3 in itertools.permutations(A, 3):
    if a3-a2 == a2-a1:
        ans = "Yes"
        break

print(ans)

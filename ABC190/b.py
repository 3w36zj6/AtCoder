N, S, D = map(int, input().split())

spells = [list(map(int, input().split())) for i in range(N)]

ans = "No"
for spell in spells:
    if spell[0] < S and spell[1] > D:
        ans = "Yes"
        break

print(ans)

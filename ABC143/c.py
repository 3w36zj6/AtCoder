N = int(input())
S = input()

tmp = None
ans = 0
for s in S:
    if tmp != s:
        tmp = s
        if tmp != None:
            ans += 1

print(ans)
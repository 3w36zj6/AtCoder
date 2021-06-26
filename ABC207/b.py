A, B, C, D = map(int, input().split())

mizu = A
aka = 0
ans = 0
for i in range(10**5+2):
    if mizu <= aka * D:
        break
    else:
        mizu += B
        aka += C
        ans += 1
else:
    ans = -1

print(ans)

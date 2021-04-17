X, Y, Z = map(int, input().split())
for i in range(10000000, -1, -1):
    if i / Z < Y / X:
        ans = i
        break
print(ans)

n = int(input())
ans = 0

for i in range(1, 6):
    if n >= 10 ** (3 * i):
        ans += n - 10 ** (3 * i) + 1

print(ans)

N = int(input())

ans = 0
# 2桁
ans += min(N // 11, 9)

# 4桁
if N >= 1010:
    ans += min((N - 1010) // 101 + 1, 90)

# 6桁
if N >= 100100:
    ans += min((N - 100100) // 1001 + 1, 900)

# 8桁
if N >= 10001000:
    ans += min((N - 10001000) // 10001 + 1, 9000)

# 10桁
if N >= 1000010000:
    ans += min((N - 1000010000) // 100001 + 1, 90000)

# 12桁
if N >= 100000100000:
    ans += min((N - 100000100000) // 1000001 + 1, 900000)

# 14桁
if N >= 10000001000000:
    ans += min((N - 10000001000000) // 10000001 + 1, 9000000)

print(ans)
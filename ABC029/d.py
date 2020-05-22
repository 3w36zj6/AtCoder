N = int(input())
ans = 0
for i in range(N+1):
    ans += str(i).count("1")

print(ans)
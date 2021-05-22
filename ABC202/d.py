A, B, K = map(int,input().split())

from math import factorial

# 辞書順
a, b = A, B
total = 0
ans = ""
for i in range(60):
    if a == 0 and b == 0:
        break
    elif a == 0:
        b = max(b-1, 0)
        ans += "b"
    elif b == 0:
        a = max(a-1, 0)
        ans += "a"
    elif total + factorial(a+b-1)//(factorial(a-1)*factorial(b)) >= K:
        a = max(a-1, 0)
        ans += "a"
    else:
        total += factorial(a+b-1)//(factorial(a-1)*factorial(b))
        b = max(b-1, 0)
        ans += "b"

print(ans)

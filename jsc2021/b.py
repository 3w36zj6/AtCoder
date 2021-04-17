N, M = map(int, input().split())
* A, = map(int, input().split())
* B, = map(int, input().split())
set_A = set(A)
set_B = set(B)

ans = list(((set_A - set_B) | (set_B - set_A)))
ans.sort()
if ans:
    print(*ans)

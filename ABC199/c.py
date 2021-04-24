N = int(input())
S = input()
Q = int(input())

TAB = [list(map(int, input().split())) for i in range(Q)]

ans = list(S)
flip = False

for t, a, b in TAB:
    if t == 1:
        if flip:
            a_ = a + N if a <= N else a - N
            b_ = b + N if b <= N else b - N
            ans[a_ - 1], ans[b_ - 1] = ans[b_ - 1], ans[a_ - 1]

        else:
            ans[a - 1], ans[b - 1] = ans[b - 1], ans[a - 1]
    else:
        flip = not flip

if flip:
    print("".join(ans[N:] + ans[:N]))
else:
    print("".join(ans))
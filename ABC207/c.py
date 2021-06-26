N = int(input())
tlr = [list(map(int, input().split())) for i in range(N)]

ans = 0

for i in range(N):
    for j in range(i+1, N):
        t_i, l_i, r_i = tlr[i]
        t_j, l_j, r_j = tlr[j]

        if min(r_i, r_j)-max(l_i, l_j) > 0:  # OK
            ans += 1
            continue
        elif min(r_i, r_j)-max(l_i, l_j) == 0:
            if r_i != l_j:
                t_i, t_j = t_j, t_i
                l_i, l_j = l_j, l_i
                r_i, r_j = r_j, r_i

            if ((t_i == 1 or t_i == 3) and (t_j == 1 or t_j == 2)):
                ans += 1

print(ans)

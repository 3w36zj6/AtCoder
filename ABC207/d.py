import math
import cmath
from decimal import Decimal
N = int(input())
S = [list(map(int, input().split())) for i in range(N)]
T = [list(map(int, input().split())) for i in range(N)]


S_G = [Decimal(0), Decimal(0)]
T_G = [Decimal(0), Decimal(0)]
for i in range(N):
    S_G[0] += S[i][0]
    S_G[1] += S[i][1]
    T_G[0] += T[i][0]
    T_G[1] += T[i][1]

S_G[0] /= N
S_G[1] /= N
T_G[0] /= N
T_G[1] /= N

V_ST = [T_G[0]-S_G[0], T_G[1]-S_G[1]]

for i in range(N):
    S[i][0] += V_ST[0]
    S[i][1] += V_ST[1]

G_c = float(T_G[0]) + float(T_G[1]) * 1j
ans = "No"
for i in range(N):
    for j in range(N):
        pass
        # T_G中心に回転
        S_c = float(S[i][0]) + float(S[i][1]) * 1j
        T_c = float(T[j][0]) + float(T[j][1]) * 1j

        if S_c == G_c:
            theta = cmath.phase((T_c-G_c))
        else:
            theta = cmath.phase((T_c-G_c)/(S_c-G_c))

        # 回転角決定
        check = True
        for k in range(N):
            S_c2 = float(S[k][0]) + float(S[k][1]) * 1j
            T_c2 = (S_c2 - G_c) * cmath.exp(theta*1j) + G_c

            if math.ceil(T_c2.real) - T_c2.real < 0.0001:
                T_c2 = math.ceil(T_c2.real) + T_c2.imag * 1j
            if T_c2.real - math.floor(T_c2.real) < 0.0001:
                T_c2 = math.floor(T_c2.real) + T_c2.imag * 1j
            if math.ceil(T_c2.imag) - T_c2.imag < 0.0001:
                T_c2 = T_c2.real + math.ceil(T_c2.imag)*1j
            if T_c2.imag - math.floor(T_c2.imag) < 0.0001:
                T_c2 = T_c2.real + math.floor(T_c2.imag)*1j

            if [T_c2.real, T_c2.imag] in T:
                continue
            else:
                check = False
                break

        if check:
            ans = "Yes"
            break

print(ans)

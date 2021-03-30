S = input()

import itertools

ans = 0
# bit全探索
for bits in itertools.product([0, 1], repeat=len(S)-1):
    formula = S[0]
    for i, bit in enumerate(bits):
        if bit == 1:
            formula += "+"
        formula += S[1 + i]
    ans += eval(formula)

print(ans)
ABCD = input()

import itertools

# bit全探索
for bits in itertools.product([0, 1], repeat=3):
    formula = ABCD[0]
    for i, bit in enumerate(bits):
        if bit == 1:
            formula += "+"
        else:
            formula += "-"
        formula += ABCD[1 + i]
    if eval(formula) == 7:
        print(formula + "=7")
        break
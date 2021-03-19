import itertools
from math import ceil
D, G = map(int, input().split())
pc = [list(map(int, input().split())) for i in range(D)]

ans = float("inf")
for i, (p0, c0) in enumerate(pc):
    #print("中途半端に解く", 100*(i+1), p0, c0)

    for bits in itertools.product([0, 1], repeat=D - 1):
        score = 0
        count = 0
        bit_index = 0
        skip = False

        for j, (p, c) in enumerate(pc):
            if (not skip) and (p, c) == (p0, c0):
                skip = True
                continue
            bit = bits[bit_index]
            #print(100*(j+1), p, c, bit)
            if bit:
                score += (100 * (j + 1)) * p + c
                count += p

            bit_index += 1

        if G <= score:
            ans = min(ans, count)
        else:
            #print(bits, G-score, score, 100*(i+1)*p0)
            if G - score > 100 * (i + 1) * (p0 - 1):
                # 無理?
                if G - score <= 100 * (i + 1) * p0 + c0:
                    count += p0
                    ans = min(ans, count)
                pass
            else:
                count += ceil((G - score) / (100 * (i + 1)))

                ans = min(ans, count)

print(ans)

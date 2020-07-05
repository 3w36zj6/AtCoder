H, W, K = map(int,input().split())
C = [list(input()) for i in range(H)]

import itertools, copy
ans = 0

for h in range(H+1):
    for w in range(W+1):
        #n個選ぶ
        comb_h = list(itertools.combinations(list(range(H)), h))
        comb_w = list(itertools.combinations(list(range(W)), w))

        for ch in comb_h:
            for cw in comb_w:
                C_ = copy.deepcopy(C)
                for x in ch:
                    for i in range(W):
                        C_[x][i] = "R"
                for y in cw:
                    for i in range(H):
                        C_[i][y] = "R"

                cnt = 0
                for x in range(H):
                    for y in range(W):
                        if C_[x][y] == "#":
                            cnt += 1
                            
                if cnt == K:
                    ans += 1

print(ans)
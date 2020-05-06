N = int(input())
H = list(map(int,input().split(" ")))
H_orig = H[:]
heights = [0 for i in range(N)]

cnt = 0

while True:
    #print(heights,H)
    if min(H) > min(heights):
        for i in range(N):
            heights[i] += 1
            H[i] -= 1
        cnt += 1
    else:
        flag = False
        for i in range(N):
            #H[i]
            if H[i] > 0:
                heights[i] += 1
                H[i] -= 1
                flag = True
            else:# H[i] == 0:
                if flag:
                    cnt += 1
                    flag = False
                    
            if i == N-1 and flag:
                cnt += 1
        
    if H_orig == heights:
        break
    
print(cnt)

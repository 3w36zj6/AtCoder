N = int(input())
plans = [list(map(int,input().split())) for i in range(N)]

ans = "Yes"
before = [0, 0, 0]
for plan in plans:
    #print(plan)
    dt = plan[0] - before[0]
    dx = abs(plan[1] - before[1])
    dy = abs(plan[2] - before[2])

    if dt >= (dx+dy) and ((dt % 2 == 0 and (dx+dy) % 2 == 0) or (dt % 2 == 1 and (dx+dy) % 2 == 1)):
        pass
    else:
        ans = "No"
        break
    before = plan[:]
    
print(ans)
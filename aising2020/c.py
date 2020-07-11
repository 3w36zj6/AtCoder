N = int(input())

answers = [0 for i in range(10**4+1)]

for x in range(1,42):
    for y in range(x,100):
        for z in range(y,100):
            n = x**2+y**2+z**2+x*y+y*z+z*x
            if 0 <= n <= 10000:
                c = len(set([x,y,z]))
                if c == 1:
                    answers[n] += 1
                elif c == 2:
                    answers[n] += 3
                else:
                    answers[n] += 6

for ans in answers[1:N+1]:
    print(ans)

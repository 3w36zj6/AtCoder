N, A, B = map(int,input().split(" "))

cnt_a = cnt_b = 0

while True:
    if cnt_a + cnt_b + A >= N: 
        # N - cnt_a - cnt_b はみ出た分
        ans = cnt_a + N - cnt_a - cnt_b
        break
    else:
        cnt_a += A
        cnt_b += B

print(ans)
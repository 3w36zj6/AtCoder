S = input()


if len(S)%2 == 0:
    ans = "Yes"
    for i in range(len(S)//2):
        #print(S[2*i:2*i+2])
        if S[2*i:2*i+2] != "hi":
            ans = "No"
            break
    print(ans)
else:
    print("No")
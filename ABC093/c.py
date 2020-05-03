numbers = list(map(int,input().split()))
numbers.sort()

#print(numbers)
ans = 0
M = max(numbers)
if 3*M%2 == sum(numbers)%2:
    #print(numbers,M)
    ans += (M-numbers[0])
    ans += (M-numbers[1])
    ans += (M-numbers[2])


else:
    #print(numbers,M+1)
    ans += (M+1-numbers[0])
    ans += (M+1-numbers[1])
    ans += (M+1-numbers[2])

print(ans//2)

N = input()

def ispalindrome(str): return 1 if str == str[::-1] else 0

ans = "No"
for i in range(11):
    if ispalindrome("0" * i + N):
        ans = "Yes"
        break

print(ans)
N = int(input())
A = map(int,input().split(" "))

def check():
    for a in A:
        if a%2 == 0 and not(a%3 == 0 or a%5 == 0):
            print("DENIED")
            return

    print("APPROVED")
        
check()
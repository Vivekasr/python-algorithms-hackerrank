import sys

def extraLongFactorials(n):
    mult = 1
    for i in range(1,n+1):
        mult = mult*i
    print(mult)    
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n

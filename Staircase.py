import sys

def staircase(n):
        for i in range(1,n+1):
                print(('#'*i).rjust(n,' '))
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)

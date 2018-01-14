import sys

def miniMaxSum(arr):
        arr.sort()
        maxarr = sum(arr[1:len(arr)])
        minarr = sum(arr[0:len(arr)-1])
        print(minarr,maxarr)
    # Complete this function

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)

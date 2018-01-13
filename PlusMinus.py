import sys

def plusMinus(arr):
        lstpos = []
        lstzero = []
        lstneg = []
        for i in range(n):
                if arr[i]>0:
                        lstpos.append(arr[i])
                if arr[i]==0:
                        lstzero.append(arr[i])
                if arr[i]<0:
                        lstneg.append(arr[i])
        pos = len(lstpos)/n
        zero = len(lstzero)/n
        neg = len(lstneg)/n
        print(pos)
        print(neg)
        print(zero)

        # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)

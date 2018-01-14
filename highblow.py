from collections import Counter
import sys

def birthdayCakeCandles(n, ar):
        ar.sort()
        maxnum = ar[n-1]
        dic = Counter(ar)
        return dic[ar[n-1]]
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

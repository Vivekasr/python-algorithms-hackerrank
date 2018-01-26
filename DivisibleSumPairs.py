import sys

def divisibleSumPairs(n, k, ar):
        lst = []
        for i in range(n):
                for j in range(n):
                        if i != j:
                                asum = ar[i]+ar[j]
                                if asum%k == 0 :
                                        lst.append(asum)
        return int(len(lst)/2)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)

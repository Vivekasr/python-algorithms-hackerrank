import sys

def solve(n, s, d, m):
        lst = []
        if n == 1:
                if m == 1:
                        if s[0] == d:
                                return 1
                        else:
                                return 0
                else:
                        return 0
        else:
                for i in range(0,n-(m-1)):
                        num = s[i:i+m]
                        numsum = sum(num)
                        if numsum == d:
                                lst.append(numsum)
                return len(lst)                

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

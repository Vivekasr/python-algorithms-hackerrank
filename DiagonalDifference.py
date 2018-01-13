import sys

def diagonalDifference(a):
        lst1 = []
        lst2 = []
        for i in range(n):
                c = a[i][i]
                lst1.append(c)
                d = a[i][n-1-i]
                lst2.append(d)
                csum = sum(lst1)
                dsum = sum(lst2)
        e = abs(csum-dsum)
        
        return e
    # Complete this function


n = int(input().strip())
a = []
for a_i in range(n):
                a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
                a.append(a_t)
                
result = diagonalDifference(a)
print(result)

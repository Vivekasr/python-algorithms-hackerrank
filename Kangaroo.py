import sys

def kangaroo(x1, v1, x2, v2):
        lst1 = []
        lst2 = []
        for i in range(10000):
                        xa = x1 + i*v1
                        xb = x2 + i*v2
                        lst1.append(xa)
                        lst2.append(xb)
        alst = []
        blst = []
        for x in lst1:
                if x in lst2:
                        a = lst1.index(x)
                        b = lst2.index(x)
                        alst.append(a)
                        blst.append(b)
        reslst = []
        for i in range(len(alst)):
                if alst[i]!=blst[i]:
                        reslst.append(i)
        if len(reslst)==len(alst):
                return "NO"
        else:
                return "YES"
                
        # Complete this function

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

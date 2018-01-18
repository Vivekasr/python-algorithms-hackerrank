import sys

def appleAndOrange(s, t, a, b, apple, orange):
        lstapple = []
        lstorange = []
        lstapphome = []
        lstorhome = []
        for Na in apple:
                app = a + Na
                lstapple.append(app)
        for No in orange:
                oran = b+No
                lstorange.append(oran)
        for intapp in lstapple:
                if s<=intapp<=t:
                        lstapphome.append(intapp)
        for intor in lstorange:
                if s<=intor<=t:        
                        lstorhome.append(intor)
        return len(lstapphome),len(lstorhome)                
        
    # Complete this function

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))

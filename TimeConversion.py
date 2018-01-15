import sys

def timeConversion(s):
        lst = []
        for timestr in s:
                lst.append(timestr)        
        if (s[8]+s[9]) == ('PM'):
                if 0<int(lst[0]+lst[1])<12:
                        newtimehour=int(lst[0]+lst[1])+12
                        newtime = str(newtimehour) + s[2] + s[3] + s[4] + s[5] + s[6] + s[7]
                if int(lst[0]+lst[1])>12:
                        pass
                if int(lst[0]+lst[1]) == 12:
                        newtime = s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7]
        if (s[8]+s[9]) == ('AM'):
                if int(lst[0]+lst[1]) == 12:
                        newtime = ('0') + ('0') + s[2] + s[3] + s[4] + s[5] + s[6] + s[7]
                else:
                        newtimehour = lst[0]+lst[1]
                        newtime = str(newtimehour) + s[2] + s[3] + s[4] + s[5] + s[6] + s[7]

        return newtime
        
    # Complete this function

s = input().strip()
result = timeConversion(s)
print(result)

import sys

def solve(grades):
        for n,grade in enumerate(grades):
                if grade>=38:
                        if ((grade+1)%5)==0:
                                grades[n]=grades[n]+1
                        elif ((grade+2)%5)==0:
                                grades[n]=grades[n]+2 
                else:
                        grades[n]=grades[n]
        return grades               
        # Complete this function

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))

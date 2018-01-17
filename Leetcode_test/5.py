
import sys

def solve(grades):
    # Complete this function
    line = 38
    #the students who under 38
    final_grades = []

    for i in range(len(grades)):

        if grades[i] < 38:
            final_grades.append(grades[i])

        else:
            mod = grades[i] % 5
            if mod >= 3:
              diff = 5 - mod
              final = grades[i] + diff
              final_grades.append(final)
            else :
              final = grades[i]
              final_grades.append(final)

    return final_grades



n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


'''
mod = grades % 5
diff = 5 - mod
final_grades = grades + final_grades

'''
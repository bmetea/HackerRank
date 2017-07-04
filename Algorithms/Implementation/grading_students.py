#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    new_grades = []
    for grade in grades:
        # print(grade%5)
        if (grade>37 and grade%5>2):
            # print((grade//5*5)+5)
            new_grades.append((grade//5*5) + 5)
        else:
            new_grades.append(grade)
    return new_grades


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))



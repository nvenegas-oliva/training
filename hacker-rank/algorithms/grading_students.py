import sys

def next_mult(num, mult):
    num = num + 1
    while num % mult != 0:
        num = num + 1
    return num

def solve(grades):
    result = []
    for g in grades:
        if g >= 38 and next_mult(g, 5) - g < 3:
            result.append(next_mult(g, 5))
        else:
            result.append(g)
    return result
    # return map(lambda x: 5*(1 + x//5) if (x > 37 and ((x%5) > 2)) else x, grades)

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))

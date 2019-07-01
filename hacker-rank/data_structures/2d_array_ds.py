#!/bin/python3

import sys
matrix = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   matrix.append(arr_t)

results = [] 
for i in range(len(matrix) - 2):
    for j in range(len(matrix) - 2):
        hourglass = [row[j:j+3] for row in matrix[i:i+3]]
        hourglass[1][0] = hourglass[1][2] = 0
        results.append(sum(map(sum, hourglass))) 
print(max(results))
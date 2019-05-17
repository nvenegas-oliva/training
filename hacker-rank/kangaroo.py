#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.


def kangaroo(x1, v1, x2, v2):
    if x1 + v1 < x2 and v2 > v1:
        return "NO"
    else:
        for t in zip(range(x1, 100000001, v1), range(x2, 100000001, v2)):
            if t[0] == t[1]:
                return "YES"
        return "NO"


def kangaroo(x1, v1, x2, v2):
    return 'YES' if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0 else 'NO'


kangaroo(0, 2, 5, 3)
kangaroo(0, 3, 4, 2)
kangaroo(4602, 8519, 7585, 8362)
(5 - 2) % (3 - 2)
(4 - 0) % (2 - 3)

4 % -2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

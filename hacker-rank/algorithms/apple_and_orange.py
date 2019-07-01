#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """"
    apples_in_range = oranges_in_range = 0
    house_range = range(s, t+1)
    for d in apples:
        if a + d in house_range:
            apples_in_range += 1

    for d in oranges:
        if b + d in house_range:
            oranges_in_range += 1

    print(apples_in_range, oranges_in_range, sep='\n')
    """
    house_range = range(s, t+1)
    print(sum([1 for d in apples if a+d in house_range]))
    print(sum([1 for d in oranges if b+d in house_range]))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
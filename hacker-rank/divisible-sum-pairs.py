#!/bin/python3

import os
from itertools import product

# Complete the divisibleSumPairs function below.


def divisibleSumPairs(n, k, ar):
    return sum(1 for i in range(n) for j in range(n) if i < j and (ar[i]+ar[j]) % k == 0)


def divisibleSumPairs(n, k, ar):
    # ar = [1, 2, 3, 4, 5, 6]
    # k = 5
    combs = [product([ar[i]], ar[i+1:]) for i in range(len(ar)-1)]
    combs = [item for sublist in combs for item in sublist]
    return len(list(filter(lambda a: a % k == 0, [t[0] + t[1] for t in combs])))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

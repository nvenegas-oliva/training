#!/bin/python3

import sys

def toys(w):
    w.sort()
    conteiners = 0
    r = range(0)
    for i in range(len(w)):
        if w[i] not in r:
            r = range(w[i], w[i] + 5)
            conteiners += 1
    return conteiners


if __name__ == "__main__":
    n = int(input().strip())
    w = list(map(int, input().strip().split(' ')))
    result = toys(w)
    print(result)
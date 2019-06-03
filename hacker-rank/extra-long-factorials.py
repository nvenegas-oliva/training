#!/bin/python3

from math import factorial


def extraLongFactorials(n):
    return factorial(n)


if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))

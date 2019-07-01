#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    s_arr = sorted(arr)
    return min([abs(a - b) for a, b in zip(s_arr, s_arr[1:])])


if __name__ == "__main__":
    path = 'input.txt'
    # n = int(input().strip())
    # arr = list(map(int, input().strip().split(' ')))
    r = open(path,'r').read().split()
    arr = list(map(int, r[1:]))
    result = minimumAbsoluteDifference(1, arr)
    print(result)
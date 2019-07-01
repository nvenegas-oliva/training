#!/bin/python3

import sys

def maximumToys(prices, k):
    s_prices = sorted(prices)
    i = 0
    while k >= 0:
        if k - s_prices[i] < 0:
            return i
        k = k - s_prices[i]
        i = i + 1


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maximumToys(prices, k)
    print(result)

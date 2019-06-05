import os
from itertools import combinations
from collections import Counter
# It's not 2+1, it's(k//2)+1.
# Consider k = 3. You want to add max(counts[1], counts[2]) to count. Since 3//2 = 1, without + 1 you would have range(1, 1), which is [].


def nonDivisibleSubset(k, S):
    counts = [0] * k
    for n in S:
        counts[n % k] += 1

    help(min)
    count = min(counts[0], 1)
    for i in range(1, k//2+1):
        if i != k - i:
            count += max(counts[i], counts[k-i])
    if k % 2 == 0:
        count += 1
    return count


def nonDivisibleSubset(k, s):
    result = 0
    s = Counter(map(lambda x: x % k, s))
    for i in range(1, k // 2 + 1):
        j = k - i
        if i == j and s[i] > 0:
            result += 1
        elif s[i] > s[j]:
            result += s[i]
        else:
            result += s[j]
    if s[0] > 0:
        result += 1
    return result


def nonDivisibleSubset(k, S):
    # S = [1, 7, 2, 4]
    # S = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
    # k = 3
    # k = 7
    # k = 50
    # tc = open("hacker-rank/non-divisible-input15.txt").readlines()
    # S = list(map(int, tc[1].split()))

    combs = []
    for i in range(2, len(S)):
        combs += list(combinations(S, i))

    result = []

    for c in combs:
        f = list(map(lambda a: True if sum(a) % k != 0 else False, combinations(c, 2)))
        if all(f):
            result.append(len(c))
        # print("%s: %s " % (c, f))
    return max(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    S = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, S)
    fptr.write(str(result) + '\n')
    fptr.close()


from itertools import product


def maximize_it(N, M):
    return max(sum(i**2 for i in c) % M for c in product(*N))


if __name__ == '__main__':
    K, M = list(map(int, input().split()))
    N = []
    for i in range(K):
        N.append(list(map(int, input().split()))[1:])

    print(maximize_it(N, M))

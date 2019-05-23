
def piling_up(side_lenghts):
    # side_lenghts = [1, 2, 3, 4, 5, 6]
    # side_lenghts = [4, 3, 2, 1, 3, 4]
    last_pop = 999999999999
    while side_lenghts:
        if max(side_lenghts[0], side_lenghts[-1]) <= last_pop:
            if side_lenghts[0] >= side_lenghts[-1]:
                last_pop = side_lenghts.pop(0)
            else:
                last_pop = side_lenghts.pop(-1)
        else:
            return "No"
    return "Yes"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        side_lenghts = list(map(int, input().split()))
        # side_lenghts = [4, 3, 2, 1, 3, 4]
        # side_lenghts = [1, 3, 2]
        print(piling_up(side_lenghts))


def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


def minimumBribes(q):
    bribes = 0
    original = list(range(1, len(q) + 1))
    for i in range(len(q)):
        if original[i] != q[i]:
            # print("original[%d] = %d, q[%d] = %d" % (i, original[i], i, q[i]))
            # Distance to original position
            distance = q[i] - (i + 1)
            if distance > 2:
                print("Too chaotic")
                return
            else:
                for j in range(i + distance, i, -1):
                    # print("original[%d] = %d" % (j, original[j]))
                    # print("ant = ", original)
                    original[j], original[j - 1] = original[j - 1], original[j]
                    bribes += 1
                    # print("des = ", original)
    print(bribes)


def minimumBribes(q):
    bribes = 0
    for i in range(len(q), -1, -1):
        distance = q[i] - (i + 1)
        if distance > 2:
            print("Too chaotic")
            return
        else:


q = [1, 2, 5, 3, 7, 8, 6, 4]
q = [2, 5, 1, 3, 4]
q = [2, 1, 5, 3, 4]

file_name = "hacker-rank/new_year_chaos-test_case_1.dat"
with open(file_name) as f:
    content = f.read().splitlines()
q = list(map(int, content[2].split()))


minimumBribes(q)


for i in range(len(q)-1, -1, -1):
    print(i, q[i])


def rotLeft(a, d):
    return a[d:] + a[:d]


a = [1, 2, 3, 4, 5]
d = 4
rotLeft(a, d)

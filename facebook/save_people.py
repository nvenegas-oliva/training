

def savePeople(people, limit):
    boats = 0
    people.sort()

    i = 0  # first
    k = 0  # last

    while i + k < len(people):
        if people[i] + people[-k - 1] == limit:
            i += 1
            k += 1
            boats += 1
            continue
        elif people[i] + people[-k - 1] > limit:
            k += 1
            boats += 1
            continue
        else:
            i += 1
            k += 1

    return boats


people = [3, 2, 2, 1]
limit = 3

people = [2, 1]
limit = 3

people = [1, 2, 3, 3]
limit = 3
print(savePeople(people, limit))  # 3

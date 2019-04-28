import re


def makeAnagram(a, b):
    in_common = "".join(l for l in set(a) & set(b))
    a_dict = {}
    b_dict = {}
    remove = len(a) - len("".join(l for l in a if l in in_common)) + \
        len(b) - len("".join(l for l in b if l in in_common))
    for l in "".join(l for l in a if l in in_common):
        if l not in a_dict:
            a_dict[l] = 1
        else:
            a_dict[l] += 1

    for l in "".join(l for l in b if l in in_common):
        if l not in b_dict:
            b_dict[l] = 1
        else:
            b_dict[l] += 1

    if len(a_dict) > len(b_dict):
        for l in a_dict:

            if a_dict[l] != b_dict[l]:
                remove += max(a_dict[l], b_dict[l]) - min(a_dict[l], b_dict[l])
    else:
        for l in b_dict:

            if a_dict[l] != b_dict[l]:
                remove += max(a_dict[l], b_dict[l]) - min(a_dict[l], b_dict[l])

    return remove


def number_needed(a, b):
    ab_intersection = set(a).intersection(b)
    anagram = sum(min(a.count(char), b.count(char)) for char in ab_intersection)
    return (len(a)+len(b)-2*anagram)


a = "cde"
b = "abc"

a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
makeAnagram(a, b)
number_needed(a, b)


s1 = "hello"
s2 = "hola"
s3 = "re"

s1 = "wouldyoulikefries"
s2 = "abcabcabcabcabcabc"

s1 = "hackerrankcommunity"
s2 = "cdecdecdecde"
set(s1)
set(s2)

set(s1).isdisjoint(set(s3))
set(s3).isdisjoint(set(s1))
set(s2).isdisjoint(set(s3))
set(s3).isdisjoint(set(s2))
set(s1) & set(s2)
set(s2) & set(s3)


def twoStrings(s1, s2):
    if set(s1).isdisjoint(set(s2)):
        return "NO"
    else:
        return "YES"


def twoStrings(s1, s2):
    return "NO" if set(s1).isdisjoint(set(s2)) else "YES"


def twoStrings(s1, s2):
    return 'YES' if set(s1) & set(s2) != set() else 'NO'


twoStrings(s1, s2)
twoStrings(s2, s3)

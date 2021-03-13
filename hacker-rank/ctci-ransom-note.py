#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine = Counter(magazine)
    note = Counter(note)
    # give me one grand today night
    # {give: 1, me: 1, one:1, grand:1, today: 1, night: 1}
    # give one grand today
    # {give: 1, me: 1, grand: 1, today: 1}
    for w in note:
        if w not in magazine or note[w] > magazine[w]:
            print('No')
            return
    print('Yes')
    
    
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)


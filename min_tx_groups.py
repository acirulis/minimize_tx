import itertools
from collections import Counter
import random

class Found(Exception): pass

data = [7, -4, 21, -56, 32]
# data = [-2, 2, 5, -5, -3, 1, 2]
random.shuffle(data)


def substract_list(a, b):
    return list((Counter(a) - Counter(b)).elements())


def find_groups(data):
    if len(data) == 0:
        return []

    f = []
    try:
        for r in range(2, len(data)+1):
            perm = itertools.combinations(data, r)
            for i in list(perm):
                if sum(i) == 0:  # group found
                    raise Found
    except Found:
            f.append(i)
            rest = find_groups(substract_list(data, i))
            for el in rest:
                f.append(el)
    return f



print('-- start actual search --')
if sum(data) == 0:
    gr = find_groups(data)
    print('-- found -- ')
    print(gr)
else:
    print('incorrect data')


import itertools
from collections import Counter
import random


class Found(Exception): pass


# data = [7, -4, 21, -56, 32]
# data = [-6, -5, -5, 3, 3, 10, 8, -8]
data = [1, 1, 1, 1, 1, 1, 1, 7, -2, -2, -2, -2, -2, -2, -2]
random.shuffle(data)


def substract_list(a, b):
    return list((Counter(a) - Counter(b)).elements())


def find_groups(data):
    if len(data) == 0:
        return []

    f = []
    try:
        for r in range(2, len(data) + 1):
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


def transactions_per_group(data):
    data.sort()
    print('Starting: ', data)
    while len(data) > 0:
        _min = data[0]
        _max = data[-1]
        if _min + _max == 0:
            print('transaction found: {} settles with {}'.format(_min, _max))
            data.pop(0)
            data.pop(-1)
        else:
            smallest = min(abs(_min), abs(_max))
            if abs(_min) == smallest:
                print('transaction found {} settles with {}, left {}'.format(_min, _max, _max + _min))
                data[-1] = _max + _min
                data.pop(0)

            else:
                print('transaction found {} settles with {}, left {}'.format(_min, _max, _max + _min))
                data[0] = _max + _min
                data.pop(-1)
        print('Remaining: ', data)


print('-- start actual search --')
if sum(data) == 0:
    gr = find_groups(data)
    print('-- found -- ')
    for group in gr:
        transactions_per_group(list(group))
else:
    print('incorrect data')

# print('-- transactions per group --')
# tx = transactions_per_group([10, -2, -8, 3, -3])

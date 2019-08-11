import itertools
from collections import Counter
import random
from min_tx_class import TxList


class Found(Exception): pass


# data = {'p1': 7, 'p2': -4, 'p3': 21, 'p4': -56, 'p5': 32}
# data = {'p1': -6, 'p2': -5, 'p3': -5, 'p4': 3, 'p5': 3, 'p6': 10, 'p7': 8, 'p8': -8}
# data = {'p1': 10, 'p2': 3, 'p3': 3, 'p4': -6, 'p5': -5, 'p6': -5}
# data = {'p1': -1, 'p2': 5, 'p3': -4, 'p4': 8, 'p5': -8}
# data = {'Andis': -4, 'Janis': 0, 'Peteris': 4}
data = {'Andis': 0, 'Janis': -4, 'Peteris': 4}

def find_groups(data):
    if len(data) == 0:
        return []
    f = []
    try:
        for r in range(2, len(data) + 1):
            perm = itertools.combinations(data, r)
            for i in list(perm):
                i = sum(i)  # combine all tuple elements into single TxList
                if i.sum() == 0:  # group found
                    raise Found
    except Found:
        f.append(i)
        rest = find_groups(data - i)
        for el in rest:
            f.append(el)
    return f


def transactions_per_group(data):
    # print('Starting: ', data)
    tx_list = []
    while len(data) > 0:
        _min = data.min()  # get keys for min & max elements
        _max = data.max()
        if data[_min] + data[_max] == 0:
            # print('Transaction found: {} settles even with {} for {}'.format(_min, _max, data[_max]))
            tx_list.append('Transaction found: {} settles even with {} for {}'.format(_min, _max, data[_max]))
            data.pop(_min)
            data.pop(_max)
        else:
            smallest = min(abs(data[_min]), abs(data[_max]))
            # print('Transaction found {} ({}) settles with {} ({}), left {}'.format(_min, data[_min], _max, data[_max],
            #                                                                        data[_max] + data[_min]))
            tx_list.append(
                'Transaction found {} ({}) settles with {} ({}), left {}'.format(_min, data[_min], _max, data[_max],
                                                                                 data[_max] + data[_min]))
            if abs(data[_min]) == smallest:
                data[_max] = data[_max] + data[_min]
                data.pop(_min)
            else:
                data[_min] = data[_max] + data[_min]
                data.pop(_max)
        # print('Remaining: ', data)
    return tx_list


print('= MINIMIZE TRANSACTIONS =')
T = TxList(data)
print('Data: ', T)

if T.sum() == 0:
    gr = find_groups(T)
    print('Unique groups found: ', gr)
    tx_list = []
    for group in gr:
        tx_list += transactions_per_group(group)
    # display results
    print('= RESULTS =')
    for ix, tx in enumerate(tx_list):
        print('#{} {} '.format(ix + 1, tx))
else:
    print('Incorrect data, must sum up to 0')

# print('-- transactions per group test--')
# tx = transactions_per_group(TxList({'p1': 4, 'p2': -2, 'p3': -2}))

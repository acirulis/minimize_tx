import json
import itertools


class InvalidTxList(Exception):
    """Elements of Tx list should always sum to zero"""
    pass


class TxList:
    """Class for dealing with list of transactions to settle among group of people"""

    def __init__(self, data):
        self.data = data

    def sum(self):
        return sum(self.data.values())

    def min(self):
        """Find a key for minimal value"""
        key = min(self.data, key=self.data.get)
        return key

    def max(self):
        """Find a key for maximal value"""
        key = max(self.data, key=self.data.get)
        return key

    def pop(self, key):
        self.data.pop(key)

    def validate(self):
        if self.sum() != 0:
            raise InvalidTxList('Sum of all participants must be 0')

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __add__(self, counter):
        return TxList({**self.data, **counter.data})

    def __radd__(self, counter):
        if counter == 0:
            return self
        else:
            return TxList({**self.data, **counter.data})

    def __sub__(self, counter):
        # all(map(a.pop, b)) # some concept to refactor for speed?
        for key in counter.data.keys():
            if key in self.data:
                del (self.data[key])
        return self

    def __iter__(self):
        return iter([TxList({k: v}) for k, v in self.data.items()])

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return 'TxList: ' + json.dumps(self.data)


if __name__ == '__main__':
    data = {'p1': -1, 'p2': 5, 'p3': -4, 'p4': 8, 'p5': -8}
    T = TxList(data)
    print(T.sum())
    perm = itertools.combinations(T, 2)
    for c in perm:
        r = sum(c)
        print(r)

import json
import itertools


class InvalidTxList(Exception):
    pass


class TxList:
    """Class for dealing with list of transactions to settle among group of people"""

    def __init__(self, data):
        self.data = data

    def __add__(self, counter):
        return TxList({**self.data, **counter.data})

    def __radd__(self, counter):
        if counter == 0:
            return self
        else:
            return TxList({**self.data, **counter.data})

    def __sub__(self, counter):
        for key in counter.data.keys():
            if key in self.data:
                del (self.data[key])
        return self

    def sum(self):
        return sum(self.data.values())

    def __iter__(self):
        return iter([TxList({k: v}) for k, v in data.items()])

    def validate(self):
        if self.sum() != 0:
            raise InvalidTxList('Sum of all participants must be 0')

    def __repr__(self):
        return 'C: ' + json.dumps(self.data)


if __name__ == '__main__':
    data = {'p1': -1, 'p2': 5, 'p3': -4, 'p4': 8, 'p5': -8}

    T = TxList(data)
    for c in itertools.combinations(T, 3):
        r = sum(c)
        print(r)

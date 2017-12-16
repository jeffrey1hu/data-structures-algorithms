# python3
import sys
from collections import defaultdict

class BwtDict:
    def __init__(self, bwt):
        self.bwt = bwt

        int_count = defaultdict(int)
        bwt_index = dict()
        inv_bwt_index = []

        for idx, ele in enumerate(self.bwt):
            int_count[ele] += 1
            char_order = str(ele) + '_' + str(int_count[ele])
            bwt_index[char_order] = idx
            inv_bwt_index.append(char_order)

        self.bwt_index = bwt_index
        self.inv_bwt_index = inv_bwt_index

def InverseBWT(bwt):
    # write your code here
    asc_bwt = list(bwt)
    asc_bwt.sort()
    assert asc_bwt[0] == '$'

    bwt = BwtDict(bwt)
    asc_bwt = BwtDict(asc_bwt)

    counter = 0
    result = []
    lookup_char = asc_bwt.bwt[0]
    result.append(lookup_char)
    lookup_char_order = asc_bwt.inv_bwt_index[0]
    lookup_char_idx = 0
    lookup_bwts = [asc_bwt, bwt]

    while len(result) < len(bwt.bwt):

        counter += 1
        lookup_bwt = lookup_bwts[counter % 2]
        # processing btw
        lookup_char = lookup_bwt.bwt[lookup_char_idx]
        # print("lookup_char_idx in bwt", lookup_char_idx)
        # print("lookup_char in bwt", lookup_char)
        result.append(lookup_char)
        lookup_char_order = lookup_bwt.inv_bwt_index[lookup_char_idx]
        # lookup_char_idx = lookup_bwt.bwt_index[lookup_char_order]

        # processing asc_btw
        counter += 1
        lookup_bwt = lookup_bwts[counter % 2]

        lookup_char_idx = lookup_bwt.bwt_index[lookup_char_order]

    result.reverse()
    return ''.join(result)


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
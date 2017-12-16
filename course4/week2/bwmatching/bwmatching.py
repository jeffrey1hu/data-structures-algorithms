# python3
import sys
from collections import defaultdict
import copy

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

        self.char_count = int_count
        self.bwt_index = bwt_index
        self.inv_bwt_index = inv_bwt_index


def PreprocessBWT(bwt):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position
        of this character in the sorted array of
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
    """
    asc_bwt = list(bwt)
    asc_bwt.sort()

    starts = dict()
    for idx, char in enumerate(asc_bwt):
      if char in starts:
          continue
      starts[char] = idx

    occ_count_before = defaultdict(dict)
    for idx in range(1, len(bwt)+1):
        occ_count_before[idx] = copy.copy(occ_count_before[idx - 1])
        char = bwt[idx - 1]
        occ_count_before[idx].setdefault(char, 0)
        occ_count_before[idx][char] += 1

    return starts, occ_count_before


def CountOccurrences(pattern, bwt, _starts, _occ_counts_before):
    top = 0
    bottom = len(bwt) - 1
    # print("top {} bottom {}".format(top, bottom))
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            if symbol not in _starts:
                return 0
            pattern = pattern[:-1]
            top = _starts[symbol] + _occ_counts_before[top].get(symbol, 0)
            bottom = _starts[symbol] + _occ_counts_before[bottom+1].get(symbol, 0) - 1
            # print("top {} bottom {}".format(top, bottom))
        else:
            return bottom - top + 1
    return 0


# def CountOccurrences(pattern, bwt, starts, occ_counts_before):
#   """
#   Compute the number of occurrences of string pattern in the text
#   given only Burrows-Wheeler Transform bwt of the text and additional
#   information we get from the preprocessing stage - starts and occ_counts_before.
#   """
#   # Implement this function yourself
#   return 0
     


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).
    starts, occ_counts_before = PreprocessBWT(bwt)
    # print("bwt", bwt)
    # print("starts ", starts)
    # print("occ_counts_before", occ_counts_before)
    # start_column_bwt, end_column_bwt = PreprocessBWT(bwt)


    occurrence_counts = []
    for pattern in patterns:
        # print("pattern ", pattern)
        occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))

# python3
import sys
import copy
from collections import defaultdict

char_mapping = {'A':1, 'C': 2, 'G': 3, 'T': 4, '$': 0}


def bwt_occurrence(pattern, bwt, _starts, _occ_counts_before, occs, suffix_array):
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
            # print("bottom, top {} {}".format(bottom, top))
            for i in range(top, bottom+1):
                occs.add(suffix_array[i])
            return 0
    return 0

def sort_doublely(s, l, order, _class):
    """
    stable sort
    :param s:
    :param l:
    :param order:
    :param _class:
    :return:
    """
    count = [0] * len(s)
    new_order = [0] * len(s)
    for i in range(len(s)):
        count[_class[i]] += 1
    for j in range(1, len(s)):
        count[j] += count[j-1]
    for i in range(len(s)-1, -1, -1):
        start = (order[i] - l + len(s)) % len(s)
        cl = _class[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order

def update_classes(new_order, _class, l):
    n = len(new_order)
    new_class = [None] * n
    new_class[new_order[0]] = 0
    for i in range(1, len(new_order)):
        cur = new_order[i]
        prev = new_order[i-1]
        mid = (cur + l) % n
        mid_prev = (prev + l) % n
        if _class[cur] != _class[prev] or _class[mid] != _class[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]
    return new_class

def sort_char(s):
    """
    count sort
    :param s:
    :return:
    """
    order = [None] * len(s)
    count = [0] * len(char_mapping)
    for i in range(len(s)):
        count[char_mapping[s[i]]] += 1
    for j in range(1, len(char_mapping)):
        count[j] = count[j] + count[j-1]
    for i in range(len(s)-1, -1, -1):
        char = s[i]
        count[char_mapping[char]] -= 1
        order[count[char_mapping[char]]] = i
    return order

def compute_char_classes(s, order):
    _class = [None] * len(s)
    _class[order[0]] = 0
    for i in range(1, len(s)):
        if s[order[i]] != s[order[i-1]]:
            _class[order[i]] = _class[order[i-1]]+1
        else:
            _class[order[i]] = _class[order[i-1]]
    return _class

def build_suffix_array(s):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = sort_char(s)
  # print("ans of q1 {}".format(order))
  _class = compute_char_classes(s, order)
  # print("ans of q2 {}".format(_class))
  l = 1
  while l < len(s):
      # print("l {}".format(l))
      # print("order {}".format(order))
      order = sort_doublely(s, l, order, _class)
      # print("ans of q4 {}".format(order))
      # print("_class {}".format(_class))
      _class = update_classes(order, _class, l)
      # print("ans of q5 {}".format(_class))
      l *= 2
  # Implement this function yourself
  return order

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



def find_occurrences(text, patterns):
    text = text + '$'
    suffix_array = build_suffix_array(text)

    bwt = [text[pos_idx-1] for pos_idx in suffix_array]

    starts, occ_counts_before = PreprocessBWT(bwt)

    occs = set()

    for pattern in patterns:
        # print("pattern ", pattern)
        bwt_occurrence(pattern, bwt, starts, occ_counts_before, occs, suffix_array)

    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))
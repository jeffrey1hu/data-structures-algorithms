# python3
import sys

char_mapping = {'A':1, 'C': 2, 'G': 3, 'T': 4, '$': 0}


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


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))

# python3
import sys


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    result = []
    # Implement this function yourself
    for i in range(len(text)):
        suffix = text[i:]
        result.append((i, suffix))
    result.sort(key=lambda x: x[1])
    return map(lambda x: x[0], result)


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))

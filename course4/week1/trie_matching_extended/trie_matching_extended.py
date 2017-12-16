# python3
import sys
from collections import defaultdict

class Node:
    def __init__ (self, idx):
        self.idx = idx
        self.is_pattern_end = False

def build_trie(patterns):
    node_idx = 0
    tree = defaultdict(dict)
    # write your code here
    for pattern in patterns:
        current_node = 0
        for idx, current_char in enumerate(pattern):
            if current_char in tree[current_node]:
                if idx == len(pattern) - 1:
                    tree[current_node][current_char].is_pattern_end = True
                current_node = tree[current_node][current_char].idx
            else:
                node_idx += 1
                tree[current_node][current_char] = Node(node_idx)
                if idx == len(pattern) - 1:
                    tree[current_node][current_char].is_pattern_end = True
                current_node = node_idx

    return tree


def solve (text, n, patterns):
    result = set()
    
    prie_tree = build_trie(patterns)
    # print(prie_tree)
    for i in range(len(text)):
        current_node = 0
        j = i
        while True:
            if text[j] in prie_tree[current_node]:
                if prie_tree[current_node][text[j]].is_pattern_end:
                    result.add(i)
                current_node = prie_tree[current_node][text[j]].idx
                j += 1
                if j >= len(text):
                    break
            else:
                break
    return sorted(result)

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')

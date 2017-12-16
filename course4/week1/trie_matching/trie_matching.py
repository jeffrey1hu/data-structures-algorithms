# python3
import sys
from collections import defaultdict

def build_trie(patterns):
    node_idx = 0
    tree = defaultdict(dict)
    # write your code here
    for pattern in patterns:
        current_node = 0
        for idx, current_char in enumerate(pattern):
            if current_char in tree[current_node]:
                current_node = tree[current_node][current_char]
            else:
                node_idx += 1
                tree[current_node][current_char] = node_idx
                current_node = node_idx
    return tree

# class Node:
# 	def __init__ (self):
# 		self.next = [NA] * 4

def solve (text, n, patterns):
    result = []
    prie_tree = build_trie(patterns)

    for i in range(len(text)):
        current_node = 0
        j = i
        while True:
            if text[j] in prie_tree[current_node]:
                current_node = prie_tree[current_node][text[j]]
                j += 1
                if current_node > 0 and (not prie_tree[current_node]):
                    result.append(i)
                    break
                if j >= len(text):
                    break
            else:
                break
    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')

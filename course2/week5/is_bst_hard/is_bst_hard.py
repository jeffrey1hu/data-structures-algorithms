#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Tree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def IsBinarySearchTree(tree):
    if len(tree) == 0:
        return True
  # Implement correct algorithm here
    key = [0 for i in range(len(tree))]
    left = [0 for i in range(len(tree))]
    right = [0 for i in range(len(tree))]
    for i, (a, b, c) in enumerate(tree):
        key[i] = a
        left[i] = b
        right[i] = c

    def inorder_traversal(_tree, _left, result, idx=0):
        if idx == -1:
            return
        inorder_traversal(_tree, _left, result, _tree.left[idx])
        result.append(_tree.key[idx])
        if _tree.left[idx] != -1:
            _left.append(_tree.key[_tree.left[idx]])
        else:
            _left.append(-float('inf'))
        # print(_tree.key[idx])
        inorder_traversal(_tree, _left, result, _tree.right[idx])

    result = []
    left_child_key = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    tree = Tree(key, left, right)
    inorder_traversal(tree, left_child_key, result)

    for i in range(1, len(result)):
        if result[i] < result[i-1] or left_child_key[i] == result[i]:
            return False

    return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# class TreeHeight:
#         def read(self):
#                 self.n = int(sys.stdin.readline())
#                 self.parent = list(map(int, sys.stdin.readline().split()))
#
#         def compute_height(self):
#                 # Replace this code with a faster implementation
#                 maxHeight = 0
#                 for vertex in range(self.n):
#                         height = 0
#                         i = vertex
#                         while i != -1:
#                                 height += 1
#                                 i = self.parent[i]
#                         maxHeight = max(maxHeight, height);
#                 return maxHeight;
class Tree:
    def __init__(self, _arr):
        self.root = None
        self.nodes = [Node(index, parent_index) for index, parent_index in enumerate(_arr)]

    def build(self):
        for node in self.nodes:
            parent = node.parent_idx
            if parent == -1:
                self.root = node
                continue
            self.nodes[parent].add_children(node)


class Node:
    def __init__(self, indx, parent_idx):
        self.indx = indx
        self.parent_idx = parent_idx
        self.children = []

    def add_children(self, child_node):
        self.children.append(child_node)

    def height(self):
        if not self.children:
            return 1
        return 1 + max(map(lambda child: child.height(), self.children))


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        tree = Tree(_arr=self.parent)
        tree.build()

        return tree.root.height()
        #
        # maxHeight = 0
        # for vertex in range(self.n):
        #     height = 0
        #     i = vertex
        #     while i != -1:
        #         height += 1
        #         i = self.parent[i]
        #         maxHeight = max(maxHeight, height);
        #     return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()

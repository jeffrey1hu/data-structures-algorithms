# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    def inorder_traversal(_tree, result, idx=0):
        if idx == -1:
            return
        inorder_traversal(_tree, result, _tree.left[idx])
        result.append(_tree.key[idx])
        # print(_tree.key[idx])
        inorder_traversal(_tree, result, _tree.right[idx])

    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    inorder_traversal(self, self.result)
                
    return self.result

  def preOrder(self):
    def preorder_traversal(_tree, result, idx=0):
        if idx == -1:
            return
        result.append(_tree.key[idx])
        preorder_traversal(_tree, result, _tree.left[idx])
        # print(_tree.key[idx])
        preorder_traversal(_tree, result, _tree.right[idx])

    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    preorder_traversal(self, self.result)

    return self.result

  def postOrder(self):
    def postorder_traversal(_tree, result, idx=0):
        if idx == -1:
            return
        postorder_traversal(_tree, result, _tree.left[idx])
        # print(_tree.key[idx])
        postorder_traversal(_tree, result, _tree.right[idx])
        result.append(_tree.key[idx])

    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    postorder_traversal(self, self.result)

    return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

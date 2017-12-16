# python3

class Heap:
    def __init__(self, arr):
        self._data = arr
        self.size = len(arr)
        self.swaps = []

    def sift_up(self, i):
        pass

    def sift_down(self, i):
        # i is 1 based idx
        max_idx = i
        left_child = self.left_child(i)
        right_child = self.right_child(i)
        # print("i {}, left {}, right {}".format(max_idx, left_child, right_child))

        if left_child <= self.size and self._data[left_child-1] < self._data[max_idx-1]:
            max_idx = left_child

        if right_child <= self.size and self._data[right_child-1] < self._data[max_idx-1]:
            max_idx = right_child

        if i != max_idx:
            self.swap(i, max_idx)
            self.sift_down(max_idx)

    def swap(self, i, j):
        # print("add swap {}".format((i, j)))
        self.swaps.append((i-1, j-1))
        self._data[i-1], self._data[j-1] = self._data[j-1], self._data[i-1]

    @staticmethod
    def left_child(i):
        return 2 * i

    @staticmethod
    def right_child(i):
        return 2*i + 1

    @staticmethod
    def parent(i):
        return i // 2

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # print("data, ", self._data)
    heap = Heap(self._data)
    size = len(self._data)
    for i in range(size // 2, 0, -1):
        # print("sift down {}".format(i))
        heap.sift_down(i)

    self._swaps = heap.swaps



    # for i in range(len(self._data)):
    #   for j in range(i + 1, len(self._data)):
    #     if self._data[i] > self._data[j]:
    #       self._swaps.append((i, j))
    #       self._data[i], self._data[j] = self._data[j], self._data[i]


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

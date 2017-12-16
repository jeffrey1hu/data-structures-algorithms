#Uses python3

import sys
import numpy as np
import queue


class MinHeap:
    def __init__(self, arr, size):
        self._data = arr
        self.size = size
        for i in range(self.size // 2, 0, -1):
            # print("sift down {}".format(i))
            self.sift_down(i)


    def sift_up(self, i):
        while i > 1 and self._data[self.parent(i) - 1][1] > self._data[i - 1][1]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def sift_down(self, i):
        # i is 1 based idx
        max_idx = i
        left_child = self.left_child(i)
        right_child = self.right_child(i)
        # print("i {}, left {}, right {}".format(max_idx, left_child, right_child))

        if left_child <= self.size and self._data[left_child-1][1] < self._data[max_idx-1][1]:
            max_idx = left_child

        if right_child <= self.size and self._data[right_child-1][1] < self._data[max_idx-1][1]:
            max_idx = right_child

        if i != max_idx:
            self.swap(i, max_idx)
            self.sift_down(max_idx)

    def swap(self, i, j):
        # print("add swap {}".format((i, j)))
        # self.swaps.append((i-1, j-1))
        self._data[i-1], self._data[j-1] = self._data[j-1], self._data[i-1]

    def extract_min(self):
        assert self.size > 0, "the heap is empty"
        result = self._data[0]
        self.size -= 1
        self._data[0] = self._data[self.size]
        self._data[self.size] = result
        self._data.pop()
        self.sift_down(1)
        return result

    def get_min(self):
        return self._data[0]

    def insert(self, ele):
        self.size += 1
        self._data.append(ele)
        self.sift_up(self.size)

    @staticmethod
    def left_child(i):
        return 2 * i

    @staticmethod
    def right_child(i):
        return 2*i + 1

    @staticmethod
    def parent(i):
        return i // 2



def extract_min(H):
    min_indx, min_val = min(H.items(), key=lambda x: x[1])
    H.pop(min_indx)
    return (min_indx, min_val)


def distance(adj, cost, s, t):
    #write your code here
    # print("adj ", adj)
    # print("cost ", cost)
    # print(s)
    # print(t)
    # inf_val = 1e8 + 1
    dist = [np.inf for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]

    dist[s] = 0

    H = MinHeap(arr=list(enumerate(dist)), size=len(dist))

    precessed_node = set()
    while H.size > 0:
        u, val = H.extract_min()
        if u in precessed_node:
            # print("pass {} with val {}".format(u, val))
            continue
        # print("process node {} with val {}".format(u, val))
        precessed_node.add(u)
        for v, _cost in zip(adj[u], cost[u]):
            if dist[v] > dist[u] + _cost:
                # print("relax node {} prev val {}".format(v, dist[v]))
                dist[v] = dist[u] + _cost
                # print("new val is {}".format(dist[v]))
                prev[v] = u
                H.insert((v, dist[v]))
                # print("insert v {} to heap, current_heap is {}".format(v, H._data))
    if np.inf == dist[t]:
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # n vertices, m edges
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    # print("remain_data", data)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))

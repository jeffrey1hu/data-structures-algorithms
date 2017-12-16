#Uses python3

import sys

def explore(adj, x, visited_set):
    if x not in visited_set:
        visited_set.add(x)
    for y in adj[x]:
        if y not in visited_set:
            explore(adj, y, visited_set)


def reach(adj, x, y):
    #write your code here
    # adj [0, 1, 2, 3, 4]
    #     [[neighbors], [], ...]
    visited_nodes = set()
    explore(adj, x, visited_nodes)
    if y in visited_nodes:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))

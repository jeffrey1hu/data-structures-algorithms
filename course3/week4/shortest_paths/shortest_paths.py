#Uses python3

import sys
import queue
import numpy


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # print("init adj", adj)
    #write your code here
    prev = [None] * len(adj)

    distance[s] = 0
    x = []
    for i in range(len(adj)):
        for u, u_edges in enumerate(adj):
            for v, v_cost in zip(u_edges, cost[u]):
                if distance[v] > distance[u] + v_cost:
                    distance[v] = distance[u] + v_cost
                    prev[v] = u
                    if i >= len(adj) -1:
                        x.append(v)
                        # shortest[v] = 0
                        # distance[v] = - numpy.inf

    # print("distance {}".format(distance))
    # print("prev {}".format(prev))
    # print("has negative cycle v {}, prev_v {}".format(v, prev[v]))
    for idx, dist in enumerate(distance):
        if dist < float('inf'):
            reachable[idx] = 1

    added_x = set(x)
    while x:
        ele = x.pop()
        shortest[ele] = 0
        for v in adj[ele]:
            if v not in added_x:
                x.append(v)
            shortest[v] = 0

    # y = x[-1]
    # if is_update:
    #     for _ in range(len(adj)):
    #         shortest[y] = 0
    #         for ele in adj[y]:
    #             shortest[ele] = 0
    #         y = prev[y]
    #     for _x in x:
    #         shortest[_x] = 0
    #         for ele in adj[_x]:
    #             shortest[ele] = 0
    # print("shortest", shortest)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])


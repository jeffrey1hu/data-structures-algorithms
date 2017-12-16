#Uses python3

import sys
import numpy as np
import copy
sys.setrecursionlimit(200000)

def reverse_adj(_adj):
    r_adj = [[] for _ in range(len(_adj))]
    for _idx, edges in enumerate(_adj):
        for _to_contrex in edges:
            r_adj[_to_contrex].append(_idx)
    return r_adj

def dfs(adj, used, order, x):
    # order means poster number
    #write your code here
    used[x] = 1

    for y in adj[x]:
        if used[y] == 0:
            dfs(adj, used, order, y)

    order.append(x)

def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    for x in range(len(adj)):
        if used[x] == 0:
            dfs(adj, used, order, x)
    # poster number is from small to large
    return order

def explore(adj, x, x_reachable_set, visited_contrex):
    for y in adj[x]:
        if y not in x_reachable_set and y not in visited_contrex:
            x_reachable_set.add(y)
            visited_contrex.add(y)
            explore(adj, y, x_reachable_set, visited_contrex)
        else:
            continue

def negative_cycle(adj, cost):
    # r_adj = reverse_adj(adj)
    # # print("adj {}".format(r_adj))
    # order = toposort(r_adj)
    # order.reverse()
    # # print(order)
    # # print("order", order)
    # num = 0
    # visited_contrex = set()
    # sscs = []
    # for idx in order:
    #     if idx in visited_contrex:
    #         # print("skip {}".format(idx))
    #         continue
    #     # print("explore contrex {} visited_contrex {}".format(idx, visited_contrex))
    #     visited_contrex.add(idx)
    #     x_reachable_set = set()
    #     explore(adj, idx, x_reachable_set, visited_contrex)
    #     x_reachable_set.add(idx)
    #     # print("a new ssc {} from sink contrex {}, visited_contrex {}".format(x_reachable_set, idx, visited_contrex))
    #     sscs.append(x_reachable_set)
    #     num += 1

    # for ssc in sscs:
    dist = [np.inf for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    # s = ssc.pop()
    dist[0] = 0
    is_update = False

    num_iter = len(adj)
    while num_iter > 0:
        is_update = False
        for u, u_edges in enumerate(adj):
            for v, v_cost in zip(u_edges, cost[u]):
                if dist[v] > dist[u] + v_cost:
                    dist[v] = dist[u] + v_cost
                    prev[v] = u
                    is_update = True
        if not is_update:
            for i in range(len(adj)):
                if dist[i] == np.inf:
                    dist[i] = 0
                    num_iter = len(adj)
                    break
        num_iter -= 1

    if is_update:
        return 1

    return 0


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
    print(negative_cycle(adj, cost))

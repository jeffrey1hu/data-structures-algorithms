#Uses python3

import sys
from collections import defaultdict
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

def number_of_strongly_connected_components(adj):
    r_adj = reverse_adj(adj)
    # print("adj {}".format(r_adj))
    order = toposort(r_adj)
    order.reverse()
    # print(order)

    num = 0
    visited_contrex = set()
    for idx in order:
        if idx in visited_contrex:
            # print("skip {}".format(idx))
            continue
        # print("explore contrex {} visited_contrex {}".format(idx, visited_contrex))
        visited_contrex.add(idx)
        x_reachable_set = set()
        explore(adj, idx, x_reachable_set, visited_contrex)
        # print("a new ssc {} from sink contrex {}".format(x_reachable_set, idx))
        num += 1
    return num


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    # print("adj_first {}".format(adj))
    print(number_of_strongly_connected_components(adj))



# def explore(adj, x, x_reachable_set):
#     for y in adj[x]:
#         if y not in x_reachable_set:
#             x_reachable_set.add(y)
#             explore(adj, y, x_reachable_set)
#         else:
#             continue
#
#
# def number_of_strongly_connected_components(adj):
#     result = 0
#     #write your code here
#     reachable_sets = [set()] * len(adj)
#     for x in range(len(adj)):
#         reachable_set = set()
#         explore(adj, x, reachable_set)
#         reachable_sets[x] = reachable_set
#
#     sccs = []
#     tracked_vetrex = set()
#     for x, reachable_set_x in enumerate(reachable_sets):
#         if x in tracked_vetrex:
#             continue
#         scc = set()
#         for y in reachable_set_x:
#             if x in reachable_sets[y]:
#                 scc.add(y)
#                 tracked_vetrex.add(y)
#         sccs.append(scc)
#         tracked_vetrex.add(x)
#     return len(sccs)
#

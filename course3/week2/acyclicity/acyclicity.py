#Uses python3

import sys

def explore(adj, x, x_reachable_set):
    for y in adj[x]:
        if y not in x_reachable_set:
            x_reachable_set.add(y)
            explore(adj, y, x_reachable_set)
        else:
            continue


def acyclic(adj):
    for vetrex_id, edges in enumerate(adj):
        reachable_set = set()
        # print("exploring {}".format(vetrex_id))
        explore(adj, vetrex_id, reachable_set)
        if vetrex_id in reachable_set:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

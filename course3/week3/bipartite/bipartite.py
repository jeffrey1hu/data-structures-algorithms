#Uses python3

import sys
import queue


def distance(adj, s, t):
    #write your code here
    dist = [-1 for _ in range(len(adj))]
    dist[s] = 0
    q = []
    q.append(s)
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if dist[v] == -1:
                q.append(v)
                dist[v] = dist[u] + 1
    return dist[t]


def bipartite(adj):
    #write your code here
    s = 0
    dist = [-1 for _ in range(len(adj))]
    dist[s] = 0
    q = []
    q.append(s)
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if dist[v] == -1:
                q.append(v)
                dist[v] = dist[u] + 1
            else:
                if (dist[v] - dist[u]) % 2 == 0:
                    return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))

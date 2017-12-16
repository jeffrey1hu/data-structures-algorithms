#Uses python3

import sys

def explore(adj, x, unvisited_set):
    if x in unvisited_set:
        unvisited_set.remove(x)
    for y in adj[x]:
        if y in unvisited_set:
            explore(adj, y, unvisited_set)


def number_of_components(adj):
    result = 0
    unvisited_set = set(range(len(adj)))
    #write your code here
    while unvisited_set:
        x = unvisited_set.pop()
        explore(adj, x, unvisited_set)
        result += 1

    return result

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
    print(number_of_components(adj))

#Uses python3
import sys
import math



def euc_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def getParent(parent, point_idx):
    # find parent and compress path
    if point_idx != parent[point_idx]:
        parent[point_idx] = getParent(parent, parent[point_idx])
    return parent[point_idx]


def clustering(x, y, k):
    #write your code here
    result = 0.
    #write your code here
    points = list(zip(x, y))
    edge_pairs = []
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                continue
            dist = euc_distance(points[i], points[j])
            edge_pairs.append((i, j, dist))
    edge_pairs.sort(key=lambda x: x[2])
    # print("edge_pairs", edge_pairs)

    parent = list(range(len(x)))
    rank = [1] * n
    # X = set()
    selected_edges = []
    for i, j, dist in edge_pairs:
        i_parent = getParent(parent, i)
        j_parent = getParent(parent, j)
        if i_parent != j_parent:
            if rank[i_parent] > rank[j_parent]:
                parent[j_parent] = i_parent
            else:
                parent[i_parent] = j_parent
                if rank[i_parent] == rank[j_parent]:
                    rank[j_parent] += 1
            selected_edges.append(dist)
            # print("merge {} and {}".format(i, j))
            # print("+", dist)

    return selected_edges[-(k-1)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))

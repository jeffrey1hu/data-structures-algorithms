# Uses python3
import sys
import numpy as np
# def optimal_weight(W, w):
#     # write your code here
#     result = 0
#     for x in w:
#         if result + x <= W:
#             result = result + x
#     return result

def optimal_weight(W, w):
    # val = [[None for _ in range(W+1)] for _ in range(len(w)+1)]
    values = np.zeros((len(w) + 1, W+1))
    values[0, :] = 0
    values[:, 0] = 0
    for i in range(1, len(w)+1):
        for _w in range(1, W+1):
            values[i, _w] = values[i - 1, _w]
            if w[i-1] <= _w:
                val = values[i-1, _w - w[i-1]] + w[i-1]
                if values[i, _w] < val:
                    values[i, _w] = val
    return int(values[-1, -1])

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # sort by val/weight
    val_per_weight = map(lambda x: x[0] * 1.0 / x[1], zip(values, weights))
    vw_ranks = sorted(enumerate(val_per_weight), key=lambda x: x[1])

    while capacity > 0 and vw_ranks:
        target_i, vw = vw_ranks[-1]
        if capacity >= weights[target_i]:
            value += weights[target_i] * vw
            vw_ranks.pop()
            capacity -= weights[target_i]
            weights[target_i] = 0
        else:
            value += capacity * vw
            weights[target_i] -= capacity
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    print(data)
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))

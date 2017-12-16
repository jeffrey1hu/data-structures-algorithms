# Uses python3
import math
import numpy as np

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def minAndMax(i, j, M, m, ops):
    _min = math.inf
    _max = - math.inf
    for k in range(i, j):
        opk = ops[k]
        a = evalt(M[i, k], M[k+1, j], opk)
        b = evalt(M[i, k], m[k+1, j], opk)
        c = evalt(m[i, k], M[k+1, j], opk)
        d = evalt(m[i, k], m[k+1, j], opk)
        _min = min(_min, a, b, c, d)
        _max = max(_max, a, b, c, d)
    return _min, _max

def get_maximum_value(dataset):
    #write your code here
    numbers = dataset[0::2]
    ops = dataset[1::2]

    M = np.zeros((len(numbers), len(numbers)))
    m = np.zeros((len(numbers), len(numbers)))
    for i in range(len(numbers)):
        M[i, i] = float(numbers[i])
        m[i, i] = float(numbers[i])
    for s in range(1, len(numbers)):
        for i in range(1, len(numbers) - s + 1):
            j = i + s
            m[i-1, j-1], M[i-1, j-1] = minAndMax(i-1, j-1, M, m, ops)
    return int(M[0, -1])

if __name__ == "__main__":
    print(get_maximum_value(input()))

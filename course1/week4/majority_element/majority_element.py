# Uses python3
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def tradeoff(a, b):
    if a == -1:
        a = []
    if b == -1:
        b = []
    result = []
    while a and b:
        x = a.pop()
        y = b.pop()
        if x == y:
            result.append(x)
            result.append(y)
        else:
            continue
    result += a
    result += b
    return result

def get_majority_element(a):
    if len(a) == 1:
        return a
    m = int(len(a) / 2)
    #write your code here
    b = get_majority_element(a[:m])
    c = get_majority_element(a[m:])
    result = tradeoff(b, c)

    if not result:
        return -1
    else:
        candidate  = result[0]
        if a.count(candidate) / len(a) <= 0.5:
            return -1
        return result


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)

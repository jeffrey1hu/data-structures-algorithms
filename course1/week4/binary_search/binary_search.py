# Uses python3
import sys

def binary_search(a, x, left, right):
    # write your code here
    if right < left:
        return -1
    mid_point = int((left + right) / 2)
    if a[mid_point] == x:
        return mid_point
    elif a[mid_point] < x:
        return binary_search(a, x, mid_point+1, right)
    else:
        return binary_search(a, x, left, mid_point-1)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, len(a)-1), end = ' ')

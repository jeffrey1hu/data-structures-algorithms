# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    loop_arr = [0, 1]
    while True:
        previous, current = current, previous + current
        current %= m
        loop_arr.append(current)
        if len(loop_arr) > 3 and loop_arr[-3:] == [0, 1, 1]:
            break
    loop_arr = loop_arr[:-3]

    return loop_arr[n % len(loop_arr)]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

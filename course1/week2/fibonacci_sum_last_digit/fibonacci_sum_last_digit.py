# Uses python3
import sys
import math

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 0

    loop_arr = [0, 1]
    while True:
        previous, current = current, previous + current
        current %= 10
        loop_arr.append(current)
        if len(loop_arr) > 3 and loop_arr[-3:] == [0, 1, 1]:
            break
    loop_arr = loop_arr[:-3]

    loop_sum_last_digit = math.fsum(loop_arr) % 10


    sum += (n // len(loop_arr)) * loop_sum_last_digit
    sum += math.fsum(loop_arr[:(n % len(loop_arr))+1])
    return int(sum % 10)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))

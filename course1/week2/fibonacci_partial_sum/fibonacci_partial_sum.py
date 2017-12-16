# Uses python3
import sys
import math

def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 1
    previous = 0

    loop_arr = [0, 1]
    while True:
        previous, current = current, previous + current
        current %= 10
        loop_arr.append(current)
        if len(loop_arr) > 3 and loop_arr[-3:] == [0, 1, 1]:
            break
    loop_arr = loop_arr[:-3]

    loop_sum_last_digit = math.fsum(loop_arr) % 10


    begin_loop_idx = from_ // len(loop_arr)

    end_loop_idx = to // len(loop_arr)

    if begin_loop_idx == end_loop_idx:
        sum += math.fsum(loop_arr[(from_ % len(loop_arr)): (to % len(loop_arr)) + 1])
    else:
        # begin_part
        sum += math.fsum(loop_arr[from_ % len(loop_arr): ])
        # end part
        end_part_length = to - (begin_loop_idx + 1) * len(loop_arr)
        sum += (end_part_length // len(loop_arr)) * loop_sum_last_digit
        sum += math.fsum(loop_arr[:(end_part_length % len(loop_arr))+1])
    return int(sum % 10)


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
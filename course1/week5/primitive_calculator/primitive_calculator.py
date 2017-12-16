# Uses python3
import sys

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

def reconstruction(cal_arr):
    n = len(cal_arr) - 1
    seq = [n]
    while n > 1:
        if n % 3 == 0 and cal_arr[n//3] == cal_arr[n] - 1:
            n = n // 3
        elif n % 2 == 0 and cal_arr[n//2] == cal_arr[n] - 1:
            n = n // 2
        else:
            n = n - 1
        seq.append(n)
    seq.reverse()
    return seq

def optimal_sequence(n):
    cal_arr = [None] * (n + 1)
    cal_arr[1] = 0
    for i in range(2, n+1):
        mul2, mul3 = n, n
        if i % 2 == 0:
            mul2 = cal_arr[i // 2] + 1
        if i % 3 == 0:
            mul3 = cal_arr[i // 3] + 1
        plus1 = cal_arr[i - 1] + 1
        cal_arr[i] = min(mul2, mul3, plus1)
    return reconstruction(cal_arr)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

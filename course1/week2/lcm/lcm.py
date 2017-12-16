# Uses python3
import sys

def gcd_naive(a, b):
    # a > b
    a, b = (a, b) if a > b else (b, a)
    while b > 0:
        c = a % b
        a, b = (b, c) if b > c else (c, b)
    return a

def lcm_naive(a, b):
    gcd = gcd_naive(a, b)

    return int(a)*int(b) // int(gcd)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))


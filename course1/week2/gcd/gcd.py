# Uses python3
import sys

def gcd_naive(a, b):
    # a > b
    a, b = (a, b) if a > b else (b, a)
    while b > 0:
        c = a % b
        a, b = (b, c) if b > c else (c, b)
    return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))

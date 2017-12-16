# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    for i in range(1, n+1):
        if n >= i:
            summands.append(i)
            n -= i
        else:
            summands[-1] += n
            break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

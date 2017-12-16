#Uses python3

import sys

def largest_number(a):
    #write your code here
    max_length = len(max(a, key=len))
    a.sort(key=lambda x: x * (10 ** (max_length - len(x))), reverse=True)
    res = ""
    for x in a:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

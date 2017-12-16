# Uses python3
import sys

def get_change(m):
    #write your code here
    num = 0
    num += m // 10
    num += (m % 10) // 5
    num += (m % 10) % 5
    return num

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

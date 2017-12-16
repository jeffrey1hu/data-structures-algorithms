# python3
import sys

def BWT(text):
    _temp_texts = []
    for i in range(len(text)):
        _temp_texts.append(text[i:] + text[:i])
    _temp_texts.sort()
    return ''.join(map(lambda x: x[-1], _temp_texts))

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans


def precompute_hash(T, p_len, p, x):
    H = [None] * (len(T) - p_len + 1)
    S = T[len(T) - p_len: ]
    H[len(T) - p_len] = poly_hash(S, p, x)
    y = 1
    for i in range(p_len):
        y = (y * x) % p
    for i in range(len(T) - p_len - 1, -1, -1):
        H[i] = (x * H[i+1] + ord(T[i]) - y*ord(T[i+p_len])) % p
    return H


def get_occurrences(pattern, text):
    p = 1000000007
    x = 263
    result = []
    pHash = poly_hash(pattern, p, x)
    H = precompute_hash(text, len(pattern), p, x)
    # print("H", H)
    # print("phash", pHash)
    for i in range(len(text)-len(pattern)+1):
        if pHash != H[i]:
            continue
        if text[i: i+len(pattern)] == pattern:
            result.append(i)

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


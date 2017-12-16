#Uses python3

import sys
import numpy as np
import math

# def lcs3(a, b, c):
#     #write your code here
#     # print("X", a, "Y", b)
#     L = lcs(a, b)
#     # print("L {}".format(np.array(L)))
#     lcs_set = reconstruction(L, a, b, len(a), len(b))
#     # print("lcs_set {}".format(lcs_set))
#
#     # print("reversed lcs_set {}".format(lcs_set))
#     max_lcs = 0
#     for _lcs in lcs_set:
#         l = len(_lcs)
#         for ele in c:
#             if ele == _lcs[-1]:
#                 _lcs.pop()
#             if not _lcs:
#                 if l > max_lcs:
#                     max_lcs = l
#                 break
#
#         # _L = lcs(_lcs, c)
#         # temp_length = _L[-1][-1]
#         # if temp_length > max_lcs:
#         #     max_lcs = temp_length
#     return max_lcs


# def reconstruction(L, X, Y, m, n):
#
#     if m == 0 or n == 0:
#         return []
#     if L[m][n] == L[m-1][n-1] + 1 and L[m][n] not in (L[m-1][n], L[m][n-1]):
#         downstream_result = reconstruction(L, X, Y, m-1, n-1)
#         if downstream_result:
#             return [[X[m-1]] + ele for ele in downstream_result]
#         else:
#             return [[X[m-1]]]
#     else:
#         result = []
#         if L[m][n] == L[m-1][n]:
#             result.extend(reconstruction(L, X, Y, m-1, n))
#         if L[m][n] == L[m][n-1]:
#             result.extend(reconstruction(L, X, Y, m, n-1))
#         return result



def lcs3(X , Y, Z):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    k = len(Z)

    # declaring the array for storing the dp values
    L = np.zeros((m+1, n+1, k+1))

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            for k in range(k+1):
                if i == 0 or j == 0 or k == 0:
                    L[i, j, k] = 0
                elif X[i-1] == Y[j-1] == Z[k - 1]:
                    L[i, j, k] = L[i-1, j-1, k-1]+1
                else:
                    L[i, j, k] = max(L[i-1, j, k], L[i, j-1, k], L[i, j, k-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    # print("L[m][n] {}".format(L[m][n]))
    return int(L[-1, -1, -1])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

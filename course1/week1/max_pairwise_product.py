# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]
a.sort(reverse=True)
result = a[0] * a[1]


print(result)

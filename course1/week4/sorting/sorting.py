# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l
    m = r + 1
    i = l+1
    while i < m:
        # print("i: {}, j: {}, m: {}".format(i, j, m))
        if a[i] < x:
            j += 1
            # print("idx {} vale is {}, which is less than x {}, swap with {}".format(i, a[i], x, a[j]))
            # print("before swap {}".format(a))
            a[i], a[j] = a[j], a[i]
            # print("after swap, {}".format(a))
        elif a[i] == x:
            m -= 1
            # print("idx {} value is {} is equal to x {}, swap it to idx {} with {}".format(i, a[i], x, m, a[m]))
            # print("before swap {}".format(a))
            a[i], a[m] = a[m], a[i]
            # print("after sway, {}".format(a))
            continue
        i += 1

    # print("now before finish, swap indx {} and {}".format(l, j))
    a[l], a[j] = a[j], a[l]
    # print(a)
    # r + 1 -m means how mush equal number found
    end_idx = j+(r + 1 - m)
    # print("swap indx {} to {}".format(range(j+1, min(end_idx+1, m)), range(max(m, end_idx+1), r + 1)))
    a[j+1: min(end_idx+1, m)], a[max(m, end_idx+1): r + 1] = a[max(m, end_idx+1): r + 1], a[j+1: min(end_idx+1, m)]
    # print("after swap a is {}".format(a))
    return j, end_idx


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    # print("a: ", a)
    random.seed(1)
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # print("b: ", a, k)
    #use partition3
    m1, m2 = partition3(a, l, r)
    # print("c: ", a, m1, m2)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

# if __name__ == '__main__':
#     for i in range(1000):
#         length = random.randint(1, 100)
#         sample = [random.randint(1, 100) for i in range(length)]
#         print("test sample, ", " ".join(map(str, sample)))
#         correct_answer = sorted(sample)
#         randomized_quick_sort(sample, 0, len(sample)-1)
#         print("after sort, ", sample)
#         if not correct_answer == sample:
#             print("the result is not correct!")
#             print(len(sample))
#             break
#         print("pass!")
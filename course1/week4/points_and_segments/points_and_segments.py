# Uses python3
import sys

def binary_search(a, x, left, right):
    # write your code here
    if right < left:
        return left-1
    mid_point = int((left + right) / 2)
    if a[mid_point] == x:
        return mid_point
    elif a[mid_point] < x:
        return binary_search(a, x, mid_point+1, right)
    else:
        return binary_search(a, x, left, mid_point-1)


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    starts.sort()
    ends.sort()
    for i, point in enumerate(points):
        # large or equal then n starts
        n = binary_search(starts, point+0.1, 0, len(starts)-1) + 1
        # print("n {}".format(n))
        # less than len(start) - n starts

        # large of equal then m ends
        m = binary_search(ends, point-0.1, 0, len(ends)-1) + 1
        # print("m {}".format(m))
        # less than len(end) - m ends
        cnt[i] = max(m - n, n - m)

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

# if __name__ == '__main__':
#     import random
#     random.seed(1)
#     for _ in range(100):
#         num_of_range = random.randint(1, 100)
#         num_of_point = random.randint(1, 10)
#         starts = [random.randint(1, 100) for i in range(num_of_range)]
#         ends = [ele + random.randint(1, 100) for ele in starts]
#         points = [random.randint(1, 100) for i in range(num_of_point)]
#         cnt_gt = naive_count_segments(starts, ends, points)
#         cnt_test = fast_count_segments(starts, ends, points)
#         print(cnt_gt, cnt_test)
#         if cnt_gt != cnt_test:
#             print("Fail!")
#             print(starts, ends)
#             print(points)
#             break

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
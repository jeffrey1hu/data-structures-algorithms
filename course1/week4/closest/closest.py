#Uses python3
import sys, threading
import numpy  as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

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

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

def minimum_distance(_x, _y):
    #write your code here
    if len(_x) == 1:
        return 10 ** 18
    elif len(_x) == 2:
        # print("points distance between {} and {} is {}".format((_x[0], _y[0]), (_x[1], _y[1]), distance(_x[0], _y[0], _x[1], _y[1])))
        return distance(_x[0], _y[0], _x[1], _y[1])

    mid = len(_x) // 2

    x1, y1 = _x[:mid], _y[:mid]
    x2, y2 = _x[mid:], _y[mid:]
    # print("x1 {}, y1 {}".format(x1, y1))
    # print("x1 {}, y1 {}".format(x2, y2))
    min_dis1 = minimum_distance(x1, y1)
    min_dis2 = minimum_distance(x2, y2)

    is_in_left = False
    if min_dis1 > min_dis2:
        temp_min_dis = min_dis2
    else:
        temp_min_dis = min_dis1
        is_in_left = True
    # print("compared bet {} and {} temp_min_dis is {}".format(min_dis1, min_dis2, temp_min_dis))

    if is_in_left:
        x1_lower_bound = _x[mid]-temp_min_dis
        x1_lower_bound = x1_lower_bound - 0.1 if int(x1_lower_bound) == x1_lower_bound else x1_lower_bound
        nearest_x1_idx = max(binary_search(x1, x1_lower_bound, 0, len(x1)-1), 0)
        # print("nearest_x1_idx {}, x1_lower_bound {} in x1 {}".format(nearest_x1_idx, x1_lower_bound, x1))
        x1_candidates, y1_candidates = x1[nearest_x1_idx: ], y1[nearest_x1_idx: ]
        # print("x1_candidates, y1_candidates", x1_candidates, y1_candidates)
        base_candidates_x, base_candidates_y = x1_candidates, y1_candidates
    else:
        x2_upper_bound = _x[mid] + temp_min_dis
        x2_upper_bound = x2_upper_bound + 0.1 if int(x2_upper_bound) == x2_upper_bound else x2_upper_bound
        nearest_x2_idx = binary_search(x2, x2_upper_bound, 0, len(x2)-1)
        # print("nearest_x2_idx {}, x2_lower_bound {} in x2 {}".format(nearest_x2_idx, x2_upper_bound, x2))
        x2_candidates, y2_candidates = x2[:nearest_x2_idx+1], y2[:nearest_x2_idx+1]
        # print("x2_candidates, y2_candidates", x2_candidates, y2_candidates)
        base_candidates_x, base_candidates_y = x2_candidates, y2_candidates

    # print("base_candidates_x, base_candidates_y ", base_candidates_x, base_candidates_y)
    # print("compared_candidates_x, compared_candidates_y", compared_candidates_x, compared_candidates_y)
    min_dis = temp_min_dis
    for base_x, base_y in zip(base_candidates_x, base_candidates_y):
        y_bound = (base_y - temp_min_dis, base_y + temp_min_dis)
        if is_in_left:
            x_bound = (base_x, base_x + temp_min_dis)
            x2_boundery = x_bound[1] + 0.1 if int(x_bound[1]) == x_bound[1] else x_bound[1]
            nearest_x_idx = binary_search(x2, x2_boundery, 0, len(x2)-1)
            compared_candidates_x, compared_candidates_y = x2[:nearest_x_idx+1], y2[:nearest_x_idx+1]
        else:
            x_bound = (base_x - temp_min_dis, base_x)
            x1_boundery = x_bound[0] - 0.1 if int(x_bound[0]) == x_bound[0] else x_bound[0]
            nearest_x_idx = max(binary_search(x1, x1_boundery, 0, len(x1)-1), 0)
            compared_candidates_x, compared_candidates_y = x1[nearest_x_idx: ], y1[nearest_x_idx: ]

        for compared_x, compared_y in zip(compared_candidates_x, compared_candidates_y):
            if compared_x <= x_bound[1] \
                    and compared_x >= x_bound[0] \
                    and compared_y >= y_bound[0] \
                    and compared_y <= y_bound[1]:
                compared_dis = distance(base_x, base_y, compared_x, compared_y)
                # print("compared_dis of ({}, {}) - ({}, {}) is {}".format(base_x, base_y, compared_x, compared_y, compared_dis))
                # print("compared with temp_min_dis {}".format(compared_dis))
                if compared_dis < min_dis:
                    min_dis = compared_dis
    # print("the min distance between points {} is {}".format(list(zip(_x, _y)), min_dis))
    return min_dis

def naive_algo(_x, _y):
    min_dis = 10 ** 18
    for x1, y1 in zip(_x, _y):
        for x2, y2 in zip(_x, _y):
            if x1 == x2 and y1 == y2:
                continue
            temp_dis = distance(x1, y1, x2, y2)
            if temp_dis < min_dis:
                min_dis = temp_dis
    return min_dis

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list(zip(x, y))
    points.sort()
    x = [_x for _x, _y in points]
    y = [_y for _x, _y in points]
    print("{0:.9f}".format(minimum_distance(x, y)))

# if __name__ == '__main__':
#     import random
#     random.seed(1)
#     for _ in range(1000):
#         num_of_point = random.randint(2, 50)
#         data = sorted(list(set((random.randint(1, 20), random.randint(1, 20)) for i in range(num_of_point))))
#         x, y = [a for a, b in data], [b for a, b in data]
#
#         print(x, y)
#         dis_gt = naive_algo(x, y)
#         dis_test = minimum_distance(x, y)
#         print(dis_gt, dis_test)
#         if dis_gt != dis_test:
#             print("Fail!")
#             break
#         print("PASS \n\n\n\n")
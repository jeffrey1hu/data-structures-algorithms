# Uses python3
import sys

def merge(a, b):
    num_inv = 0
    sorted_arr = []
    while a and b:
        x = a[0]
        y = b[0]
        if x > y:
            # print("a {}, b {}, add {} invs by ele {}".format(a, b, len(y)))
            sorted_arr.append(a.pop(0))
            num_inv += len(b)
        else:
            sorted_arr.append(b.pop(0))
    sorted_arr.extend(a)
    sorted_arr.extend(b)
    return sorted_arr, num_inv

def get_number_of_inversions(a, left, right):
    # print("a: {}, b: {}, left: {}, right: {}".format(a, b, left, right))
    number_of_inversions = 0
    if right - left <= 1:
        return [a[left: right]], number_of_inversions
    ave = (left + right) // 2
    desc_arr_l, num_of_inv_l = get_number_of_inversions(a, left, ave)
    desc_arr_r, num_of_inv_r = get_number_of_inversions(a, ave, right)
    sorted_array, num_of_inv_between_l_r = merge(desc_arr_l, desc_arr_r)
    #write your code here
    number_of_inversions = (num_of_inv_l + num_of_inv_r + num_of_inv_between_l_r)
    return sorted_array, number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, 0, len(a))[1])

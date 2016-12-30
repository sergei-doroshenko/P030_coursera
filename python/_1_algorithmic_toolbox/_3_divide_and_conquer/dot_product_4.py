# Uses python3
import math
import sys


def binary_search_tup(arr, from_ind, to_ind, key):
    lo = from_ind
    hi = to_ind - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_key = arr[mid][0]
        if mid_key < key:
            lo = mid + 1
        elif mid_key > key:
            hi = mid - 1
        else:
            return mid
    return -(lo + 1)


def min_dot_product_naive(a, b):
    points = list(map(lambda x, y: (x, y), a, b))
    return min_dist_all(points)


def min_dist_all(points):
    # print('min_dist_all:{}'.format(points))
    min_dist = None
    p_1, p_2 = None, None
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            dist = calc_dist(points[i], points[j])
            if min_dist is None or dist < min_dist:
                min_dist = dist
                p_1 = points[i]
                p_2 = points[j]
    print("p_1:{}, p_2:{}, min:{}".format(p_1, p_2, min_dist))
    return min_dist


def min_dot_product_4(a, b):
    points = list(map(lambda x, y: (x, y), a, b))
    # print(points)
    # x_sorted = sorted(points, key=lambda tup: tup[0])
    x_sorted = sorted(points)
    for i in range(len(x_sorted) - 1):
        if x_sorted[i][0] == x_sorted[i + 1][0] and x_sorted[i][1] == x_sorted[i + 1][1]:
            return 0.0
    # print(x_sorted)
    y_sorted = sorted(points, key=lambda tup: tup[1])
    # print(y_sorted)
    res = min_rec(x_sorted, 0, len(x_sorted) - 1, y_sorted)
    return res


def min_rec(x_sorted, lo, hi, y_sorted):
    # print('calculate for: {}, lo:{}, hi:{}'.format(x_sorted[lo:hi+1], lo, hi))
    if hi - lo < 1:
        return None
    elif hi - lo == 1:
        # print('lo:{}, hi{}'.format(lo, hi))
        return calc_dist(x_sorted[lo], x_sorted[hi])

    mid = (lo + hi) // 2
    mid_point_x = x_sorted[mid]
    # print('mid:{}, mid_point_x:{}'.format(mid, mid_point_x))
    x_mid = mid_point_x[0]

    min_dist_left = min_rec(x_sorted, lo, mid, y_sorted)
    min_dist_right = min_rec(x_sorted, mid + 1, hi, y_sorted)

    if min_dist_left is None and min_dist_right is not None:
        min_dist = min_dist_right
    elif min_dist_right is None and min_dist_left is not None:
        min_dist = min_dist_left
    else:
        min_dist = min_dist_left if min_dist_left < min_dist_right else min_dist_right

    if min_dist == 0:
        return min_dist
    # print('min_dist:{}'.format(min_dist))
    x_temp = list(filter(lambda x: x_mid - min_dist < x[0] < x_mid + min_dist, x_sorted[lo:hi + 1]))
    # print('x_temp:{}'.format(x_temp))
    if len(x_temp) >= 2:
        # here we sort by y
        # y_temp = sorted(x_temp, key=lambda tup: tup[1])
        y_temp = []
        for ye in y_sorted:
            if binary_search_tup(x_sorted, lo, hi, ye[0]) >= 0:
                y_temp.append(ye)
        # print('y_temp:{}'.format(y_temp))
        y_temp_filtered = []
        i = 0
        while i < len(y_temp):
            if i == 0:
                if y_temp[i + 1][1] - y_temp[i][1] < min_dist:
                    y_temp_filtered.append(y_temp[i])
            elif i == len(y_temp) - 1:
                if y_temp[i][1] - y_temp[i - 1][1] < min_dist:
                    y_temp_filtered.append(y_temp[i])
            elif 0 < i < len(y_temp) - 1:
                if y_temp[i + 1][1] - y_temp[i][1] < min_dist or y_temp[i][1] - y_temp[i - 1][1] < min_dist:
                    y_temp_filtered.append(y_temp[i])
            i += 1
        # print('y_temp_filtered:{}'.format(y_temp_filtered))
        md = None
        for p in y_temp_filtered:
            for pp in y_temp_filtered:
                if p[0] == pp[0] and p[1] == pp[1]:
                    continue
                td = calc_dist(p, pp)
                if md is None or td < md:
                    md = td
        if md is not None and md < min_dist:
            min_dist = md

    # print('min_dist:{}'.format(min_dist))
    return min_dist


def calc_dist(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [8, 9, 3, -2, 5, 3, 1, 3, -6, -1, -2, -8, -4, 2, 7, 1, -8]
    # data = [4, 0, 0, 5, 6, 3, 4, 7, 2]
    # data = [4, 2, 7, 5, 8, 10, 3, 4, 4]
    # data = [2, 0, 0, 3, 4]
    # data = [11, 4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2,
    #         4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]
    # data = [7, -4, 6, -5, 10, 10, 9, 1, 0, -5, 9, -6, -10, 10, 10]
    # data = [3, 0, -7, 8, -1, 7, -2]
    n = data[0]
    a = data[1::2]
    b = data[2::2]
    # print(data)
    # print(n)
    # print(a)
    # print(b)
    print(min_dot_product_4(a, b))
    # print(min_dot_product_naive(a, b))

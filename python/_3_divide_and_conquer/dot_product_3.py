# Uses python3
import math
import sys


def calc_dist(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def brute_force(points):
    # print('min_dist_all:{}'.format(points))
    min_dist = None
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            dist = calc_dist(points[i], points[j])
            if min_dist is None or dist < min_dist:
                min_dist = dist
    return min_dist


def split(p_l, p_r, a):
    a_l, a_r = [], []
    for p in a:
        if p in p_l:
            a_l.append(p)
        elif p in p_r:
            a_r.append(p)
    return a_l, a_r


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


def min_rec(x, y):
    if len(x) <= 3:
        return brute_force(x)

    mid = len(x) // 2
    x_l = x[:mid]
    x_r = x[mid:]
    y_l, y_r = split(x_l, x_r, y)

    d_l = min_rec(x_l, y_l)
    d_r = min_rec(x_r, y_r)
    d = d_l if d_l < d_r else d_r

    xx = list(filter(lambda e: x[mid][0] - d < e[0] < x[mid][0] + d, x))
    # yy = []
    # for t in y:
    #     if t in xx:
    #         yy.append(t)
    # yy = list(filter(lambda z: z in xx, y))
    yy = []
    for el in y:
        if binary_search_tup(xx, 0, len(xx), el[0]) >= 0:
            yy.append(el)

    if len(yy) >= 2:
        yy_f = []
        i = 0
        while i < len(yy):
            if i == 0:
                if yy[i + 1][1] - yy[i][1] < d:
                    yy_f.append(yy[i])
            elif i == len(yy) - 1:
                if yy[i][1] - yy[i - 1][1] < d:
                    yy_f.append(yy[i])
            elif 0 < i < len(yy) - 1:
                if yy[i + 1][1] - yy[i][1] < d or yy[i][1] - yy[i - 1][1] < d:
                    yy_f.append(yy[i])
            i += 1

        dc = None
        for k in range(len(yy)):
            for j in range(len(yy)):
                if k == j:
                    continue
                if yy[j][1] - yy[k][1] < d:
                    td = calc_dist(yy[k], yy[j])
                    if dc is None or td < dc:
                        dc = td
                else:
                    break

        d = dc if dc is not None and dc < d else d

    return d


def min_dot_product_3(a, b):
    p = list(map(lambda x, y: (x, y), a, b))
    # print(p)
    # x_sorted = sorted(points, key=lambda tup: tup[0])
    x = sorted(p)
    # print(x)
    for i in range(len(x) - 1):
        if x[i][0] == x[i + 1][0] and x[i][1] == x[i + 1][1]:
            return 0.0

    y = sorted(p, key=lambda tup: tup[1])
    # print(y)
    res = min_rec(x, y)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [4, -6, 2, 7, -1, -7, -7, 10, 9]
    n = data[0]
    a = data[1::2]
    b = data[2::2]
    # print(data)
    # print(n)
    # print(a)
    # print(b)
    print(min_dot_product_3(a, b))

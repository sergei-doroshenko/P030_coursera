# Uses python3
import math
import sys

from python._3_divide_and_conquer.dot_product import min_dot_product_naive


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


def min_rec(p, x, y):
    if len(p) <= 3:
        return brute_force(p)

    mid = len(p) // 2
    p_l = p[:mid]
    p_r = p[mid:]
    x_l, x_r = split(p_l, p_r, x)
    y_l, y_r = split(p_l, p_r, y)

    d_l = min_rec(p_l, x_l, y_l)
    d_r = min_rec(p_r, x_r, y_r)
    d = d_l if d_l < d_r else d_r

    xx = list(filter(lambda e: x[mid][0] - d < e[0] < x[mid][0] + d, x))
    yy = []
    for t in y:
        if t in xx:
            yy.append(t)
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


def min_dot_product_2(a, b):
    p = list(map(lambda x, y: (x, y), a, b))
    print(p)
    # x_sorted = sorted(points, key=lambda tup: tup[0])
    x = sorted(p)
    print(x)
    y = sorted(p, key=lambda tup: tup[1])
    print(y)
    res = min_rec(p, x, y)
    return res


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    data = [4, -6, 2, 7, -1, -7, -7, 10, 9]
    n = data[0]
    a = data[1::2]
    b = data[2::2]
    # print(data)
    # print(n)
    # print(a)
    # print(b)
    print(min_dot_product_2(a, b))
    print(min_dot_product_naive(a, b))

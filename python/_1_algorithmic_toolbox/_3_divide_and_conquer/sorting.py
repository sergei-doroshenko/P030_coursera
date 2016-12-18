# Uses python3
import sys
import random


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


def partition_3_ways(a, lo, hi):
    v = a[lo]
    lt = lo
    gt = hi
    i = lo
    while i <= gt:
        # print(a[i])
        if a[i] < v:
            print('swap {} - {}, lt:{}, i:{}, gt:{}'.format(a[lt], a[i], lt, i, gt))
            a[i], a[lt] = a[lt], a[i]  # swap left
            i += 1
            lt += 1
        elif a[i] > v:
            print('swap {} - {}, lt:{}, i:{}, gt:{}'.format(a[i], a[gt], lt, i, gt))
            a[i], a[gt] = a[gt], a[i]  # swap right
            gt -= 1
        else:
            i += 1
    print('a: {}, lt:{}, i:{}, gt:{}'.format(a, lt, i, gt))
    return lt, gt


def partition3(a, l, r):
    x = a[l]
    # print('a: {}, pivot: {}'.format(a, x))
    n, m, k = l, l, l

    for i in range(l + 1, r + 1):
        if a[i] <= x:
            m += 1
            n += 1
            a[i], a[m] = a[m], a[i]  # swap elements
            if a[m] == x:
                k += 1
                a[m], a[k] = a[k], a[m]  # swap elements

    # print(a[l:k+1])
    # print('Before swap: {}, l-k:{}-{}, n:{}, m:{}'.format(a, l, k, n, m))
    if n > k:
        for j in range(l, k + 1):
            # print('swap {} - {}'.format(a[j], a[n]))
            a[j], a[n] = a[n], a[j]
            if j < k:
                n -= 1
            if n == k:
                break
    # print('After swap: {}, l-k:{}-{}, n:{}, m:{}'.format(a, l, k, n, m))
    return n, m


def randomized_quick_sort_3(a, l, r):
    # print('sort: {}, left: {}, right: {}'.format(a, l, r))
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    n, m = partition_3_ways(a, l, r)
    randomized_quick_sort_3(a, l, n - 1)
    randomized_quick_sort_3(a, m + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n, *a = [5, 2, 3, 9, 2, 2]
    # n, *a = [5, 4, 1, 7, 3, 6]
    # n, *a = [8, 4, 1, 7, 1, 3, 3, 6, 3]
    # n, *a = [7, 4, 3, 0, 1, 4, 2, 5]
    # n, *a = [11, 5, 5, 5, 5, 1, 5, 5, 17, 5, 5, 5]
    # randomized_quick_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')
    # print('')
    randomized_quick_sort_3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

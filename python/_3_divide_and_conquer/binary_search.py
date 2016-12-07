# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)-1
    while right - left >= 0:
        i = (left + right) // 2
        if a[i] == x:
            return i
        elif a[i] < x:
            left = i + 1
        else:
            right = i - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [5, 1, 5, 8, 12, 13, 5, 8, 1, 23, 1, 11]
    # data = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    # for x in data[n + 2:]:
    #     print(linear_search(a, x), end=' ')
    # print('')
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')

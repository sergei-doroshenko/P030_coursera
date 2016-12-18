# Uses python3

import sys


def largest_number(a):
    res = ""
    max_digit = 0
    ind = 0

    while len(a) > 0:
        for i in range(len(a)):
            if is_greater_or_equal(a[i], max_digit):
                max_digit = a[i]
                ind = i

        res += str(max_digit)
        max_digit = 0
        del a[ind]

    return res


def is_greater_or_equal(a, b):
    a, b = str(a) + str(b), str(b) + str(a)
    return int(a) >= int(b)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    # print(largest_number([1, 112]))

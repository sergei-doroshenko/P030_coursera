# Uses python3

import sys
from operator import add

from functools import reduce


def max_dot_product(a, b):
    res = 0
    a, b = sorted(a, reverse=True, ), sorted(b, reverse=True)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


def max_dot_product_2(a, b):
    return reduce(add,
                  map(lambda k, l: k * l,
                      sorted(a, reverse=True),
                      sorted(b, reverse=True)
                      )
                  )


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     a = data[1:(n + 1)]
#     b = data[(n + 1):]
#     print(max_dot_product(a, b))
print(max_dot_product([1, 3, -5], [-2, 4, 1]))
print(max_dot_product_2([1, 3, -5], [-2, 4, 1]))

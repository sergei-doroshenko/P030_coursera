# Uses python3 F(n + 2) - 1
import sys

import math


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    print("fib num: {}, sum: {}".format(current, sum))

    return sum % 10


def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n + 1):
        previous, current = current, previous + current

    return (current - 1) % 10


def fibonacci_sum_adv(n):
    fib = get_fibonacci_huge(n + 2, 10)

    if fib == 0:
        return 9
    else:
        return fib - 1


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    pisano = [0, 1]
    previous = 0
    current = 1

    for _ in range(2, n+1):
        temp = previous + current
        previous = current
        current = temp
        pisano.append(current % m)

        if pisano[len(pisano) - 2] == 0 and pisano[len(pisano) - 1] == 1:
            pisano = pisano[:len(pisano) - 2]
            break

    if len(pisano) < n:
        return pisano[n % len(pisano)]

    return pisano[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_adv(n))
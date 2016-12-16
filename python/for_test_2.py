import math

print(min(10, 1, 3, -7))


def a(n):
    def quadratic(a):
        return math.pow(a, 3)

    x = quadratic(1)
    y = quadratic(1)

    return n + x + y


print(a(1))

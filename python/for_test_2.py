import math
from python._2_data_structures._1_basic_data_structures.check_brackets import Stack


def test_min():
    print(min(10, 1, 3, -7))


def a(n):
    def quadratic(a):
        return math.pow(a, 3)

    x = quadratic(1)
    y = quadratic(1)
    return n + x + y


def test_nested():
    print(a(1))


def test_stack():
    s = Stack()
    print(s.is_empty())
    s.push('a')
    s.push('b')
    s.push('c')
    print(s.is_empty())
    while not s.is_empty():
        print(s.top())
        print(s.pop())


if __name__ == '__main__':
    test_stack()

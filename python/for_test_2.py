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


def test_arr():
    contacts = [None] * 21
    contacts[20] = "Hello"
    print(contacts[20])

def test_arr_2():
    arr = [1, 2, 3]
    arr.insert(0, 7)
    print(arr)
    print(arr.pop(0))
    print(arr)

if __name__ == '__main__':
    test_arr_2()

# Uses python3
import math


def calc_fib(n):

    if n <= 1:
        return n
    else:
        i_0 = 0
        i_1 = 1
        r = 0
        for i in range(2, n + 1):
            r = i_0 + i_1
            i_0 = i_1
            i_1 = r

        return r

def calc_fib_bine(n):
    return int((math.pow(((1 + math.sqrt(5)) / 2), n) - math.pow(((1 - math.sqrt(5)) / 2), n)) / math.sqrt(5))

def calc_fib_bine_2(n):
    a = math.pow(int((1 + math.sqrt(5)) / 2), n)
    b = math.pow(int((1 - math.sqrt(5)) / 2), n)
    return int((a - b) / math.sqrt(5))

n = int(input())
print(calc_fib(n))
print(calc_fib_bine(n))
print(calc_fib_bine_2(n))

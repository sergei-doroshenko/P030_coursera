# fibonacci numbers sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# F(20) = 6765
# F(50) = 12586269025

"""my test function"""
import time


# from __builtin__ import xrange


def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_arr(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[n]


def fib_var(n):
    i_0 = 0
    i_1 = 1
    r = 0
    for i in range(2, n + 1):
        r = i_0 + i_1
        i_0 = i_1
        i_1 = r

    return r


start_time = time.time()
print(fib_rec(40))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(fib_arr(40))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(fib_var(40))
print("--- %s seconds ---" % (time.time() - start_time))

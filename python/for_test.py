import sys
from collections import namedtuple
from operator import add

from functools import reduce

arr = [1, 2, 3, 4, 5]
print(len(arr))
print(arr[len(arr) - 1])
print(arr[:len(arr) - 1])
print(arr[:len(arr) - 2])

a = 0
b = 1
s = 2
for _ in range(10):
    a, b = b, a + b
    print("a:{}, b:{}".format(a, b))

c, d, i = 1, 3, 5
print("c: {} d:{} i:{}".format(c, d, i))

print(10 / 6)
print(1 // 6)
print(3 % 10)
print("***********************************************************")
# data = list(map(int, sys.stdin.read().split()))
# print(data)
# n, capacity = data[0:2]
# values = data[2:(2 * n + 2):2]
# weights = data[3:(2 * n + 2):2]
_list = list(map(int, "1345678"))
print(_list)
print(_list[::2])
print(_list[1::2])
junk = sorted(list(map(lambda v, w: v / w, [10, 20, 30], [1.5, 4, 3])))
print(junk)
dict_0 = {}
# map(lambda v, w: dict.update(v / w, [v, w]), [10, 20, 30], [1.5, 4, 3])
jj = sorted(list(map(lambda w, v: (v / w, (v, w)), [20, 50, 30], [60, 100, 120])))
print("jj: " + str(jj))
# print(values)

# dict = {}
# junk = list(map(lambda v, w: dict.update(v / w, [v, w]), values, weights))

print(reduce(add, range(1, 20)))

print("-------------------------------------------------------------")
Segment = namedtuple('Segment', 'start end')
n, *data = map(int, "3132536")
segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
print("n: {}".format(n))
print(segments)
print('-------------------------------------------------------------')
def get_smth():
    return 2, 3

s0, s1 = get_smth()
print('s0: {}, s1: {}'.format(s0, s1))

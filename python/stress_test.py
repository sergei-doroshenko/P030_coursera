import random
import time

from python._2_greedy.largest_number import is_greater_or_equal
from python._1_intro.max_pairwise_product_fixed import get_max_pairwise

from python._2_greedy.different_summands import optimal_summands_2, optimal_summands_rec
from python._1_intro.max_pairwise_product import get_max_pairwise1
from python._3_divide_and_conquer.dot_product import min_dot_product, min_dot_product_naive, binary_search_tup
from python._3_divide_and_conquer.dot_product_2 import min_dot_product_2
from python._3_divide_and_conquer.dot_product_3 import min_dot_product_3
from python._3_divide_and_conquer.dot_product_4 import min_dot_product_4
from python._3_divide_and_conquer.sorting import randomized_quick_sort_3, randomized_quick_sort


def test_pair():
    while True:
        n = random.randint(2, 100)
        a = []
        for i in range(0, n):
            a.append(random.randint(0, 100000))

        print(a)
        r1 = get_max_pairwise(a)
        r2 = get_max_pairwise1(a)
        if r1 != r2:
            print("Wrong answer: r1: {}, r2: {}".format(r1, r2))
        else:
            print("OK: r1: {}, r2: {}".format(r1, r2))


def test_different_summands():
    while True:
        n = random.randint(40, 100)
        print("n: {}".format(n))
        a = optimal_summands_2(n)

        if sum(a) != n:
            print("Wrong answer: n: {}, sum: {}".format(n, sum))
            break

        check_summands(a)

        b = optimal_summands_rec(n)

        if not compare_list(a, b):
            print("a: {} not equal b: {}".format(a, b))
            break

        print("OK: n: {}, \na: {}, \nb: {}".format(n, a, b))


def check_summands(a):
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            print("Wrong answer: a1: {}, a2: {}".format(a[i], a[i + 1]))
            break


def compare_list(list1, list2):
    if len(list1) != len(list2):
        print("Error. list1 has length: {}, list2: {}".format(len(list1), len(list2)))
        return False

    for i in list1:
        if i not in list2:
            print("Error. Element {} not found.".format(i))
            return False

    return True


def test_largest_number():
    print(is_greater_or_equal(232232, 232323))


def test_sorting():
    while True:
        n = random.randint(1, 2000)
        print('n: {}'.format(n))
        a = []
        for i in range(0, n):
            a.append(random.randint(1, 200))
        print("before: {}".format(a))

        randomized_quick_sort_3(a, 0, n - 1)
        print("after: {}".format(a))
        if not is_sorted(a):
            print('Error')
            break


def is_sorted(a):
    prev = 0
    result = True
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            result = False
            break
    return result


def test_dot_product():
    while True:
        n = random.randint(2, 10)
        data = [n]
        for i in range(0, n * 2):
            data.append(random.randint(-10, 10))
        a = data[1::2]
        b = data[2::2]
        print('data{}'.format(data))
        # dist_quick = run_timed(min_dot_product, [a, b])
        dist_naive = run_timed(min_dot_product_naive, [a, b])
        # dist_2 = run_timed(min_dot_product_2, [a, b])
        # dist_3 = run_timed(min_dot_product_3, [a, b])
        dist_4 = run_timed(min_dot_product_4, [a, b])
        if dist_4 == dist_naive:
            print('OK. Answer: {}, correct:{}'.format(dist_4, dist_naive))
        else:
            print('Wrong answer: {}, correct:{}'.format(dist_4, dist_naive))
            break


def test_binary_search():
    arr = [(0, 77), (1, 3), (2, 7), (4, 10), (15, 8)]
    # arr = [(-5, 3), (2, 7), (4, 10)]
    # arr = [(0, 7)]
    key = 0
    i = binary_search_tup(arr, 0, len(arr), key)
    print('key: {}, i: {}, el: {}'.format(key, i, arr[i] if i >= 0 else None))


def run_timed(func, args):
    start_time = time.time()
    r = func(*args)
    print("--- %s seconds ---" % (time.time() - start_time))
    return r


if __name__ == '__main__':
    test_dot_product()
    # test_binary_search()
import random

from python.max_pairwise_product import get_max_pairwise1
from python.max_pairwise_product_fixed import get_max_pairwise

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

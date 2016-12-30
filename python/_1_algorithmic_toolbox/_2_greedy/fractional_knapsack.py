# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.

    while capacity > 0 and len(weights) > 0 and len(values) > 0:
        max_vw, max_ind = 0, 0

        for i in range(len(weights)):
            temp = values[i] / weights[i]
            if temp > max_vw:
                max_vw, max_ind = temp, i

        if capacity >= weights[max_ind]:
            value += values[max_ind]
            capacity -= weights[max_ind]
        else:
            value += capacity * (values[max_ind] / weights[max_ind])
            capacity = 0

        del values[max_ind]
        del weights[max_ind]

    return value


def get_optimal_value_2(capacity, weights, values):
    value = 0.

    for i in sorted(list(map(lambda w, v: (v / w, (v, w)), weights, values)), reverse=True):
        if i[1][1] <= capacity:
            value += i[1][0]
            capacity -= i[1][1]
        else:
            value += i[0] * capacity
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value_2(capacity, weights, values)
    print("{:.10f}".format(opt_value))

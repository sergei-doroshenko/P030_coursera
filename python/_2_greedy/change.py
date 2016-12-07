# Uses python3
import sys


def get_change(m):
    coins = [10, 5, 1]
    n = 0
    for c in coins:
        n += m // c
        m %= c
        if m == 0:
            break

    return n


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

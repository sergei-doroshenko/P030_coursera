# Uses python3
import sys


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    pisano = [0, 1]
    previous = 0
    current = 1

    for _ in range(2, n+1):
        temp = previous + current
        previous = current
        current = temp
        pisano.append(current % m)

        if pisano[len(pisano) - 2] == 0 and pisano[len(pisano) - 1] == 1:
            pisano = pisano[:len(pisano) - 2]
            break

    if len(pisano) < n:
        return pisano[n % len(pisano)]

    return pisano[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
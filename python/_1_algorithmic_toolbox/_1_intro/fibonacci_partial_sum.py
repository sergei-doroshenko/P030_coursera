# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_partial_sum_adv(fr, to):
    from_0_m_sum = get_fibonacci_huge(fr + 1, 10)
    from_0_n_sum = get_fibonacci_huge(to + 2, 10)

    if from_0_n_sum >= from_0_m_sum:
        from_m_n_sum = from_0_n_sum - from_0_m_sum
    else:
        from_m_n_sum = from_0_n_sum + 10 - from_0_m_sum

    return from_m_n_sum


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    pisano = [0, 1]
    previous = 0
    current = 1

    for _ in range(2, n + 1):
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
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_adv(from_, to))

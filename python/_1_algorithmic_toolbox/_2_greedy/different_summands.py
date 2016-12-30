# Uses python3
import sys


def optimal_summands(n):
    summands = []
    k = 0
    while n > 0:
        k += 1
        if n >= k + 1:
            summands.append(k)
            n -= k
        elif n <= summands[-1]:
            summands[-1] += n
            n = 0
        else:
            summands.append(n)
            n = 0

    return summands


def optimal_summands_2(n):
    summands = [0]

    while n > 0:
        if n >= summands[-1] + 1:
            summands.append(summands[-1] + 1)
            n -= summands[-1]
        elif n <= summands[-1]:
            summands[-1] += n
            n = 0
        else:
            summands.append(n)
            n = 0

    return summands[1:]


def optimal_summands_rec(n):
    summands = []
    return calc(summands, n, 1)


def calc(summands, n, k):
    if n < k + 1:
        if len(summands) == 0 or n > summands[-1]:
            summands.append(n)
        else:
            summands[-1] += n
        return summands
    else:
        summands.append(k)
        n -= k
        k += 1
        return calc(summands, n, k)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    n = 6
    # summands = optimal_summands(n)
    summands = optimal_summands_2(n)
    summands = optimal_summands_rec(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

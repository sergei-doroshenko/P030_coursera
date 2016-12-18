# Uses python3
import sys


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0

    if right - left < 1:
        return number_of_inversions

    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave + 1, right)

    number_of_inversions += merge(a, b, left, ave, right)

    return number_of_inversions


def merge(a, b, left, ave, right):
    i, k = left, left
    j = ave + 1
    noi = 0
    while i <= ave and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
            noi += (ave + 1 - i)
        k += 1

    if i <= ave and j > right:
        for x in range(i, ave+1):
            b[k] = a[x]
            k += 1

    if j <= right and i > ave:
        for y in range(j, right+1):
            b[k] = a[y]
            k += 1

    for t in range(left, right + 1):
        a[t] = b[t]

    return noi


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n, *a = [5, 2, 3, 9, 2, 9]
    # n, *a = [8, 3, 2, 9, 4, 1, 8, 2, 5]
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a) - 1))


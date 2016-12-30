# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    middle = (left + right) // 2
    x = get_majority_element(a, left, middle)
    y = get_majority_element(a, middle + 1, right)
    x_n, y_n = 0, 0

    if right == len(a):
        lim = right - 1
    else:
        lim = right

    for i in range(left, lim + 1):
        if a[i] == x:
            x_n += 1
        elif a[i] == y:
            y_n += 1

    if x_n > (right - left) // 2:
        return x
    elif y_n > (right - left) // 2:
        return y

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n, *a = [5, 3, 2, 9, 2, 2]
    # n, *a = [4, 1, 2, 3, 4]
    # n, *a = [4, 1, 2, 3, 1]
    # n, *a = [3, 7, 9, 9]
    # n, *a = [1, 7]
    # n, *a = [0]
    # n, *a = [10, 2, 124554847, 2, 941795895, 2, 2, 2, 2, 792755190, 756617003]
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

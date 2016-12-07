# Uses python3
import sys


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        temp = (previous + current) % 10
        previous = current
        current = temp

    return current % 10


# if __name__ == '__main__':
#     input_data = sys.stdin.read()
#     n = int(input_data)
#     print(get_fibonacci_last_digit_naive(n))

n = int(input())
print(get_fibonacci_last_digit(n))


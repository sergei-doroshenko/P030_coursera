# Uses python3
# Results: Good job! (Max time used: 0.43/7.50, max memory used: 13774848/536870912.)
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def create_table(n):
    table = [0, 1]
    for m in range(2, n + 1):
        k_min = table[m - 1]

        if m % 2 == 0:
            k_1 = table[m // 2]
            if k_1 < k_min:
                k_min = k_1

        if m % 3 == 0:
            k_2 = table[m // 3]
            if k_2 < k_min:
                k_min = k_2

        table.append(k_min + 1)
    # print(table)
    return table


def dynamic_sequence(n):
    table = create_table(n)

    idx = len(table) - 1
    sequence = [idx]
    while table[idx] > 1:
        if table[idx - 1] == table[idx] - 1:
            idx -= 1
        elif idx % 2 == 0 and table[idx // 2] == table[idx] - 1:
            idx //= 2
        elif idx % 3 == 0 and table[idx // 3] == table[idx] - 1:
            idx //= 3
        else:
            print('Error')
            print('{} - {}'.format(idx, table[idx]))
            print(sequence)
            break
        sequence.append(idx)

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
# n = 96234
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')
# print('')
sequence = list(dynamic_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

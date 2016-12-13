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
    """
    The table contains number of actions that needed to calculate each number, represented by index.
    For instance, to calculate 1 we need add 1 to 0 - one action, to calculate 2 we need
     multiply 1 by 2 - one more action - result 2, to calculate 3 we need multiply 1 by 3 - 1+1 = 2 actions, etc.
     4 = 2 *2, where 2 = 1 *2, where 1 = 0 +1 Sum: 1(*2) + 1(*2) + 1(+1) = 3 actions.
    :param n: length of table / last index
    :return: table of number of actions needs for calculating each index from zero to n
    """
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
    """
    Calculates minimum number of actions(*3, *2 of +1) needed to get n, represented by sequence of numbers.
    e.g. for 96234 = 1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117 96234; 14 actions.
    During calculation we go from end to start of actions table and test each element by division by 3 first,
     because it's the shortest way, than by 2 and by subtract 1 (the last). By this actions we find index with
     minimum index number.
    :param n: required number
    :return: sequence of numbers with minimal length, it represents minimum number of actions needed to get n
    """
    table = create_table(n)

    idx = len(table) - 1
    sequence = [idx]
    while table[idx] > 1:
        if idx % 3 == 0 and table[idx // 3] == table[idx] - 1:
            idx //= 3
        elif idx % 2 == 0 and table[idx // 2] == table[idx] - 1:
            idx //= 2
        elif table[idx - 1] == table[idx] - 1:
            idx -= 1
        else:
            print('Error')
            print('{} - {}'.format(idx, table[idx]))
            print(sequence)
            break
        sequence.append(idx)

    return reversed(sequence)


# input = sys.stdin.read()
# n = int(input)
n = 96234
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')
# print('')
sequence = list(dynamic_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

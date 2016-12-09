# Uses python3
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


def dynamic_sequence(n):
    table = [0, 1]
    for m in range(2, n + 1):
        r = m - 1
        for i in range(2):
            if i == 0 and m % 2 == 0:
                r = m // 2
            elif i == 1 and m % 3 == 0:
                r = m // 3
        table.append(table[r] + 1)
    # print(table)

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

# Uses python3
# Results: Good job! (Max time used: 0.03/5.00, max memory used: 7757824/536870912.)

def init_matrix(x, y):
    matrix = [[i for i in range(y + 1)]]
    for x in range(1, x + 1):
        m = [x] + [0 for _ in range(y)]
        matrix.append(m)
    # matrix = [[0 for x in range(len(s) + 1)] for y in range(len(t) + 1)]
    return matrix


def print_matrix(m):
    for a in m:
        print(a)


def edit_distance(s, t):
    x, y = len(s), len(t)
    matrix = init_matrix(x, y)
    # print_matrix(matrix)
    # print('')
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            d_0 = matrix[i - 1][j] + 1
            d_1 = matrix[i][j - 1] + 1
            d_2 = matrix[i - 1][j - 1] if s[i-1] == t[j-1] else matrix[i - 1][j - 1] + 1
            matrix[i][j] = min(d_0, d_1, d_2)
    # print_matrix(matrix)
    return matrix[x][y]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance('ab', 'abc'))
    # print(edit_distance('editing', 'distance'))
    # print(edit_distance('short', 'ports'))

# Uses python3
# Results: Good job! (Max time used: 0.02/5.00, max memory used: 7725056/536870912.)
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def init_matrixes(dataset):
    n = len(dataset) - (len(dataset) - 1) // 2
    m, M = [[0 for x in range(n)] for y in range(n)], [[0 for x in range(n)] for y in range(n)]
    j = 0
    for i in range(n):
        m[i][i] = int(dataset[j])
        M[i][i] = int(dataset[j])
        j += 2
    return m, M


def print_matrix(m):
    for a in m:
        print(a)


def get_maximum_value(dataset):
    if len(dataset) == 1:
        return int(dataset)

    m, M = init_matrixes(dataset)
    # print_matrix(m)
    # print('')
    # print_matrix(M)
    # print('-------------------------------------------------------')
    n = len(dataset) - (len(dataset) - 1) // 2

    def max_min(i, j):
        r = []
        for k in range(i, j):
            op = dataset[k * 2 + 1]
            a = m[i][k]
            b = m[k + 1][j]
            t0 = evalt(a, b, op)
            r.append(t0)
            # print('({}, {}): ({}, {}) ({}, {}) {} {} {} = {}'.format(i, j, i, k, k + 1, j, a, op, b, t0))
            c = M[i][k]
            d = M[k + 1][j]
            t1 = evalt(c, d, op)
            r.append(t1)
            # print('({}, {}): ({}, {}) ({}, {}) {} {} {} = {}'.format(i, j, i, k, k + 1, j, c, op, d, t1))
        return min(r), max(r)

    for s in range(0, n):
        for i in range(0, n - s):
            j = i + s
            if i != j:
                m[i][j], M[i][j] = max_min(i, j)

    # print('-------------------------------------------------------')
    # print_matrix(m)
    # print('')
    # print_matrix(M)
    return M[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
    # print(get_maximum_value('1+5-8'))
    # print(get_maximum_value('5-8+7*4'))
    # print(get_maximum_value('1+5'))
    # print(get_maximum_value('5-8+7*4-8+9'))
    # print(get_maximum_value('5'))

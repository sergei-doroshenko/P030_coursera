# Uses python3
def evalt(a, b, op):
    # print('{} {} {}'.format(a, op, b))
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
    m, M = init_matrixes(dataset)
    # print_matrix(m)
    # print('')
    # print_matrix(M)
    # print('-------------------------------------------------------')
    n = len(dataset) - (len(dataset) - 1) // 2

    def max_min(y, x, d):
        t_0, t_1 = 0, 0
        for k in range(1, d + 1):
            r = []
            am = m[y][x - k]
            bm = m[y + k][x]
            aM = M[y][x - k]
            bM = M[y + k][x]
            op = dataset[x * 2 - 1]
            t_0 = evalt(am, bm, op)
            print('{} {} {} = {}'.format(am, op, bm, t_0))
            t_1 = evalt(aM, bM, op)
        print('-------------------------------------------------------')
        return t_0, t_1

    for s in range(0, n):
        for i in range(0, n - s):
            j = i + s
            if i != j:
                m[i][j], M[i][j] = max_min(i, j, s)
                # print('(i:{}, j:{}) = {}'.format(i, j, m[i][j]))
                # print_matrix(m)
    print('-------------------------------------------------------')
    print_matrix(m)
    print('')
    print_matrix(M)
    return M[0][n - 1]


if __name__ == "__main__":
    # print(get_maximum_value(input()))
    # print(get_maximum_value('1+5-8'))
    print(get_maximum_value('5-8+7*4'))

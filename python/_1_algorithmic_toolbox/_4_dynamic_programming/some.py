def max_result(a_):
    memo = {}
    a = list(a_)
    a.insert(0, 0)
    return min_and_max(a, 0, len(a) - 1, memo)[1]


def min_and_max(a, i, j, memo):
    if (i, j) in memo:
        return memo[i, j]
    if i == j:
        return (a[i], a[i])
    min_val = max_val = None
    for k in range(i, j):
        left = min_and_max(a, i, k, memo)
        right = min_and_max(a, k + 1, j, memo)
        for op in "*-+":
            for x in left:
                for y in right:
                    val = apply(x, y, op)
                    if min_val == None or val < min_val: min_val = val
                    if max_val == None or val > max_val: max_val = val
    ret = (min_val, max_val)
    memo[i, j] = ret
    return ret


def apply(x, y, op):
    if op == '*': return x * y
    if op == '+': return x + y
    return x - y

if __name__ == "__main__":
    print(max_result('3+2-1'))

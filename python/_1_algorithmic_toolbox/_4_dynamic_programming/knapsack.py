# Uses python3
# Results: Good job! (Max time used: 0.79/10.00, max memory used: 32501760/536870912.)
import sys


def init_matrix(W, n):
    """
    Initialize knapsack matrix
    :param W: number of columns, represents all possible knapsack weights
    :param n: number of rows, represents items of golds
    :return: matrix(n-1 x W)
    """
    matrix = [[0 for x in range(W + 1)] for y in range(n)]
    return matrix


def print_matrix(m):
    for a in m:
        print(a)


def optimal_weight(W, n, w):
    """
    Calculates optimal value that can be carried in knapsack of specific weight.
    The key point is subproblem definition: we state that optimal knapsack value is optimal value of smaller knapsack
     e.g.: W - w_i
    :param W: knapsack's weight
    :param n: number of items
    :param w: list of items values/weights
    :return: optimal value
    """
    matrix = init_matrix(W, n)
    print_matrix(matrix)
    for i in range(0, n):
        for j in range(1, W + 1):
            matrix[i][j] = matrix[i - 1][j]
            if w[i] <= j:
                # here we get optimal value of smaller knapsack and add value of current item
                val = matrix[i - 1][j - w[i]] + w[i]
                if matrix[i][j] < val:
                    matrix[i][j] = val
    print_matrix(matrix)
    result = matrix[n - 1][W]
    return result


if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    W, n, *w = [10, 3, 2, 4, 8]
    # W, n, *w = [10, 5, 3, 5, 3, 3, 5]
    print(optimal_weight(W, n, w))

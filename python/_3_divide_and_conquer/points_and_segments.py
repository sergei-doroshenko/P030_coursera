# Uses python3
from bisect import bisect_left

import sys

"""
    segments: [0,5]                       |------|
              [7,10]    |-----------|
    points:    1 6 11   |--|--------|--|--|------|--|
    results:   1 0 0    0  1        5  6  7     10  11
                           ^           ^
    pairs:    (0, l), (7, l), (5, r), (10, r), (1, p), (6, p), (11, p)
    sorted:   (0, 1), (1, p), (5, r), (6, p), (7, l), (10, r), (11, p)
         i: 0 -> +1 -> add  -> -1   -> skip ->  +1  ->   -1  -> skip
    if 'l' - increment, if 'r' - decrement, if 'p' and i > 0 write count to results
"""


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    sorted_points = sorted(points)
    points_ = []
    for j in range(len(points)):
        points_.append((points[j], j))
    points_ = sorted(points_)
    # print(points_)
    pairs = sorted(list(map(lambda x: (x, 'p'), points)) +
                   list(map(lambda x: (x, 'l'), starts)) +
                   list(map(lambda x: (x, 'r'), ends))
                   )
    # print(pairs)
    i = 0
    for pair in pairs:
        if pair[1] == 'l':
            i += 1
        elif pair[1] == 'r':
            i -= 1
        else:
            if i > 0:
                pos = bisect_left(sorted_points, pair[0])
                cnt[points_[pos][1]] += i
                del sorted_points[pos]  # in case of equals points bisect_left will always find the same object
                del points_[pos]
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]
    # starts = [-9, 14, 32]
    # ends = [52, 97, 77]
    # points = [-9, -9, -9]

    starts = [0, 7]
    ends = [5, 10]
    points = [1, 6, 11]
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
    # print('')
    cnt_2 = fast_count_segments(starts, ends, points)
    for x in cnt_2:
        print(x, end=' ')

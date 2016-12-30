# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments1):
    points1 = []
    point = 0
    for s in sorted(segments1):
        if point == 0:
            point = s.end
        elif s.start <= point > s.end:
            point = s.end
        elif s.start > point > 0:
            points1.append(point)
            point = s.end

    if point > 0:
        points1.append(point)
    return points1


def optimal_points_2(segments2):
    points2 = []

    for s in sorted(segments2):
        if len(points2) == 0:
            points2.append(s.end)
        elif s.start <= points2[-1] > s.end:
            points2[-1] = s.end
        elif s.start > points2[-1] > 0:
            points2.append(s.end)

    return points2


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    # n, *data = map(int, "0")
    # n, *data = map(int, "127")
    # n, *data = map(int, "3251336")
    # n, *data = map(int, "447132556")
    # n, *data = map(int, "6142523465624")
    # n, *data = map(int, "51425465624")
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points_2(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

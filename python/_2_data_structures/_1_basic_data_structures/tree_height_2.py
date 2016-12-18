# python3
# Results: Good job! (Max time used: 0.45/3.00, max memory used: 108150784/536870912.)
import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def read_from_file():
    with open('tree_input.txt') as f:
        lines = f.readlines()
        print(lines)
        n = int(lines[0])
        data = list(map(int, lines[1].split()))
        return n, data


class TreeHeight:
    def __init__(self):
        self.nodes = []
        self.parent = []
        self.n = 0
        self.root = None

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        # self.n = 5
        # self.parent = [4, -1, 4, 1, 1]
        # self.parent = [-1, 0, 4, 0, 3]
        # self.n, self.parent = read_from_file()

        for i in range(self.n):
            self.nodes.append([])

        for j in range(self.n):
            parent_index = self.parent[j]
            if parent_index == -1:
                self.root = self.nodes[j]
            else:
                self.nodes[parent_index].append(j)

    def compute_height(self):
        max_height = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            max_height = max(max_height, height)
        return max_height

    def height_rec(self, arr):
        if len(arr) == 0:
            return 0
        else:
            h = 0
            for i in arr:
                t = self.height_rec(self.nodes[i])
                if t > h:
                    h = t
            # print('{} - {}'.format(i, 1 + h))
            return 1 + h


def main():
    tree = TreeHeight()
    tree.read()
    # print(tree.compute_height())
    print(1 + tree.height_rec(tree.root))


threading.Thread(target=main).start()

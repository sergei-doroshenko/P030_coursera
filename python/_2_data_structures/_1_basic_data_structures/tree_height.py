# python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Node:
    def __init__(self, parent_index):
        self.parent_index = parent_index
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class TreeHeight:
    def __init__(self):
        self.nodes = []
        self.root = None

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        # self.n = 5
        # self.parent = [4, -1, 4, 1, 1]
        # self.parent = [-1, 0, 4, 0, 3]

        for i in range(self.n):
            self.nodes.append(Node(parent_index=self.parent[i]))

        for ci in range(self.n):
            node = self.nodes[ci]
            parent_index = node.parent_index
            if parent_index == -1:
                self.root = node
            else:
                self.nodes[parent_index].add_child(node)

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

    def height_rec(self, nodes):
        if len(nodes) == 0:
            return 0
        else:
            h = 0
            for n in nodes:
                t = self.height_rec(n.children)
                if t > h:
                    h = t
            return 1 + h

    def height_bfs(self, nodes):
        if len(nodes) == 0:
            return
        q = []


def main():
    tree = TreeHeight()
    tree.read()
    # print(tree.compute_height())
    print(tree.height_rec(tree.nodes))


threading.Thread(target=main).start()

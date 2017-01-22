# python3
# Good job! (Max time used: 1.02/6.00, max memory used: 92930048/536870912.)

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order_traversal(self, i, result):
        if i == -1:
            return
        self.in_order_traversal(self.left[i], result)
        result.append(self.key[i])
        self.in_order_traversal(self.right[i], result)

    def inOrder(self):
        self.result = []
        self.in_order_traversal(0, self.result)
        return self.result

    def pre_order_traversal(self, i, result):
        if i == -1:
            return
        result.append(self.key[i])
        self.pre_order_traversal(self.left[i], result)
        self.pre_order_traversal(self.right[i], result)

    def preOrder(self):
        self.result = []
        self.pre_order_traversal(0, self.result)
        return self.result

    def post_order_traversal(self, i, result):
        if i == -1:
            return
        self.post_order_traversal(self.left[i], result)
        self.post_order_traversal(self.right[i], result)
        result.append(self.key[i])

    def postOrder(self):
        self.result = []
        self.post_order_traversal(0, self.result)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()

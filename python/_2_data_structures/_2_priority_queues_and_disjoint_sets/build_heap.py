# python3
# Good job! (Max time used: 0.52/3.00, max memory used: 26140672/536870912.)

"""
Builds binary min-heap.
"""


class HeapBuilder:
    def __init__(self):
        self._swaps = []  # stores tuples with swaps, e.g. (1, 4)
        self._data = []  # array of numbers for build a heap
        self._size = 0

    @staticmethod
    def parent(i):
        """
        Returns index of parent element for a 0-based array heap
        :param i: index of a heap leaf
        :return: index of it's parent node
        """
        return (i - 1) / 2

    @staticmethod
    def left_child(i):
        """
        Returns index of left child node.
        :param i: parent's node index
        :return: left child's node index
        """
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        """
        Returns index of right child node for particular parent.
        :param i: parent's node index
        :return: right child's node index
        """
        return 2 * i + 2

    def swap(self, i, j):
        """
        Swaps two elements in _data, adds indices of swap elements as a tuple in the _swaps list.
        :param i: index of first element
        :param j: index of second element
        """
        self._swaps.append((i, j))
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def shift_up(self, i):
        """
        Shifts element with specified index up in the heap. Can be called after inserting element.
        :param i:  index of shifted element
        """
        j = HeapBuilder.parent(i)
        while i > 0 and self._data[j] > self._data[i]:
            self.swap(i, j)
            i = HeapBuilder.parent(i)
            j = HeapBuilder.parent(i)

    def shift_down(self, i):
        """
        Shift element with specified index down in the heap. Can be called after get_max (not implemented)
        and swap max element with the last leaf.
        :param i: index of shifted element
        """
        min_index = i
        # look for minimum from left and right child nodes
        l = HeapBuilder.left_child(i)
        if l < self._size and self._data[l] < self._data[min_index]:
            min_index = l

        r = HeapBuilder.right_child(i)
        if r < self._size and self._data[r] < self._data[min_index]:
            min_index = r
        # swap with left or right children
        if i != min_index:
            self.swap(i, min_index)
            self.shift_down(min_index)  # call shift_down recursively

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        # n = 5
        # self._data = [5, 4, 3, 2, 1]
        # self._data = [1, 2, 3, 4, 5]
        self._size = len(self._data)
        assert n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def generate_swaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        # for i in range(len(self._data)):
        #     for j in range(i + 1, len(self._data)):
        #         if self._data[i] > self._data[j]:
        #             self.swap(i, j)

        for i in range(self._size // 2, -1, -1):  # starts from _size // 2 - specific for heaps!!!
            self.shift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()

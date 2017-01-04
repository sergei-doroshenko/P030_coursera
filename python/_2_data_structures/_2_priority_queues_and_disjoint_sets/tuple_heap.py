# python3
# Good job! (Max time used: 0.52/3.00, max memory used: 26140672/536870912.)

"""
Builds binary min-heap.
"""


class TupleHeap:
    def __init__(self, data):
        self._data = data  # array of numbers for build a heap
        self._size = len(data)
        self.build_heap()

    def parent(self, i):
        """
        Returns index of parent element for a 0-based array heap
        :param i: index of a heap leaf
        :return: index of it's parent node
        """
        return (i - 1) // 2

    def left_child(self, i):
        """
        Returns index of left child node.
        :param i: parent's node index
        :return: left child's node index
        """
        return 2 * i + 1

    def right_child(self, i):
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
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def shift_up(self, i):
        """
        Shifts element with specified index up in the heap. Can be called after inserting element.
        :param i:  index of shifted element
        """
        j = self.parent(i)
        while i > 0 and self.is_less(self._data[i], self._data[j]):
            self.swap(i, j)
            i = j
            j = self.parent(i)

    def is_less(self, a, b):
        if a[0] < b[0]:
            return True
        elif a[0] == b[0]:
            return a[1] < b[1]
        return False

    def shift_down(self, i):
        """
        Shift element with specified index down in the heap. Can be called after get_max (not implemented)
        and swap max element with the last leaf.
        :param i: index of shifted element
        """
        min_index = i
        # look for minimum from left and right child nodes
        l = self.left_child(i)
        if l < self._size and self.is_less(self._data[l], self._data[min_index]):
            min_index = l

        r = self.right_child(i)
        if r < self._size and self.is_less(self._data[r], self._data[min_index]):
            min_index = r
        # swap with left or right children
        if i != min_index:
            self.swap(i, min_index)
            self.shift_down(min_index)  # call shift_down recursively

    def build_heap(self):
        for i in range(self._size // 2, -1, -1):  # starts from _size // 2 - specific for heaps!!!
            self.shift_down(i)

    def get_min(self):
        if self._size <= 0:
            return None
        result = self._data[0]
        self._data[0] = self._data[self._size - 1]
        self._size -= 1
        self.shift_down(0)
        return result

    def insert(self, p):
        self._size += 1
        self._data[self._size - 1] = p
        self.shift_up(self._size - 1)

    def write_response(self):
        print(self._data)


if __name__ == '__main__':
    heap_0 = TupleHeap(data=[(0, i) for i in range(2)])
    for i in range(1, 6):
        w = heap_0.get_min()
        print(str(w) + ' ' + str(w[1]) + ' ' + str(w[0]))
        heap_0.insert((w[0]+i, w[1]))
    print('-------------------------------------------------------')
    heap_1 = TupleHeap(data=[(0, i) for i in range(4)])
    for i in range(1, 21):
        w = heap_1.get_min()
        print(str(w) + ' ' + str(w[1]) + ' ' + str(w[0]))
        heap_1.insert((w[0]+1, w[1]))
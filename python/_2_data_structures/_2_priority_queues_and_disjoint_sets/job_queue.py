# python3
# Good job! (Max time used: 3.70/6.00, max memory used: 35385344/536870912.)


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        # self.num_workers, m = 2, 5
        # self.jobs = [1, 2, 3, 4, 5]
        # self.num_workers, m = 4, 20
        # self.jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

    def assign_jobs_heap(self):
        heap = TupleHeap(data=[(0, i) for i in range(self.num_workers)])
        for i in range(len(self.jobs)):
            w = heap.get_min()
            print(w[1], w[0])
            heap.insert((w[0] + self.jobs[i], w[1]))

    def solve_heap(self):
        self.read_data()
        self.assign_jobs_heap()


class TupleHeap:
    def __init__(self, data):
        self._data = data  # array of tuples for build a heap
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

    def is_less(self, a, b):
        """
        Extremely important method, calls from shift_up and shift_down methods to figure out if tuple less or equals.
        :param a: first tuple
        :param b: second tuple
        :return: True if tuple is less, otherwise - False
        """
        if a[0] < b[0]:  # compares time at first
            return True
        elif a[0] == b[0]:  # if time is equals, compare by priority
            return a[1] < b[1]
        return False

    def build_heap(self):
        """
        Builds a heap from shuffled array of numbers.
        """
        for i in range(self._size // 2, -1, -1):  # starts from _size // 2 - specific for heaps!!!
            self.shift_down(i)

    def get_min(self):
        """
        Returns the minimum heap element, placed at the root node (vertex) of heap.
        :return: the minimum element.
        """
        if self._size <= 0:
            return None
        result = self._data[0]
        self._data[0] = self._data[self._size - 1]
        self._size -= 1
        self.shift_down(0)
        return result

    def insert(self, p):
        """
        Inserts new element to the heap.
        :param p: new element (number)
        """
        self._size += 1
        self._data[self._size - 1] = p
        self.shift_up(self._size - 1)

if __name__ == '__main__':
    job_queue = JobQueue()
    # job_queue.solve()
    # print('------------------------')
    job_queue.solve_heap()

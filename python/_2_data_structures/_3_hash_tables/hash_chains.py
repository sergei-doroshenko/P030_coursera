# python3
# Good job! (Max time used: 1.57/7.00, max memory used: 25636864/536870912.)
# Implementation of hash table with chaining and buckets.


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        """
        Polynomial hash function: calculates hash as a sum of expression with each character(CodePoint).
        :param s: input string
        :return: hash
        """
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.elems[query.ind])
        else:
            # calculates a hash to find correct bucket
            _hash = self._hash_func(query.s)
            try:
                ind = self.elems[_hash].index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems[_hash].insert(0, query.s)
            else:
                if ind != -1:
                    self.elems[_hash].pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
        # for query in list(map(lambda s: Query(s.split()), [
        #     'add world',
        #     'add HellO',
        #     'check 4',
        #     'find World',
        #     'find world',
        #     'del world',
        #     'check 4',
        #     'del HellO',
        #     'add luck',
        #     'add GooD',
        #     'check 2',
        #     'del luck',
        #     'check 2'
        # ])):
        #     self.process_query(query)


if __name__ == '__main__':
    bucket_count = int(input())
    # bucket_count = 5
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

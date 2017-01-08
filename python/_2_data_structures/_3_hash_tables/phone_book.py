# python3
# Good job! (Max time used: 0.75/6.00, max memory used: 116998144/671088640.)
# Implements hash table using direct addressing scheme


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]
    # return list(map(lambda s: Query(s.split()), [
    #     'find 3839442',
    #     'add 123456 me',
    #     'add 0 granny',
    #     'find 0',
    #     'find 123456',
    #     'del 0',
    #     'del 0',
    #     'find 0'
    # ]))
    # return list(map(lambda s: Query(s.split()), [
    #     'add 911 police',
    #     'add 76213 Mom',
    #     'add 17239 Bob',
    #     'find 76213',
    #     'find 910',
    #     'find 911',
    #     'del 910',
    #     'del 911',
    #     'find 911',
    #     'find 76213',
    #     'add 76213 daddy',
    #     'find 76213'
    # ]))


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Init list of all possible phone numbers with no more than 7 digits.
    contacts = [None] * 10000000
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None
        else:
            response = 'not found' if contacts[cur_query.number] is None else contacts[cur_query.number].name
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

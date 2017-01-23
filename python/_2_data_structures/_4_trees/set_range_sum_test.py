from python._2_data_structures._4_trees.set_range_sum import insert, _sum, erase


def test_01():
    insert(1)
    insert(2)
    insert(4)
    print(_sum(1, 2))
    print(_sum(1, 2))
    print(_sum(1, 2))
    insert(5)
    print(_sum(1, 2))


def test_02():
    insert(1)
    insert(2)
    insert(4)
    erase(1)
    erase(2)
    erase(4)

if __name__ == '__main__':
    test_02()
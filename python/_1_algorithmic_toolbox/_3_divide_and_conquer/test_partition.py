from python._1_algorithmic_toolbox._3_divide_and_conquer.sorting import partition_3_ways


def test_partition_3_ways():
    # a = [4, 3, 5, 2, 4, 7, 3, 4]
    a = [4, 3, 5, 2, 7]
    print(a)
    lt, gt = partition_3_ways(a, 0, 4)
    print('a{}: lt{}: gt:{}'.format(a, lt, gt))

if __name__ == '__main__':
    test_partition_3_ways()
# Uses python3
def get_max_pairwise(numbers):
    n = len(numbers)
    assert(n > 0)
    max1 = -1
    max2 = -1
    for i in range(0, n):
        if max1 == -1 or numbers[i] > numbers[max1]:
            max1 = i

    for i in range(0, n):
        if (max2 == -1 or numbers[i] > numbers[max2]) and i != max1:
            max2 = i

    # print(str(max1) + " " + str(max2))

    return numbers[max1] * numbers[max2]

# n = int(input())
# a = [int(x) for x in input().split()]
# assert (len(a) == n)
# result = get_max_pairwise(a)
# print(result)




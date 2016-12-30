__author__ = 'Sergei_Admin'


def test_tree():
    with open('tree_input.txt') as f:
        lines = f.readlines()
        print(lines)
        n = int(lines[0])
        data = list(map(int, lines[1].split()))
        return n, data


if __name__ == '__main__':
    print(test_tree())

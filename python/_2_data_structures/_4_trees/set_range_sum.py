# python3

from sys import stdin


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v


def small_rotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def big_rotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    else:
        # Zig-zag
        small_rotation(v)
        small_rotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)


def split(_root, key):
    (result, new_root) = find(_root, key)
    if result is None:
        return new_root, None
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return left, right


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Helpers
# log_on = True


log_on = False


def log(message):
    if log_on:
        print(message)


def in_order_traverse(r, result):
    if r is None:
        return
    in_order_traverse(r.left, result)
    result.append(r.key)
    in_order_traverse(r.right, result)


def in_order(r):
    result = []
    in_order_traverse(r, result)
    log(result)


def pre_order_traverse(r, result):
    if r is None:
        return
    result.append(r.key)
    pre_order_traverse(r.left, result)
    pre_order_traverse(r.right, result)


def pre_order(r):
    result = []
    pre_order_traverse(r, result)
    log(result)


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)
    # find(root, x)
    # pre_order(root)


def erase1(x):
    global root
    (next, new_root) = find(root, x)
    log(next.key if next is not None else 'None')
    root = new_root
    if next is not None and next.key == x:
        (left, right) = split(root, x)
        if left is not None and left.key == x:
            root = merge(merge(left.left, left.right), right)
        elif right is not None and right.key == x:
            root = merge(left, merge(right.left, right.right))
    # pre_order(root)


def erase(x):
    global root
    (next, new_root) = find(root, x)
    log(next.key if next is not None else 'None')
    root = new_root
    if next is not None and next.key == x:
        (left, right) = split(root, x)  # x is exactly in the right sub-tree and right.left is None
        right = right.right
        if right is not None:
            right.parent = None
        root = merge(left, right)
    # pre_order(root)


def search(x):
    global root
    (next, new_root) = find(root, x)
    root = new_root
    found = next.key == x if next is not None else False
    # pre_order(root)
    return found


def _sum(fr, to):
    global root
    if fr > to:
        fr, to = to, fr
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    if middle is not None:
        ans += middle.sum
    root = merge(left, merge(middle, right))
    # pre_order(root)
    return ans


if __name__ == '__main__':
    MODULO = 1000000001
    n = int(stdin.readline())
    last_sum_result = 0
    for i in range(n):
        line = stdin.readline().split()
        if line[0] == '+':
            x = int(line[1])
            insert((x + last_sum_result) % MODULO)
        elif line[0] == '-':
            x = int(line[1])
            erase((x + last_sum_result) % MODULO)
        elif line[0] == '?':
            x = int(line[1])
            print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
        elif line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            res = _sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
            print(res)
            last_sum_result = res % MODULO

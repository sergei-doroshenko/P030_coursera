# python3
# Results: Good job! (Max time used: 0.18/1.00, max memory used: 15974400/536870912.)
import sys


class Stack:
    def __init__(self):
        self.a = []

    def push(self, key):
        self.a.append(key)

    def top(self):
        return self.a[len(self.a) - 1]

    def pop(self):
        return self.a.pop(len(self.a) - 1)

    def is_empty(self):
        return len(self.a) == 0


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()
    # text = '[]'
    # text = '{}[]'
    # text = '[()]'
    # text = '(())'
    # text = '{[]}()'
    # text = '{'
    # text = '{[}'
    # text = 'foo(bar);'
    # text = 'foo(bar[i);'
    # text = '}]]'

    opening_brackets_stack = Stack()
    for i, n in enumerate(text):
        if n == '(' or n == '[' or n == '{':
            opening_brackets_stack.push(Bracket(n, i + 1))

        if n == ')' or n == ']' or n == '}':
            if opening_brackets_stack.is_empty():
                opening_brackets_stack.push(Bracket(n, i + 1))
                break
            else:
                p = opening_brackets_stack.top()
                if p.match(n):
                    opening_brackets_stack.pop()
                else:
                    opening_brackets_stack.push(Bracket(n, i + 1))
                    break

    if opening_brackets_stack.is_empty():
        print('Success')
    else:
        print(opening_brackets_stack.top().position)

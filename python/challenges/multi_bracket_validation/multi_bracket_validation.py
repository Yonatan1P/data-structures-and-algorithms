class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class InvalidOperationError(Exception):
    pass


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        if self.top:
            return False
        return True

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value


def match_brackets(string):
    pair_bank = {
        "{": "}",
        "[": "]",
        "(": ")"}
    match_stack = Stack()
    for char in string:
        for bracket in pair_bank:
            if bracket == char:
                match_stack.push(bracket)
            elif pair_bank[bracket] == char:
                if not match_stack.top:
                    return False
                elif match_stack.top.value == char:
                    match_stack.pop()
                else:
                    return False
    print('this is the match stack:',match_stack.top)
    return not match_stack.top

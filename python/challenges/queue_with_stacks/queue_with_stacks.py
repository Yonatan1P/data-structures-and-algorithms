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

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value


class PsuedoQueue:
    
    def __init__(self):
        self.top = None
        self.main = Stack()
        self.temporary = Stack()

    def enqueue(self, value):
        while self.main.top:
            self.temporary.push(self.main.top.value)
            self.main.pop()
        self.main.push(value)
        while self.temporary.top:
            self.main.push(self.temporary.top.value)
            self.temporary.pop()
        self.top = self.main.top

    def dequeue(self):
        if self.top:
            output = self.top.value
            self.main.pop()
            self.top = self.main.top
            return output

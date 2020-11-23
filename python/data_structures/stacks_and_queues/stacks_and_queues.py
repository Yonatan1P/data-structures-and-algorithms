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


class Queue():

    def __init__(self):
        self.front = None

    def enqueue(self, value):
        current = self.front
        node = Node(value)
        if not current:
            self.front = node
            return
        else:
            while current.next:
                current = current.next
            current.next = node

    def dequeue(self):
        current = self.front
        print(current.next.value)
        if not current:
            return
        else:
            while current.next:
                current = current.next
            return

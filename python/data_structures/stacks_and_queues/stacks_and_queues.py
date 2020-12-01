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
        self.rear = None

    def enqueue(self, value):
        if not self.rear:
            self.rear = Node(value)
            self.front = self.rear
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        # current = self.front
        # node = Node(value)
        # if not current:
        #     self.front = node
        #     return
        # else:
        #     while current.next:
        #         current = current.next
        #     current.next = node

    def dequeue(self):
        current = self.front

        if not current:
            # raise exception
            raise InvalidOperationError('dequeue error')
        else:
            if self.front == self.rear:
                self.rear = None
            self.front = current.next
            return current.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError('No front for peek') # Throw an error if there is no self.front
        return self.front.value

    def is_empty(self):
        return not self.front

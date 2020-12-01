class Node:
    '''each node represents a different dog or cat object
    They each have a name, a type (cat or dog), and a
    reference to the next animal in the shelter queue
    '''
    def __init__(self, animal_type, next_node=None):
        self.animal_type = animal_type
        self.next = next_node


class InvalidOperationError(Exception):
    pass


class Queue:
    '''Queue of animals in the animal shelter
    Follows first in first out (fifo) principle
    First animal enqueued should be the first animal dequeued
    '''
    def __init__(self):
        self.front = None

    def enqueue(self, animal_type=None):
        new_node = Node(animal_type)
        if not self.front:
            self.front = new_node
        else:
            current = self.front
            while current.next:
                current = current.next
            current.next = new_node

    def dequeue(self, preference=None):
        current = self.front
        if not current:
            return "No animals available"
        if not preference:
            first = self.front
            self.front = current.next
            return first.animal_type
        if preference != "cat" and preference != "dog":
            return "Null"
        while current.animal_type != preference:
            if current.next:
                previous_node = current
                current = current.next
                next_node = current.next
            else:
                return "Null"
        previous_node.next = next_node
        return current.animal_type

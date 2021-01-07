from challenges.stacks_and_queues.stacks_and_queues import Queue


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        node = Node(value, None, None)

        if not self.root:
            self.root = node
            return

        temp_queue = Queue()
        temp_queue.enqueue(self.root)

        while not temp_queue.is_empty():
            current = temp_queue.dequeue()
            
            if not current.left:
                current.left = node
                return
            else:
                temp_queue.enqueue(current.left)

            if not current.right:
                current.right = node
                return
            else:
                temp_queue.enqueue(current.right)



    def breadth_first_traversal(self):

        output = []
        temp_queue = Queue()

        if not self.root:
            return

        temp_queue.enqueue(self.root)

        while not temp_queue.is_empty():
            current_node = temp_queue.dequeue()
            output += [current_node.value]
            if current_node.left:
                temp_queue.enqueue(current_node.left)

            if current_node.right:
                temp_queue.enqueue(current_node.right)

        return output

    def find_maximum_value(self):

        if self.root:
            max_value = self.root.value
        else:
            max_value = False

        def walk(root):
            nonlocal max_value
            if not root:
                return
            if root.value > max_value:
                max_value = root.value

            walk(root.left)
            walk(root.right)

        walk(self.root)

        return max_value

    def preOrder(self):
        values = []

        def walk(root):
            if not root:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)
        walk(self.root)
        return values

    def postOrder(self):
        values = []

        def walk(root):
            if not root:
                return
            walk(root.left)
            walk(root.right)
            values.append(root.value)
        walk(self.root)
        return values

    def inOrder(self):
        values = []

        def walk(root):
            if not root:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)
        walk(self.root)
        return values


class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return self.root

        def walk(root):

            if root.value == value:
                return root

            elif root.value < value:
                if not root.right:
                    root.right = Node(value)
                root.right = walk(root.right)

            else:
                if not root.left:
                    root.left = Node(value)
                root.left = walk(root.left)
            return root

        walk(self.root)

    def contains(self, value):

        def walk(current):

            if not current:
                return False

            if current.value == value:
                return True

            else:
                if value < current.value:
                    return walk(current.left)
                else:
                    return walk(current.right)

        return walk(self.root)

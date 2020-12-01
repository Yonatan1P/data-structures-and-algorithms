class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

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
    #    if root:
    #        self.preOrder(self.root.left)
    #        print(self.root.value)
    #        self.preOrder(self.root.right)


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
    #    if root:
    #        self.postOrder(self.root.left)
    #        self.postOrder(self.root.right)
    #        print(self.root.value)

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
                    root.right=Node(value)
                root.right = walk(root.right)

            else:
                if not root.left:
                    root.left=Node(value)
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

from challenges.binarytree_sum.binarytree_sum import totalUsage
from challenges.tree.tree import BinaryTree


def test_happy_path():
    tree = BinaryTree()
    tree.insert(35)
    tree.insert(41)
    tree.insert(59)
    tree.insert(33)
    tree.insert(52)
    tree.insert(30)
    tree.insert(44)
    actual = totalUsage(tree)
    expected = 294
    assert actual == expected


def test_empty_input():
    tree = BinaryTree()
    actual = totalUsage(tree)
    expected = 0
    assert actual == expected

def test_empty_input():
    tree = BinaryTree()
    tree.insert('h')
    tree.insert('i')
    tree.insert(' ')
    tree.insert('t')
    tree.insert('h')
    tree.insert('e')
    tree.insert('r')
    tree.insert('e')
    actual = totalUsage(tree)
    expected = 'hi there'
    assert actual == expected

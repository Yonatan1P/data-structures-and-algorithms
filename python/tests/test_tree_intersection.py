from challenges.tree_intersection.tree_intersection import find_intersection
from challenges.tree.tree import BinarySearchTree

def test_find_intersection():
    tree1 = BinarySearchTree()
    tree1.add(1)
    tree1.add(2)
    tree1.add(3)
    tree1.add(4)
    tree1.add(5)
    tree1.add(6)
    tree1.add(7)
    tree1.add(8)
    tree2 = BinarySearchTree()
    tree2.add(12)
    tree2.add(12)
    tree2.add(13)
    tree2.add(14)
    tree2.add(15)
    tree2.add(16)
    tree2.add(7)
    tree2.add(8)
    actual = find_intersection(tree1, tree2)
    expected = [7,8]
    assert actual == expected

def test_empty_binary_tree():
    tree1 = BinarySearchTree()
    tree1.add(1)
    tree1.add(2)
    tree1.add(3)
    tree1.add(4)
    tree1.add(5)
    tree1.add(6)
    tree1.add(7)
    tree1.add(8)
    tree2 = BinarySearchTree()
    actual = find_intersection(tree1, tree2)
    expected = []
    assert actual == expected

def test_first_empty_binary_tree():
    tree2 = BinarySearchTree()
    tree2.add(1)
    tree2.add(2)
    tree2.add(3)
    tree2.add(4)
    tree2.add(5)
    tree2.add(6)
    tree2.add(7)
    tree2.add(8)
    tree1 = BinarySearchTree()
    actual = find_intersection(tree1, tree2)
    expected = []
    assert actual == expected

def test_same_tree():
    tree1 = BinarySearchTree()
    tree1.add(1)
    tree1.add(2)
    tree1.add(3)
    tree1.add(4)
    tree1.add(5)
    tree1.add(6)
    tree1.add(7)
    tree1.add(8)
    tree2 = BinarySearchTree()
    tree2.add(1)
    tree2.add(2)
    tree2.add(3)
    tree2.add(4)
    tree2.add(5)
    tree2.add(6)
    tree2.add(7)
    tree2.add(8)
    actual = find_intersection(tree1, tree2)
    expected = [1,2,3,4,5,6,7,8]
    assert actual == expected

from challenges.tree.tree import BinarySearchTree, BinaryTree


def test_init_empty_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected


def test_tree_with_root():
    tree = BinarySearchTree()
    tree.add(1)
    actual = tree.root.value
    expected = 1
    assert actual == expected


def test_tree_with_root_and_left():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(1)
    actual = tree.root.value
    expected = 2
    assert actual == expected


def test_tree_with_root_and_right():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    actual = tree.root.right.value
    expected = 2
    assert actual == expected


def test_add_full_tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(2)
    tree.add(30)
    tree.add(4)
    tree.add(15)
    tree.add(20)
    tree.add(17)
    tree.add(22)
    actual = tree.root.left.right.value
    expected = 4
    assert actual == expected


def test_pre_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(2)
    tree.add(30)
    tree.add(4)
    actual = tree.preOrder()
    expected = [10, 2, 4, 30]
    assert actual == expected


def test_post_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(2)
    tree.add(30)
    tree.add(4)
    actual = tree.postOrder()
    expected = [4,2,30,10]
    assert actual == expected


def test_in_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(2)
    tree.add(30)
    tree.add(4)
    actual = tree.inOrder()
    expected = [2, 4, 10, 30]
    assert actual == expected


def test_contain_true():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(2)
    tree.add(30)
    tree.add(4)
    actual = tree.contains(4)
    expected = True
    assert actual == expected


def test_contain_false():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(2)
    tree.add(30)
    tree.add(4)
    actual = tree.contains(1)
    expected = False
    assert actual == expected
# Testing Find Max Value Method
# Happy Path
def test_find_max_value_true():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    actual = tree.find_maximum_value()
    expected = 5
    assert actual == expected

# Happy Case
def test_find_max_value_true():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(5)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    actual = tree.find_maximum_value()
    expected = 5
    assert actual == expected

# Edge Case
def test_find_max_value_negatives():
    tree = BinarySearchTree()
    tree.add(-1)
    tree.add(-5)
    tree.add(-2)
    tree.add(-3)
    tree.add(-4)
    actual = tree.find_maximum_value()
    expected = -1
    assert actual == expected

# Find max of all zeroes
def test_find_max_value_zeroes():
    tree = BinarySearchTree()
    tree.add(0)
    tree.add(0)
    tree.add(0)
    tree.add(0)
    tree.add(0)
    actual = tree.find_maximum_value()
    expected = False
    assert actual == expected


def test_find_max_value_empty():
    tree = BinarySearchTree()
    actual = tree.find_maximum_value()
    expected = False
    assert actual == expected